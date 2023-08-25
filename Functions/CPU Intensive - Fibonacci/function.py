import http.server
import socketserver

PORT = 8080 # The port to listen on (make sure it matches the EXPOSE line in Dockerfile)

def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please provide a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        try:
            # Get the value of the 'n' query parameter from the request URL
            n = int(self.path.split('?')[-1].split('=')[-1])
            result = fibonacci(n)

            # Send the Fibonacci result as the response
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(str(result).encode())
        except ValueError:
            # If 'n' is not a valid integer, return an error message
            self.send_response(400)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Invalid input. Please provide a positive integer.")

if __name__ == "__main__":
    # Configure the HTTP server to listen on the specified port
    with socketserver.TCPServer(("", PORT), MyHttpRequestHandler) as httpd:
        print(f"Server started on port {PORT}")
        httpd.serve_forever()
