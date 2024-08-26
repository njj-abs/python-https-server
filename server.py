from http.server import HTTPServer, SimpleHTTPRequestHandler

import ssl

PORT = 3020

class CustomHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        super().end_headers()

def run(server_class=HTTPServer, handler_class=CustomHandler):
    server_address = ("0.0.0.0", PORT)
    httpd = server_class(server_address, handler_class)
    print(f"Serving on port {PORT}")

    # Secure the connection using SSL with both cert and key files
    httpd.socket = ssl.wrap_socket(
        httpd.socket,
        certfile="./cert.pem",  # Use your certificate file
        keyfile="./key.pem",  # Use your key file
        server_side=True,
    )

    httpd.serve_forever()


if __name__ == "__main__":
    run()

