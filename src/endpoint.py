# |-------------------------------------------------------------------------------------------------------------------------------
# | By: Christian Toro |
# |-------------------------------------------------------------------------------------------------------------------------------
# | Sources: |
# |----------| HTTP Requests Library
# |----------| https://docs.python-requests.org/en/master/

import requests
import sys
from urllib.parse import urlparse, parse_qs
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
        print('error')
        return ''
    return formatted_data

#---------------------------------------------------------------------------------------------------------------------
# Function that will get all json data from the endpoint
# First endpoint returns multiple endpoints under member key
# Subsequent for loop will retrieve the json data from each individual end point
# Returns the data as a list
def consume_endpoint(ENDPOINT: tuple, API_KEY: tuple):
    try:
        # Get request for the endpoint
        response = requests.get(ENDPOINT[0])
        table_row_list = list()
        # If failure to call first api call, exit the program
        if 'json' not in response.headers.get('Content-Type'): 
            print('Error retrieving data from api endpoint.')
            return []
        # Obtain data from each endpoint from the response and format data into html element
        for member in response.json()['member']:
            response_data = requests.get(member['link'], params={'apikey': API_KEY[0], 'format': 'json'})
            formatted_data = parse_data(response_data.json())
            table_row_list.append(formatted_data)
    except:
        print('Error retrieving data from api endpoint.')
        return []
    # Returns the html elements with the data as one string
    return "".join(table_row_list)

#---------------------------------------------------------------------------------------------------------------------
# Simple function for getting api key from the endpoint
def get_api_key(ENDPOINT: tuple):
    try:
        # Parses url into a 6 item tuple
        endpoint_string = urlparse(ENDPOINT[0])
        if 'apikey' not in endpoint_string.query:
            raise ValueError()
    except:
        print('No API key found!')
        return ''
    # Will get the dictionary from query and return the API key
    return parse_qs(endpoint_string.query)['apikey']

#---------------------------------------------------------------------------------------------------------------------
# Function to get the json data from the endpoint passed in as the second argument
# If error in consuming the api, program will exit
def get_api_data():
    ENDPOINT = tuple([sys.argv[2]])
    API_KEY = tuple([get_api_key(ENDPOINT)])
    data = consume_endpoint(ENDPOINT, API_KEY)
    return data