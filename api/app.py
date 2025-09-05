"""
Modern Vercel Python function
"""
def handler(request):
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html',
            'Access-Control-Allow-Origin': '*'
        },
        'body': '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>DocuMind AI</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }
                .container { max-width: 600px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; }
                h1 { color: #333; text-align: center; }
                .status { background: #e8f5e8; padding: 15px; border-radius: 5px; margin: 20px 0; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🧠 DocuMind AI</h1>
                <div class="status">
                    <h3>✅ Server Status: Running</h3>
                    <p>DocuMind AI is successfully deployed on Vercel!</p>
                </div>
            </div>
        </body>
        </html>
        '''
    }
