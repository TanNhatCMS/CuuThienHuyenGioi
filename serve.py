"""Serve the game locally with cross-origin isolation headers (Godot web export)."""
import http.server
import socketserver


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        super().end_headers()


if __name__ == "__main__":
    with socketserver.TCPServer(("127.0.0.1", 8123), Handler) as httpd:
        print("Serving at http://127.0.0.1:8123/")
        httpd.serve_forever()
