# |-------------------------------------------------------------------------------------------------------------------------------
# | By: Christian Toro |
# |-------------------------------------------------------------------------------------------------------------------------------
# | Sources: |
# |----------| How to get command line arguments and about command line argument in general
# |----------| https://docs.python.org/3/using/cmdline.html
# |----------| How to set up HTTP Server
# |----------| https://docs.python.org/3/library/http.server.html
# |----------| More on the HTTP Server functionality
# |----------| https://docs.python.org/3/library/socketserver.html#socketserver.TCPServer
# |----------| Using KeyboardInterrupt Exception to close server
# |----------| https://stackoverflow.com/questions/42763311/how-to-shut-down-python-server
# |----------| How to exit program
# |----------| https://www.geeksforgeeks.org/python-exit-commands-quit-exit-sys-exit-and-os-_exit/

import sys
import requests
import json
from http.server import ThreadingHTTPServer
from http_handler import HTTPHandler
# from endpoint import consume_endpoint

# Function to check if 2 arguments passed into program
# Program exits if it does not have the 2 arguments
def arguments_check():
    if len(sys.argv) != 3: sys.exit('Must Input Two Required Arguments: PORT API_ENDPOINT')

# Function to convert first argument to integer
# Must be a valid port number otherwise an exception will be raised and the program exits
def get_port():
    try:
        PORT = int(sys.argv[1])
        if PORT < 0 or PORT > 65535: raise ValueError()
    except ValueError as err: 
        sys.exit('PORT must be a valid number between 0 and 65535')
    except Exception as err: 
        sys.exit(f'Error when converting argument to PORT number: {err}')
    return PORT

# Function to get the json data from the endpoint passed in as the second argument
# If error in consuming the api, program will exit
# def get_api_data():
#     try:
#         ENDPOINT = tuple([sys.argv[2]])
#         data = consume_endpoint(ENDPOINT)
#     except Exception as err:
#         sys.exit(f'Error when consuming API from endpoint: {err}')
#     return data

if __name__ == '__main__':

    # First check to see if arguments passed otherwise quit program
    # Then obtain the port number and the data from the endpoint
    arguments_check()
    PORT = tuple([get_port()])
    # data = get_api_data()

    # Set up the server
    server_address = ('localhost', PORT[0])
    http_server = ThreadingHTTPServer(server_address, HTTPHandler)

    # Run the server and quit on keyboard interrupt
    try:
        print(f'Server listening on localhost:{PORT[0]}')
        http_server.serve_forever(poll_interval=0.5)
    except KeyboardInterrupt:
        http_server.server_close()
    
    print('Server closed.')