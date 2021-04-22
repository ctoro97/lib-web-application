# |-------------------------------------------------------------------------------------------------------------------------------
# | By: Christian Toro |
# |-------------------------------------------------------------------------------------------------------------------------------
# | Sources: |
# |----------| HTTP Requests Library
# |----------| https://docs.python-requests.org/en/master/

import requests
import sys

# Function that parses the endpoint response data and adds it to html elements in a string
def parse_data(data):
    formatted_data = ''
    try:
        formatted_data += '<tr>'
        formatted_data += '<td>' + data['bib_data']['title'] + '</td>'
        formatted_data += '<td>' + data['bib_data']['author'] + '</td>'
        formatted_data += '<td>' + data['bib_data']['isbn'] + '</td>'
        formatted_data += '<td>' + data['bib_data']['date_of_publication'] + '</td>'
        formatted_data += '<td>' + data['holding_data']['call_number'] + '</td>'
        formatted_data += '</tr>'
    except:
        return ''
    return formatted_data

# Function that will get all json data from the endpoint
# First endpoint returns multiple endpoints under member key
# Subsequent for loop will retrieve the json data from each individual end point
# Returns the data as a list
def consume_endpoint(ENDPOINT: tuple, API_KEY: tuple):
    try:
        first_data_set = requests.get(ENDPOINT[0])
        second_data_set = list()

        # If failure to call first api call, exit the program
        if 'json' not in first_data_set.headers.get('Content-Type'): 
            print('Error retrieving data from api endpoint.')
            return []
        
        for member in first_data_set.json()['member']:
            new_endpoint = member['link']
            params = {'apikey': API_KEY[0], 'format': 'json'}
            response_data = requests.get(new_endpoint, params=params)
            formatted_data = parse_data(response_data.json())
            second_data_set.append(formatted_data)

        final_data_set = "".join(second_data_set)
    except Exception as err:
        print(err)
        return []
    
    return final_data_set

# Simple function for getting api key from the endpoint
def get_api_key(ENDPOINT: tuple):
    left_bound = 7 + ENDPOINT[0].index('apikey')
    right_bound = ENDPOINT[0].index('&')
    return ENDPOINT[0][left_bound:right_bound]

# Function to get the json data from the endpoint passed in as the second argument
# If error in consuming the api, program will exit
def get_api_data():
    ENDPOINT = tuple([sys.argv[2]])
    API_KEY = tuple([get_api_key(ENDPOINT)])
    data = consume_endpoint(ENDPOINT, API_KEY)
    return data
