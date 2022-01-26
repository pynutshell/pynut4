"""
debug_test.py: create and interact with the FastAPI app object.
"""
from server2 import app
from wsgiref.simple_server import make_server

app.debug = True

with make_server('', 8000, app) as httpd:
    print("Serving HTTP on port 8000...")

    # Respond to requests until process is killed
    httpd.serve_forever()

    # Alternative: serve one request, then exit
    httpd.handle_request()

