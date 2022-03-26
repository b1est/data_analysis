#!/usr/bin/python3

import os
import re
import cgi
import subprocess
form = cgi.FieldStorage()
query = form.getfirst("query", "Query not defined")
src = form.getfirst("src", "Source not defined")
os.system('"/usr/lib/cgi-bin/test_json.sh" %s %s' % (query, src))
