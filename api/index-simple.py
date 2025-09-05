"""
Ultra-simple Vercel function
"""
def handler(request):
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'text/html'},
        'body': '<h1>DocuMind AI - Working!</h1><p>Serverless function is running successfully.</p>'
    }
