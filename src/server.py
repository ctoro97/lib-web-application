# |-------------------------------------------------------------------------------------------------------------------------------
# | By: Christian Toro |
# |-------------------------------------------------------------------------------------------------------------------------------

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
        poll_interval_value = 0.5
        http_server.serve_forever(poll_interval=poll_interval_value)
    except KeyboardInterrupt:
        http_server.server_close()
    
    print('Server closed.')
