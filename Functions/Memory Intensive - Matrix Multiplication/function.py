import http.server
import socketserver
import urllib.parse
import json
import random

PORT = 8080  # The port to listen on (make sure it matches the EXPOSE line in Dockerfile)

def generate_random_matrix(rows, cols):
    matrix = [[random.randint(0, 9) for _ in range(cols)] for _ in range(rows)]
    return matrix

def matrix_multiply(matrix_a, matrix_b):
    result = []
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0])

    if cols_a != rows_b:
        return "Invalid input. Number of columns in matrix A must match number of rows in matrix B."

    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            element = 0
            for k in range(cols_a):
                element += matrix_a[i][k] * matrix_b[k][j]
            row.append(element)
        result.append(row)

    return result

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        try:
            query_params = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            a = int(query_params.get('a', ['0'])[0])
            b = int(query_params.get('b', ['0'])[0])
            x = int(query_params.get('x', ['0'])[0])
            y = int(query_params.get('y', ['0'])[0])

            matrix_a = generate_random_matrix(a, b)
            matrix_b = generate_random_matrix(x, y)

            result = matrix_multiply(matrix_a, matrix_b)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(result).encode())
        except (ValueError, IndexError):
            self.send_response(400)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Invalid input. Please provide valid values for a, b, x, and y.")

if __name__ == "__main__":
    # Configure the HTTP server to listen on the specified port
    with socketserver.TCPServer(("", PORT), MyHttpRequestHandler) as httpd:
        print(f"Server started on port {PORT}")
        httpd.serve_forever()
