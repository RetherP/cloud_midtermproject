from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_word():
    return """
        <head>
            <title>Cloud Project Website</title>
            <link rel="icon" href="/img/cloud_icon.png">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
        </head>
        <body>
            <div class="container">
                <div class="row">
                    <div class="col">
                        <h1> Hello Word </h1>
                    </div>
                </div>
                <div class="row">
                    <div class="col">
                        <p>This is a demo webpage for the midterm project</p>
                    </div>
                </div>
                <div class="row">
                    <div class="col">    
                        <p>This code is running from a Docker Container on Azure VM deployed via Github Actions </p>
                </div>
                </div>
                <div class="row">
                    <div class="col">
                        <h2>The Deployment Status</h2>
                        <a href="https://github.com/RetherP/cloud_midtermproject/actions/workflows/main.yml">
                            <img src="https://github.com/RetherP/cloud_midtermproject/actions/workflows/main.yml/badge.svg">            
                        </a>
                </div>
                </div>
                
        </body>
    """


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)