"""
Vercel Python function - correct format
"""
from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<h1>DocuMind AI - Working!</h1><p>Serverless function is running successfully.</p>')
    
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        response = {'message': 'DocuMind AI API', 'status': 'running'}
        self.wfile.write(json.dumps(response).encode())
