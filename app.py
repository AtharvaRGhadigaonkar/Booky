from flask import Flask,render_template,request
import numpy as np,pickle
pt = pickle.load(open("pt.pkl",'rb'))
score = pickle.load(open("score.pkl",'rb'))
Books = pickle.load(open("Books.pkl",'rb'))
pop = pickle.load(open("pop.pkl",'rb'))



app=Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/leaderboard")
def leaderboard():
    return render_template("top50.html",
                           bookname=list(pop["Book-Title"].values),
                           bookauthor=list(pop["Book-Author"].values),
                           bookyear=list(pop["Year-Of-Publication"].values),
                           bookpublisher=list(pop["Publisher"].values),
                           bookrating=list(np.round(pop["Rating-Mean"].values)),
                           bookvotes=list(pop["Rating-Count"].values),
                           bookimg=list(pop["Image-URL-L"].values)
                           )

@app.route("/recommend_books", methods=["POST"])
def recommend_books():
    user_input = request.form.get("userinput")

    try:
        index = np.where(pt.index == user_input)[0][0]
    except IndexError:
        return render_template("colab.html", book_list=list(pt.index), error="Book not found. Please select from the list.")

    distance = score[index]
    items = sorted(list(enumerate(distance)), key=lambda x: x[1], reverse=True)[1:13]
    data = []
    for x in items:
        item = []
        a = Books[Books["Book-Title"] == pt.index[x[0]]]
        a.drop_duplicates("Book-Title", inplace=True)
        item.extend(list(a["Book-Title"].drop_duplicates()))
        item.extend(list(a["Book-Author"].drop_duplicates()))
        item.extend(list(a["Year-Of-Publication"].drop_duplicates()))
        item.extend(list(a["Publisher"].drop_duplicates()))
        item.extend(list(a["Image-URL-L"].drop_duplicates()))
        data.append(item)
    return render_template("colab.html", data=data, book_list=list(pt.index))

@app.route("/recommend")
def recommend():
    return render_template("colab.html",book_list=list(pt.index))


if __name__ == '__main__':
    app.run(debug=True)

