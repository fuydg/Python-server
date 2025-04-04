import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
import argparse
import socket

def run_server(port=8000, directory="src"):
    try:
        os.chdir(directory)
        print(f"Server started and accessible at http://localhost:{port}")
        server_address = ("", port)
        httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
        print(f"Serving directory: {os.getcwd()}")
        httpd.serve_forever()
    except OSError as e:
        if e.errno == socket.errno.EADDRINUSE:
            print(f"Error: Port {port} is already in use. Please try another port.")
        else:
            print(f"Error starting server: {e}")
    except FileNotFoundError:
        print(f"Error: Directory '{directory}' not found. Please check.")
    except KeyboardInterrupt:
        print("\nServer stopped.")
        if 'httpd' in locals():
            httpd.shutdown()
    finally:
        if 'httpd' in locals():
            httpd.server_close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start a simple HTTP server.")
    parser.add_argument("-p", "--port", type=int, default=8000, help="Port number to listen on (default: 8000)")
    parser.add_argument("-d", "--directory", type=str, default="src", help="Directory to serve static files from (default: 'src')")
    args = parser.parse_args()

    run_server(port=args.port, directory=args.directory)
