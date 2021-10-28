from http.server import BaseHTTPRequestHandler, HTTPServer
import ssl


class run_server(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()

    def do_GET(self):
        self._set_headers()
        print(self.path)
        self.wfile.write(b'<html><body><h1>Get Request Received!</h1></body></html>')

    def do_POST(self):
        self._set_headers()
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST'}
        )
        print(form.getvalue("foo"))
        print(form.getvalue("bin"))
        self.wfile.write("<html><body><h1>POST Request Received!</h1></body></html>")

def run(server_class=HTTPServer, handler_class=run_server, server_address='127.0.0.1', port=80):
    
    httpd = server_class((server_address, port), handler_class)
    
    print("Server running at "+server_address+":"+str(port)+"...")
    httpd.serve_forever()

server_address = '127.0.0.1'
server_port = 80
run(server_address=server_address, port=server_port)