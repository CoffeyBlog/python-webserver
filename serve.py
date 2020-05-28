from http.server import BaseHTTPRequestHandler, HTTPServer      # Import the Request Handler & Server from the http.server module

class HTTPServer_RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):                                           # If someone sends a GET request to our server show
        self.send_response(200)                                 # Response 200 - OK - The request has succeeded
        self.send_header("Content-type", "text/html")           # The CONTENT-TYPE that we will produce via our webserver is HTML
        self.end_headers()                                      # ...End this header ^
    # Here we are going to use python code to dynamically generate - what is typically a static html website.
    # Our servers name is self ... so anytime you see the variable self being called we are asking our server to do something.

        self.wfile.write(b"<!DOCTYPE html>")
        self.wfile.write(b"<html lang='en'>")
        self.wfile.write(b"<head>")
        self.wfile.write(b"<title>Python</title>")
        self.wfile.write(b"</head>")
        self.wfile.write(b"<body>")
        self.wfile.write(b"Hello, World!")
        self.wfile.write(b"</body>")
        self.wfile.write(b"</html>")
    # That is an HTML page written in Python
    port = 8080                                                     # We are listening on TCP Port 8080
    server_address = ("0.0.0.0", port)                              # the address will be 0.0.0.0.8080
    httpd = HTTPServer(server_address, BaseHTTPRequestHandler)  # We are are storing HTTPServer into http

    httpd.serve_forever()                                           # We are telling the server to start listening for GET requests




