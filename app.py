from flask import Flask


app = Flask(__name__)

from structures.views import index

if __name__ == 'main':
    app.run(debug=True)
