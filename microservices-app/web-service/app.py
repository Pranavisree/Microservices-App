from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Pranavi Sree</h1><h2>Roll No: 2022BCD0012</h2><p>I am passionate about software development and microservices architecture.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
