from http.server import HTTPServer, CGIHTTPRequestHandler
import os
server_address = ("", 8000)
http_server = HTTPServer(server_address, CGIHTTPRequestHandler)
os.system('chmod a+x /cgi-bin/*.py')
os.system('chmod a+x /cgi-bin/test_json.sh')
http_server.serve_forever()