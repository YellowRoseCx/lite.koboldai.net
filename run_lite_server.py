import http.server
import socketserver

PORT = 5005
IP_ADDRESS = "0.0.0.0"

class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', 'null') 
        http.server.SimpleHTTPRequestHandler.end_headers(self)

with socketserver.TCPServer((IP_ADDRESS, PORT), CORSRequestHandler) as httpd:
    print(f"serving KoboldAI-Lite at {IP_ADDRESS}:{PORT}")
    httpd.serve_forever()
