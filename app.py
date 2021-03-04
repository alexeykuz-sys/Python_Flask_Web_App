import  os
from flask import Flask


if os.path.exist("env.py"):
    import env


app = Flask(__name__)

@app.route("/")
def hello():
    return "dfdfgfghg"


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)