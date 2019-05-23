from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return 'Hello'

@app.route("/about")
def about():
    return "<h1>heading<h1>"

if __name__=='__main__':
    main()
