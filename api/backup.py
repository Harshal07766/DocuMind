"""
Backup Python function for Vercel
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
        <head><title>DocuMind AI</title></head>
        <body>
            <h1>🧠 DocuMind AI</h1>
            <p>✅ Serverless function is working!</p>
        </body>
        </html>
        '''
    }
