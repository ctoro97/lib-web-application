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
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

if len(sys.argv) != 3: sys.exit("Must Input Two Required Arguments: PORT API_ENDPOINT")

try:
    PORT = int(sys.argv[1])
    if PORT < 0 or PORT > 65535: raise ValueError()
except ValueError as err: 
    sys.exit("PORT must be a valid number between 0 and 65535")
except Exception as err: 
    sys.exit(f"Error when converting argument to PORT number: {err}")

if __name__ == "__main__":
    server_address = ("localhost", PORT)
    http_server = ThreadingHTTPServer(server_address, BaseHTTPRequestHandler)

    try:
        print(f"Server listening on localhost:{PORT}")
        http_server.serve_forever(poll_interval=0.5)
    except KeyboardInterrupt:
        http_server.server_close()
    
    print("Server closed.")