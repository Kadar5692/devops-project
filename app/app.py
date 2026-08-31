from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>My DevOps Project</title>
        </head>
        <body>
            <h1>🚀 My DevOps Project</h1>
            <h2>Flask Application</h2>
            <p>Application is running successfully!</p>
            <p>Version: 1.1</p>
        </body>
    </html>
    """


@app.route("/health")
def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)