from flask import Flask, render_template, request
import mysql.connector

# Connect with the MySQL Server
db = mysql.connector.connect(host="ensembldb.ensembl.org",
                              user="anonymous",
                              password="",
                              db="homo_sapiens_core_95_38")

# A cursor object that will execute all the queries that are needed
cur = db.cursor()

# print all the first cell of all the rows
for row in cur.fetchall():
    print(row[0])

db.close()
# Create the app
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        cursor = mysql.connection.cursor("SELECT * FROM ")
        cursor.execute()
        cursor.fetchall()
        cursor.close()
        return f"Done!!"

if __name__ == '__main__':
    app.run(debug=True)
