from flask import Flask, render_template, request

app = Flask(__name__)

# Mock function for recommendations
def recommend_songs(book_name):
    # Replace this with your model logic
    return [
        {"Song Title": "Song 1", "Artist": "Artist 1"},
        {"Song Title": "Song 2", "Artist": "Artist 2"},
        {"Song Title": "Song 3", "Artist": "Artist 3"},
    ]

@app.route('/', methods=['GET', 'POST'])
def index():
    songs = []
    book_name = ''
    if request.method == 'POST':
        book_name = request.form['book_name']
        songs = recommend_songs(book_name)
    return render_template('index.html', book_name=book_name, songs=songs)

if __name__ == '__main__':
    app.run(debug=True)
