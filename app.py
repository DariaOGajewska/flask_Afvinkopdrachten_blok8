from flask import Flask, render_template, request
import mysql.connector

# Connect with the MySQL Server
db = mysql.connector.connect(host="ensembldb.ensembl.org",
                              user="anonymous",
                              password="",
                              db="homo_sapiens_core_95_38")

# # print all the first cell of all the rows
# for row in cur.fetchall():
#     print(row[0])

# Create the app
app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return render_template('base.html')


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        search = request.form.get("search", "")
        # A cursor object that will execute all the queries that are needed
        cursor = db.cursor()
        # list = cursor.execute("SELECT * FROM homo_sapiens_funcgen_95_38")
        # # Fetching everything from the database
        # for row in cursor.fetchall():
        #     print(row)
        # Closing the cursor
        cursor.close()
        db.close()
        return render_template("base.html", search=search)
    else:
        return render_template("base.html", search="")

if __name__ == '__main__':
    app.run(debug=True)
