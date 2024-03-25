from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Hello, world!')

def run():
    httpd = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    httpd.serve_forever()

if __name__ == '__main__':
    run()
