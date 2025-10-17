import os

from dotenv import load_dotenv
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Books(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True)
    author: Mapped[str] = mapped_column(String(250))
    url: Mapped[str] = mapped_column(String(500), unique=True)
    rating: Mapped[float]


@app.route("/")
def home():
    all_books = db.session.execute(db.select(Books)).scalars().all()
    return render_template("index.html", all_books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        entry = {
            "title": request.form.get("book_name"),
            "author": request.form.get("author"),
            "url": request.form.get("url"),
            "rating": request.form.get("rating"),
        }
        new_book = Books(**entry)
        db.session.add(new_book)
        db.session.commit()

    return render_template("add.html")


@app.route("/edit/<id>", methods=["GET", "POST"])
def edit(id):
    book = db.session.execute(db.select(Books).where(Books.id == id)).scalar()
    if request.method == "POST":
        new_title = request.form.get("title")
        new_author = request.form.get("author")
        new_rating = request.form.get("rating")

        book.title = new_title
        book.author = new_author
        book.rating = new_rating

        db.session.commit()

        all_books = db.session.execute(db.select(Books)).scalars().all()
        return render_template("index.html", all_books=all_books)

    return render_template("edit.html", book=book)


@app.route("/<id>")
def delete(id):
    book = db.session.execute(db.select(Books).where(Books.id == id)).scalar()
    db.session.delete(book)
    db.session.commit()

    all_books = db.session.execute(db.select(Books)).scalars().all()
    return render_template("index.html", all_books=all_books)


if __name__ == "__main__":
    app.run(debug=True)
