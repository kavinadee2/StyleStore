
from flask import Flask, render_template
from db import get_db_connection


app = Flask(__name__)


@app.route("/")
def home():
   connection = get_db_connection()

   cursor = connection.cursor(dictionary=True)
   cursor.execute("SELECT * FROM products")
   products = cursor.fetchall()
   cursor.close()
   connection.close()

   return render_template("index.html", products=products)


if __name__ == "__main__":
    app.run(debug=True)
