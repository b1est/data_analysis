from http.server import HTTPServer, CGIHTTPRequestHandler
from sys import platform
import os


# os.system('chmod a+x /cgi-bin/test_json.sh')

if platform == "linux" or platform == "linux2":
    os.system('sudo chmod a+x cgi-bin/request.py')
server_address = ("", 8000)
http_server = HTTPServer(server_address, CGIHTTPRequestHandler)

http_server.serve_forever()
