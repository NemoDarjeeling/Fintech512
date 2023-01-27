import sys, os, http.server

#-------------------------------------------------------------------------------

class ServerException(Exception):
    '''For internal error reporting.'''
    pass

#-------------------------------------------------------------------------------

class RequestHandler(http.server.BaseHTTPRequestHandler):
    '''
    If the requested path maps to a file, that file is served.
    If anything goes wrong, an error page is constructed.
    '''

    # How to display an error.
    Error_Page = """\
        <html>
        <body>
        <h1>Error accessing {path}</h1>
        <p>{msg}</p>
        </body>
        </html>
        """

    # Classify and handle request.
    def do_GET(self):
    #The method do_GET is called as part of the request handling process in the RequestHandler class. It is defined as a method on the http.server.BaseHTTPRequestHandler class, which RequestHandler inherits from. When a GET request is received by the server, this method is called to handle the request and generate a response.
        try:

            # Figure out what exactly is being requested.
            full_path = os.getcwd() + self.path
# os.getcwd() is a function from the os module of the python standard library. It stands for "get current working directory" and it returns the current working directory(cwd) of the process as a string.
# In the given code, it is used to concatenate the full path for a file that the client is requesting.
# full_path = os.getcwd() + self.path
# It's the current directory where the python script is running, so it will be the root directory of the server.

            # It doesn't exist...
            if not os.path.exists(full_path):
                raise ServerException("'{0}' not found".format(self.path))

            # ...it's a file...
            elif os.path.isfile(full_path):
                self.handle_file(full_path)

            # ...it's something we don't handle. exists but not a file
            else:
                raise ServerException("Unknown object '{0}'".format(self.path))

        # Handle errors.
        except Exception as msg:
            self.handle_error(msg)

    def handle_file(self, full_path):
        try:
            with open(full_path, 'rb') as reader:
                content = reader.read()
            self.send_content(content)
        except IOError as msg:
            msg = "'{0}' cannot be read: {1}".format(self.path, msg)
            self.handle_error(msg)

    # Handle unknown objects.
    def handle_error(self, msg):
        content = self.Error_Page.format(path=self.path, msg=msg)
        self.send_content(content)

    # Send actual content.
    def send_content(self, content):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        #self.wfile.write(content.encode('utf-8'))
        #important here, as the content of the error page is a string, which is a Unicode object. However, the write() method of the self.wfile object expects bytes, not a string. By encoding the string to UTF-8, you are converting it to a bytes object which can be sent over the network using the write() method.
        #but if you want to display a html, use line below
        self.wfile.write(content)

#-------------------------------------------------------------------------------

if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = http.server.HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()

#why it only says ServerException: '/path_that_does_not_exist' not found, but there is no message of "Error accessing /path_that_does_not_exist"?
#This is because the message in the handle_error method is not being displayed. The handle_error method is only constructing the error page with the message ServerException: '/path_that_does_not_exist' not found and the path requested, but it is not sending it to the browser.
#You need to add self.wfile.write(content.encode('utf-8')) or self.wfile.write(content) to send the constructed error page to the browser.