# Ex Libris Alma API Consumer
The Ex Libris Alma API Consumer is a simple application that consumes an API from Ex Libris Alma, a unified library services platform.

## Description
This is a project completed as part of the interview process for the University of Miami Libraries. The purpose of the project is to consume an API endpoint from the Ex Libris Alma library service platform and display it on an HTML page. The data is sortable by title and data of publication as requested.  

The HTML is styled using some of the university's brand guidelines (see sources below). The project is not an official application or website for the university.

## Usage

### Configuration
Before using the application, install the python library requests.
```bash
pip install requests
```
In addition, set up the config.py file. View the example_config.py file for more details.

### Running
To run the program use the following command from the src directory.
```bash
python server.py
```
Following that, open your browser to __localhost:PORT_NUMBER.__ After the page loads, you will be able  
to view the data and sort it.

### Errors
Errors will be logged to a file call __error.log.__ 

## Author
Christian Toro

## Sources
### Ex Libris and Library Standards
1. Ex Libris Alma
    - General Information
        - https://exlibrisgroup.com/products/alma-library-services-platform/open-platform/
    - REST API
        - https://developers.exlibrisgroup.com/alma/apis/#defining
2. _ISBN Format_
    - https://www.isbn-international.org/content/what-isbn#:~:text=An%20ISBN%20is%20an%20International,digit%20to%20validate%20the%20number.
3. _Library of Congress Call Number Format_
    - https://www.library.northwestern.edu/find-borrow-request/catalogs-search-tools/understanding-call-numbers/sudoc.html
    - https://www.loc.gov/catdir/cpso/lcco/

### Code
1. _How to set up HTTP Server_
    - https://docs.python.org/3/library/http.server.html  
2. _More on the HTTP Server functionality_ 
    - https://docs.python.org/3/library/socketserver.html#socketserver.TCPServer
3. _Using KeyboardInterrupt Exception to close server_
    - https://stackoverflow.com/questions/42763311/how-to-shut-down-python-server
4. _How to exit program_
    - https://www.geeksforgeeks.org/python-exit-commands-quit-exit-sys-exit-and-os-_exit/
5. _Implementation of BaseHTTPRequestHandler (same as setting up server)_
    - https://docs.python.org/3/library/http.server.html
6. _Pass data to html file from python_
    - https://stackoverflow.com/questions/41354948/passing-variables-to-html-file-on-python
7. _HTTP Requests Library_
    - https://docs.python-requests.org/en/master/
8. _Python Logging_
    - https://docs.python.org/3/howto/logging.html
9. _Python Regex_
    - https://www.w3schools.com/python/python_regex.asp

### Additional
1. _University of Miami Brand Guidelines_
    - General
        - https://ucomm.miami.edu/_assets/pdf/tools-and-resources/umiami-visual-identity-guide.pdf
    - Web
        - https://webcomm.miami.edu/resources/identity/um-2016/index.html