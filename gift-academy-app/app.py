from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

# Define the port number
PORT = 8080

# Create the HTTP server
Handler = SimpleHTTPRequestHandler

with TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
