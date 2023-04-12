from flask import Flask
import mysql.connector

# Connect with the MySQL Server
cnx = mysql.connector.connect(host="ensembldb.ensembl.org",
                              user="anonymous",
                              password="",
                              db="homo_sapiens_core_95_38")
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
