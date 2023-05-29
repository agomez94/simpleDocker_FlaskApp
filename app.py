from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello():
    return 'Hello Everyone! This is practice for Docker'
if __name__ == '__main__':
    app.run(debug=True)