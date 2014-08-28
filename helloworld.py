from bottle import Bottle

app = Bottle()

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)