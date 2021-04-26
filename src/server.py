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
import logging
from http.server import ThreadingHTTPServer
from http_handler import HTTPHandler
from config import PORT

if __name__ == '__main__':

    logging.basicConfig(filename='error.log', level=logging.INFO, format='[%(asctime)s] %(name)s | %(levelname)s: %(message)s')

    # Set up the server and exit program if PORT is not valid
    try:
        server_address = ('localhost', PORT[0])
        http_server = ThreadingHTTPServer(server_address, HTTPHandler)
    except OverflowError:
        logging.error('PORT number is not valid. Must be between 0 and 65535 (inclusive).')
        sys.exit(1)
    except TypeError:
        logging.error('PORT must be a number between 0 and 65535 (inclusive).')
        sys.exit(1)
    except:
        logging.error('Error setting up the HTTP server. Check to ensure PORT is set up correctly.')
        sys.exit(1)

    # Run the server and quit on keyboard interrupt
    try:
        print(f'Server listening on localhost:{PORT[0]}')
        http_server.serve_forever(poll_interval=0.5)
    except KeyboardInterrupt:
        http_server.server_close()
    
    print('Server closed.')
