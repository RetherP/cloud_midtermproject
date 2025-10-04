from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_word():
    return """
        <head>
            <title>Cloud Project Website</title>
            <link rel="icon" href="img/cloud_icon.png">
        </head>
        <body>
            <center>
                <h1> Hello Word </h1>
                <p>This is a demo webpage for the midterm project</p>
                <hr>
                <p>This code is running from a Docker Container on Azure VM deployed via Github Actions </p>
                <h2>The Deployment Status</h2>
                <a href="https://github.com/RetherP/cloud_midtermproject/actions/workflows/main.yml">
                    <img src="https://github.com/RetherP/cloud_midtermproject/actions/workflows/main.yml/badge.svg">            
                </a>
            </center>
        </body>
    """


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)