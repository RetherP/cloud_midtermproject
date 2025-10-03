from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_word():
    return "<b>Hello Word</b>" \
    "<p>This is an test webpage for the project</p>"


if __name__ == '__main__':
    app.run()