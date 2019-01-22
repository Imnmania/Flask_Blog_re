from flask import Flask, render_template, url_for # render_template is used for rendering other pages/ templates 
app = Flask(__name__)                             # url_for is for detecting main.css file

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post Content',
        'date_posted': 'April 20, 2019'
    },
    {
        'author': 'Niloy Biswas',
        'title': 'Blog Post 2',
        'content': 'Second post Content',
        'date_posted': 'April 21, 2019'
    },
    {
        'author': 'Sama Biswas',
        'title': 'Blog Post 3',
        'content': 'Third post Content',
        'date_posted': 'April 22, 2019'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')



if __name__== '__main__':
    app.run(debug=True)