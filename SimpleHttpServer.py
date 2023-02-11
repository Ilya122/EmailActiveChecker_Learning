from http.server import HTTPServer, BaseHTTPRequestHandler
import shutil
import os

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        file = str(self.path[1:])

        if('@' in file and not '_cat.jpg' in file):
            shutil.copy('cat.jpg', file + '_cat.jpg')
            return

        with open(file, 'rb') as f:
            print(f"Email {str(file[:-8])} is active")
            content = f.read()
            print(file)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(content)
        os.remove(file)


httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
