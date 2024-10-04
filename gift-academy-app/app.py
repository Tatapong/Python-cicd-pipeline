from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

# Define the port number
PORT = 8081

# Create the HTTP server
Handler = SimpleHTTPRequestHandler

# Bind the server to all network interfaces by using ""
# This makes the server accessible from outside the container.
with TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
