# |-------------------------------------------------------------------------------------------------------------------------------
# | By: Christian Toro |
# |-------------------------------------------------------------------------------------------------------------------------------
# | Sources: |
# |----------| HTTP Requests Library
# |----------| https://docs.python-requests.org/en/master/

import requests
import sys
import logging
from config import API_KEY, ENDPOINT
from data_formatter import author_format, call_number_format, date_format, isbn_format, title_format

#---------------------------------------------------------------------------------------------------------------------
# Function that parses the endpoint response data and adds it to html elements in a string
def parse_data(data):
    formatted_data = ''
    try:
        formatted_data += '<tr><td>' + title_format(data, 'bib_data', 'title') + '</td>'
        formatted_data += '<td>' + author_format(data, 'bib_data', 'author') + '</td>'
        formatted_data += '<td>' + isbn_format(data, 'bib_data', 'isbn') + '</td>'
        formatted_data += '<td>' + date_format(data, 'bib_data', 'date_of_publication') + '</td>'
        formatted_data += '<td>' + call_number_format(data, 'holding_data', 'call_number') + '</td></tr>'
    except:
        logging.error('Error formatting the data in parse_data.')
        return ''
    return formatted_data

#---------------------------------------------------------------------------------------------------------------------
# Function that will get all json data from the endpoint
# First endpoint returns multiple endpoints under member key
# Subsequent for loop will retrieve the json data from each individual end point
# Returns the data as a list
def consume_endpoint(API_ENDPOINT: tuple, KEY: tuple):
    try:
        # Get request for the endpoint
        response = requests.get(API_ENDPOINT[0], params={'apikey': KEY[0], 'format': 'json'})
        table_row_list = list()
        # If failure to call first api call, exit the program
        if 'json' not in response.headers.get('Content-Type'): 
            logging.error('ENDPOINT response did not come in the form of json. Ensure json format is being returned.')
            return ''
        # Obtain data from each endpoint from the response and format data into html element
        for member in response.json()['member']:
            response_data = requests.get(member['link'], params={'apikey': KEY[0], 'format': 'json'})
            formatted_data = parse_data(response_data.json())
            table_row_list.append(formatted_data)
    except:
        logging.error('Error retrieving data from api endpoint and response endpoints.')
        return ''
    # Returns the html elements with the data as one string
    return "".join(table_row_list)

#---------------------------------------------------------------------------------------------------------------------
# Function to get the json data from the endpoint passed in as the second argument
# If error in consuming the api, function will return empty string
def get_api_data():
    try:
        API_ENDPOINT = tuple([ENDPOINT[0]],)
        KEY = tuple([API_KEY[0]],)
    except IndexError:
        logging.error('No ENDPOINT or API_KEY were found.')
        return ''
    except:
        logging.error('Unknown error. Ensure ENDPOINT and API_KEY are set up correctly.')
        return ''
    data = consume_endpoint(API_ENDPOINT, KEY)
    return data
