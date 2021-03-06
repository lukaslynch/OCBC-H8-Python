# from flask import (
#     Flask,
#     render_template
# )

# # Create the application instance
# app = Flask(__name__, template_folder="templates")

# # Create a URL route in our application for "/"
# @app.route('/')
# def home():
#     """
#     This function just responds to the browser ULR
#     localhost:5000/

#     :return:        the rendered template 'home.html'
#     """
#     return render_template('home.html')

# # If we're running in stand alone mode, run the application
# if __name__ == '__main__':
#     app.run(debug=True)

########################### SWAGGER !!!!!!!!!!!!!!!!!

# from flask import render_template
# import connexion

# # Create the application instance
# app = connexion.App(__name__, specification_dir='./')

# # Read the swagger.yml file to configure the endpoints
# app.add_api('swagger.yml')

# # Create a URL route in our application for "/"
# @app.route('/')
# def home():
#     """
#     This function just responds to the browser ULR
#     localhost:5000/
#     :return:        the rendered template 'home.html'
#     """
#     return render_template('home.html')

# # If we're running in stand alone mode, run the application
# if __name__ == '__main__':
#     app.run(host='localhost', port=5000, debug=True)

################ LUKAS
"""
Main module of the server file
"""

# 3rd party moudles
from flask import render_template

# local modules
import config


# Get the application instance
connex_app = config.connex_app

# Read the swagger.yml file to configure the endpoints
connex_app.add_api("swagger.yml")


# create a URL route in our application for "/"
@connex_app.route("/")
def home():
    """
    This function just responds to the browser URL
    localhost:5000/
    :return:        the rendered template "home.html"
    """
    return render_template("home.html")


if __name__ == "__main__":
    connex_app.run(host='localhost', port=5000, debug=True)