from flask import Flask, render_template, request
from Bio import Entrez
import mysql.connector

# # print all the first cell of all the rows
# for row in cur.fetchall():
#     print(row[0])

# Create the app
app = Flask(__name__)

input = input("Search: ")
Entrez.email = "DO.Gajewska@student.han.nl"
handle = Entrez.esearch(db='pubmed',
                            sort='relevance',
                            retmode='xml',
                            term=input)
results = Entrez.read(handle)

ids = ','.join(results['IdList'])
Entrez.email = 'DO.Gajewska@student.han.nl'
handle = Entrez.efetch(db='pubmed',
                       retmode='xml',
                       id=ids)
results = Entrez.read(handle)
for i, paper in enumerate(results['PubmedArticle']):
    print(paper)
    print("{} {}".format(i + 1,
                          paper['MedlineCitation']['Article']['ArticleTitle'])) #pubdate does not work

# for record in records:
#     for element in record.values():
#         print(element)
        # if (element.lower).find(input) >= 0:
        #     print("hey")
        # if type(element) == list:
        #     for ele in element:
        #         print(ele)
        #         woord = ele.lower()
        #         match = woord.find(input)
        #         if match >= 0:
        #             print("Match")
        # else:
        #     woord = element.lower()
        #     match = woord.find(input)
        #     if match >=0:
        #         print("Match")


handle.close()

# @app.route('/')
# def hello_world():
#     return render_template('base.html')
#
#
# @app.route('/', methods=['GET', 'POST'])
# def home():
#     # Connect with the MySQL Server
#     db = mysql.connector.connect(host="ensembldb.ensembl.org",
#                                  user="anonymous",
#                                  password="",
#                                  db="homo_sapiens_core_95_38")
#     if request.method == 'POST':
#         search = "%"+request.form.get("search", "")+"%"
#         # A cursor object that will execute all the queries that are needed
#         cursor = db.cursor()
#         query = f"SELECT description FROM gene where description like %s"
#         cursor.execute(query, [search])
#         # Fetching everything from the database
#         fetched_curs = cursor.fetchall()
#         # Removing % from the search input
#         search = search.replace("%", "")
#         # Making a new datalist
#         dataset_list = []
#         for element in fetched_curs:
#             if search in element[0]:
#                 new_string = element[0].replace(search, "<b>"+search+"</b>")
#                 dataset_list.append(new_string)
#
#
#         # Closing the cursor
#         cursor.close()
#         db.close()
#         return render_template("base.html", cursor=dataset_list)
#     else:
#         return render_template("base.html", cursor=[" ", " "])
#
# if __name__ == '__main__':
#     app.run(debug=True)
