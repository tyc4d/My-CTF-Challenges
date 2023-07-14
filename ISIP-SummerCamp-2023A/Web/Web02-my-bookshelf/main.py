from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

books = [
    {
        "id": 1,
        "title": "Book 1",
        "author": "Author 1",
        "cover_image": "https://example.com/book1.jpg"
    },
    {
        "id": 2,
        "title": "Book 2",
        "author": "Author 2",
        "cover_image": "https://example.com/book2.jpg"
    },
    {
        "id": 3,
        "title": "Book 3",
        "author": "Author 3",
        "cover_image": "https://example.com/book3.jpg"
    }
]

@app.route("/api/books", methods=["GET"])
def get_books():
    return jsonify(books)

@app.route("/api/books", methods=["POST"])
def add_book():
    data = request.get_json()
    book = {
        "id": len(books) + 1,
        "title": data["title"],
        "author": data["author"],
        "cover_image": data["cover_image"]
    }
    books.append(book)
    return jsonify(book), 201

if __name__ == "__main__":
    app.run(debug=True)
