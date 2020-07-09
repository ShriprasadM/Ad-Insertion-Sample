#!/usr/bin/python3

import time
import http.server
import socketserver
import requests
import threading
import gadserver
import sample
import json
from urllib.parse import urlparse
from urllib.parse import parse_qs

import process


HOST_NAME = '' # !!!REMEMBER TO CHANGE THIS!!!
PORT_NUMBER = 9008 # Maybe set this to 9000.


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    
    def do_GET(s):
        """Respond to a GET request."""
        params = parse_qs(urlparse(s.path).query)
        print(params)
        stream =  process.ADClipDecision(None, None, False, params)
        vast = process.createMergedVast(stream)
        print(vast)
        if None == vast :
            s.send_response(500)
            s.wfile.write("error in getting vast")
        else:
            s.send_response(200)
            s.send_header("Content-type", "application/xml")
            s.end_headers()
            s.wfile.write(vast.encode())


def runServer():
    httpd = socketserver.TCPServer((HOST_NAME, PORT_NUMBER), Handler)   
    print(time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER))

def runServerInBackgroud():
    th = threading.Thread(target=runServer)
    th.start()

if __name__ == '__main__':
   runServer()