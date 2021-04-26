# |-------------------------------------------------------------------------------------------------------------------------------
# | By: Christian Toro |
# |-------------------------------------------------------------------------------------------------------------------------------
# | Sources: |
# |----------| Implementation of BaseHTTPRequestHandler (same as setting up server)
# |----------| https://docs.python.org/3/library/http.server.html
# |----------| Pass data to html file from python
# |----------| https://stackoverflow.com/questions/41354948/passing-variables-to-html-file-on-python

from http.server import BaseHTTPRequestHandler
from endpoint import get_api_data

# Child class for the BaseHTTPRequestHandler to implement the GET requests
class HTTPHandler(BaseHTTPRequestHandler):
    # Implementation of the GET Method for HTTP Requests
    def do_GET(self):
        # Set default status code and content to 404 not found
        status_code = 404
        content_type = 'text/plain'
        file_content = '404 Page Not Found'

        # If the url is the index then display the index.html file
        if self.path == '/':
            data = get_api_data()
            status_code = 200
            content_type = 'text/html'
            file_content = open('components/search-results/index.html').read().format(data=data)
        
        # Get the CSS file to style the HTML page
        if self.path == '/styles.css':
            status_code = 200
            content_type = 'text/css'
            file_content = open('components/search-results/styles.css').read()

        # Get the JavaScript file for sorting table data and manipulating the HTML DOM
        if self.path == '/main.js':
            status_code = 200
            content_type = 'text/javascript'
            file_content = open('components/search-results/main.js').read()
        
        # Add response header with status code to log requests
        # Send header with content type and also send the content
        self.send_response(status_code)
        self.send_header('Content-Type', content_type)
        self.end_headers()
        self.wfile.write(bytes(file_content, 'utf-8'))
