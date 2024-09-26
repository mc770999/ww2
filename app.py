

from controller.target import targets_blueprint

from flask import Flask



app = Flask(__name__)

if __name__ == "__main__":

    app.register_blueprint(targets_blueprint, url_prefix="/api/targets")

    app.run(debug=True)

