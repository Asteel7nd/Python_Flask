from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/gallery")
def gallery():
    return render_template('gallery.html')

@app.route("/news")
def news():
    return render_template('news.html')

@app.route("/projects")
def projects():
    return render_template('projects.html')

if __name__ == '__main__':
    app.run(debug=True)
