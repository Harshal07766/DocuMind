"""
Minimal test function for Vercel
"""
def handler(request):
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': '{"message": "Hello from Vercel!", "status": "ok"}'
    }
