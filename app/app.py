from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>My DevOps Project</title>
        </head>
        <body>
            <p>Application is running successfully!</p>

<h3>💡 “The secret of getting ahead is getting started.”</h3>

<p>🚀 💻 🔥</p>

<p>Version: 1.2 - Auto Deployment Test</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))