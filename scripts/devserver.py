"""Static dev server that never caches — the browser pane holds onto
css/js hard enough that edits went unnoticed during review."""
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

class NoCache(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, max-age=0')
        super().end_headers()
    def log_message(self, *a):
        pass
    def do_POST(self):
        # stands in for Netlify Forms so the contact form can be exercised locally
        self.rfile.read(int(self.headers.get('Content-Length') or 0))
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'ok')

class Server(ThreadingHTTPServer):
    # the page asks for dozens of images at once; the default backlog of 5
    # reset connections and left random images blank
    request_queue_size = 128
    daemon_threads = True

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    Server(('127.0.0.1', port), NoCache).serve_forever()
