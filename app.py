from flask import Flask
from Controllers.load_route import bp_data
from Controllers.accident import bp_accident
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'
app.register_blueprint(bp_data)
app.register_blueprint(bp_accident)

if __name__ == '__main__':
    app.run(debug=True)
