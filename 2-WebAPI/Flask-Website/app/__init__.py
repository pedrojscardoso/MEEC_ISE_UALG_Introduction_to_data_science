"""
Application Initialization and Routing Configuration.
Here we create the Flask app instance and import the desired routing file.

By uncommenting different 'routes' imports below, you can change the 
behavior of the website to demonstrate different Flask features.
"""
from flask import Flask

app = Flask(__name__)

# To test different examples, uncomment EXACTLY ONE of the imports below:
from app import routes      # 1. Simple text response
# from app import routes2   # 2. Hardcoded HTML string response
# from app import routes3   # 3. Using render_template (Jinja2) with variables
# from app import routes4   # 4. Passing a list of dictionaries to templates
# from app import routes5   # 5. Advanced template rendering example
