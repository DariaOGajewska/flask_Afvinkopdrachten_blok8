from flask import Flask, render_template, request
import mysql.connector

# # print all the first cell of all the rows
# for row in cur.fetchall():
#     print(row[0])

# Create the app
app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return render_template('base.html')


@app.route('/', methods=['GET', 'POST'])
def home():
    # Connect with the MySQL Server
    db = mysql.connector.connect(host="ensembldb.ensembl.org",
                                 user="anonymous",
                                 password="",
                                 db="homo_sapiens_core_95_38")
    if request.method == 'POST':
        search = "%"+request.form.get("search", "")+"%"
        # A cursor object that will execute all the queries that are needed
        cursor = db.cursor()
        query = f"SELECT description FROM gene where description like %s"
        cursor.execute(query, [search])
        # Fetching everything from the database
        fetched_curs = cursor.fetchall()
        # Removing % from the search input
        search = search.replace("%", "")
        # Making a new datalist
        dataset_list = []
        for element in fetched_curs:
            if search in element[0]:
                new_string = element[0].replace(search, "<b>"+search+"</b>")
                dataset_list.append(new_string)


        # Closing the cursor
        cursor.close()
        db.close()
        return render_template("base.html", cursor=dataset_list)
    else:
        return render_template("base.html", cursor=[" ", " "])

if __name__ == '__main__':
    app.run(debug=True)
