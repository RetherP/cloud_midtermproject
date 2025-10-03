from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_word():
    return "<b>Hello Word</b>" \
    "<p>This is an test webpage for the project</p>" \
    "<br>" \
    "<p>This is now running from the docker container</p>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)