import time
from urllib.parse import urlparse
from http.server import BaseHTTPRequestHandler
from http.server import ThreadingHTTPServer

__VERSION__ = "0.1"
PORT = 8000


class HTTPMockRequestHandler(BaseHTTPRequestHandler):
    def code(self, code):
        try:
            return int(code)
        except ValueError:
            pass
        return None

    def slow(self, code):
        time.sleep(5)
        return self.code(code)

    def parse_route(self):
        # Separate the path output
        path = urlparse(self.path).path

        route = path.split("/")
        if route[1] == "slow":
            return self.slow(route[2])
        if route[1] == "code":
            return self.code(route[2])
        return None

    def process_request(self):
        code = self.parse_route()
        if code:
            self.send_response(code)
            self.end_headers()
            resp = f"HTTP {code} response"
            self.wfile.write(resp.encode("ascii"))
        else:
            self.send_response(404, message="Not Found")
            self.end_headers()
            self.wfile.write(b"Unknown path")

    def do_GET(self):
        self.process_request()

    def do_PUT(self):
        self.process_request()

    def do_POST(self):
        self.process_request()


def main():
    httpd = ThreadingHTTPServer(("", PORT), HTTPMockRequestHandler)

    print("serving at port", PORT)
    httpd.serve_forever()


if __name__ == "__main__":
    main()
