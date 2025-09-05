"""
Vercel Serverless Function Entry Point for DocuMind AI
"""
import json
import os

def handler(request):
    """Vercel serverless function handler"""
    
    try:
        # Handle different HTTP methods
        if request.method == 'GET':
            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'text/html',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
                    'Access-Control-Allow-Headers': 'Content-Type, Authorization'
                },
                'body': '''
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>DocuMind AI</title>
                    <style>
                        body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }
                        .container { max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
                        h1 { color: #333; text-align: center; }
                        .status { background: #e8f5e8; padding: 15px; border-radius: 5px; margin: 20px 0; }
                        .note { background: #fff3cd; padding: 15px; border-radius: 5px; margin: 20px 0; }
                        .warning { background: #f8d7da; padding: 15px; border-radius: 5px; margin: 20px 0; }
                    </style>
                </head>
                <body>
                    <div class="container">
                        <h1>🧠 DocuMind AI</h1>
                        <div class="status">
                            <h3>✅ Server Status: Running</h3>
                            <p>DocuMind AI is successfully deployed on Vercel!</p>
                        </div>
                        <div class="warning">
                            <h3>⚠️ Limited Functionality</h3>
                            <p>This is a simplified serverless deployment. PDF processing is disabled due to Vercel build constraints. For full functionality including PDF processing, deploy to Railway, Render, or use Docker.</p>
                        </div>
                        <div class="note">
                            <h3>📝 Supported Features</h3>
                            <ul>
                                <li>✅ Text document processing</li>
                                <li>✅ DOCX file processing</li>
                                <li>✅ Basic API endpoints</li>
                                <li>❌ PDF processing (disabled)</li>
                                <li>❌ Image OCR (disabled)</li>
                            </ul>
                        </div>
                    </div>
                </body>
                </html>
                '''
            }
        
        elif request.method == 'POST':
            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({
                    'message': 'DocuMind AI API',
                    'status': 'running',
                    'note': 'Simplified serverless deployment - PDF processing disabled',
                    'supported_formats': ['txt', 'docx'],
                    'unsupported_formats': ['pdf', 'images']
                })
            }
        
        else:
            return {
                'statusCode': 405,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'error': 'Method not allowed'})
            }
    
    except Exception as e:
        # Return error response if something goes wrong
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({
                'error': 'Internal server error',
                'message': str(e),
                'status': 'error'
            })
        }