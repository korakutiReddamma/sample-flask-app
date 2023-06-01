from flask import Flask
app = Flask(__name__)

@app.route('/route1')
def route1():
    return 'Hello from route1!'
@app.route('/route2')
def route2():
    return 'Hello from route2!'
@app.route('/route3')
def route3():
    return 'Hello from route3!'
@app.route('/route4')
def route4():
    return 'Hello from route4!'
@app.route('/route5')
def route5():
    return 'Hello from route5!'
@app.route('/route6')
def route6():
    return 'Hello from route6!'
@app.route('/route7')
def route7():
    return 'Hello from route7!'
@app.route('/route8')
def route8():
    return 'Hello from route8!'
@app.route('/route9')
def route9():
    return 'Hello from route9!'
@app.route('/route10')
def route10():
    return 'Hello from route10!'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=100,debug=True)
    