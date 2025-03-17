import time
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flaskuser:flaskpassword@db/flaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Retry mechanism for database connection
def initialize_db():
    retries = 5
    delay = 5  # seconds
    while retries > 0:
        try:
            # Use the application context
            with app.app_context():
                db.create_all()
                print("Database connected successfully!")
                return
        except pymysql.err.OperationalError as e:
            print(f"Database connection failed: {e}. Retrying in {delay} seconds...")
            retries -= 1
            time.sleep(delay)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break
    print("Failed to connect to the database after multiple retries.")

# Call the initialize_db function when the app starts
initialize_db()

from app import routes
