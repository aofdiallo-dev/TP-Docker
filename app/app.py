
from flask import Flask
import os
import psycopg2

app = Flask(__name__)


@app.route("/")
def home():
    return "Bonjour depuis Docker !"


@app.route("/info")
def info():
    return {
        "application": "Docker DevOps Project",
        "environment": os.getenv("APP_ENV", "development")
    }


@app.route("/db")
def database():
    try:
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )

        connection.close()

        return "Connexion PostgreSQL : OK"

    except Exception as error:
        return f"Erreur PostgreSQL : {error}", 500


app.run(host="0.0.0.0", port=3000)

