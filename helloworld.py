from bottle import Bottle, request

app = Bottle()

@app.route('/', method='GET')
def echo():
    return {key: request.headers.get(key) for key in request.headers}

if __name__ == '__main__':
    app.run(host='localhost', port=8080, reloader=True, debug=True)
