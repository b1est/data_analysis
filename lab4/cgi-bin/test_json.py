#!/usr/bin/python3

# import re
# import subprocess

import os
import cgi
form = cgi.FieldStorage()
query = form.getfirst("query", "Query not defined")
src = form.getfirst("src", "Source not defined")
os.system(f'./cgi-bin/test_json.sh {query} {src}')
