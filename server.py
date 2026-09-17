from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


DIST_DIR = Path(__file__).parent / "dist"


class SpaHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIST_DIR), **kwargs)

    def do_GET(self):
        requested_path = DIST_DIR / self.path.lstrip("/").split("?", 1)[0]
        if self.path != "/" and not requested_path.is_file():
            self.path = "/index.html"
        super().do_GET()


if __name__ == "__main__":
    server = ThreadingHTTPServer(("0.0.0.0", 8000), SpaHandler)
    print("Elsherif Store is running on port 8000")
    server.serve_forever()
