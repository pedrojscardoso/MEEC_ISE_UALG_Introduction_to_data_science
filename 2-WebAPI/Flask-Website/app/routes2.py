from app import app


things = [{'id': 1, 'name': 'Prometheus'}]

@app.route('/')
@app.route('/index')
def index():
    return '''
        <html>
            <head>
                <title>Home Page</title>
            </head>
            <body>
                <h1>Thing: ''' + things[0]['name'] + '''!</h1>
            </body>
        </html>'''
