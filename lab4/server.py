from http.server import HTTPServer, CGIHTTPRequestHandler
import os


# os.system('chmod a+x /cgi-bin/test_json.sh')

server_address = ("", 8000)
http_server = HTTPServer(server_address, CGIHTTPRequestHandler)
http_server.serve_forever()
os.system('chmod a+x /cgi-bin/*.py')