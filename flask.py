from flask import Flask

# Create a Flask app
app = Flask(__name__)

# Define a route and a function to handle requests
@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/kishore')
def kishore():
    return "Hello, kishore"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
