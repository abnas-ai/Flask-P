
# app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask! 🎉'

@app.route('/blog')
def blog():
    return 'This is the blog'

@app.route('/blog/<int:blog_id>')
def blogpost(blog_id):
    return 'This is blog number' + str(blog_id)

if __name__ == '__main__':
    app.run(debug=True)
# To run the Flask app, use the command:
# python app.py
# Make sure to install Flask first:
# pip3 install Flask
# This code sets up a simple Flask web application that returns "Hello, Flask! 🎉" when accessed at the root URL.
# This is a basic Flask application that serves a simple "Hello, Flask!" message.


