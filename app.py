from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST", "db"),
        user="root",
        password=os.environ.get("MYSQL_ROOT_PASSWORD"),
        database=os.environ.get("MYSQL_DATABASE")
    )

@app.route("/")
def home():
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS visits (id INT AUTO_INCREMENT PRIMARY KEY, time TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
        cursor.execute("INSERT INTO visits (time) VALUES (NOW())")
        conn.commit()
        cursor.execute("SELECT COUNT(*) FROM visits")
        count = cursor.fetchone()[0]
        conn.close()
        return f"This page has been visited {count} times!"
    except Exception as e:
        return f"Database error: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
