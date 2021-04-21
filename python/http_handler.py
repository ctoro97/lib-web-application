# |-------------------------------------------------------------------------------------------------------------------------------
# | By: Christian Toro |
# |-------------------------------------------------------------------------------------------------------------------------------
# | Sources: |
# |----------| Implementation of BaseHTTPRequestHandler (same as setting up server)
# |----------| https://docs.python.org/3/library/http.server.html
# |----------| Pass data to html file from python
# |----------| https://stackoverflow.com/questions/41354948/passing-variables-to-html-file-on-python

from http.server import BaseHTTPRequestHandler

class HTTPHandler(BaseHTTPRequestHandler):
    # Implementation of the GET Method for HTTP Requests
    def do_GET(self):
        # Set default status code and content to 404 not found
        status_code = 404
        content_type = 'text/plain'
        html_file = '404 Page Not Found'

        # If the url is the index then display the index.html file
        if self.path == '/':
            status_code = 200
            content_type = 'text/html'
            html_file = open('index.html').read().format(data=status_code)
        
        # Add response header with status code to log requests
        # Send header with content type and also send the content
        self.send_response(status_code)
        self.send_header('Content-Type', content_type)
        self.end_headers()
        self.wfile.write(bytes(html_file, 'utf-8'))