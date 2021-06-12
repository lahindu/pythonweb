from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "0.0.0.0"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes("<html><body><h1>Hi...</h1></body></html>", "utf-8"))


server_object = HTTPServer(server_address=(hostName, serverPort), RequestHandlerClass=MyServer)
print("Server started http://%s:%s" % (hostName, serverPort))
server_object.serve_forever()
