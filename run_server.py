import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

def run_server(port=8000):
    os.chdir("src")
    print(f"The server is being started and accessed at http://localhost:{port}")
    server_address = ("", port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    httpd.serve_forever()
                                            if __name__ == "__main__":
    run_server()                        
