from flask import Flask,render_template,url_for
app = Flask(__name__)
posts=[
{
    'author':'Barnadip Dey',
    'title':'Blog Post 1',
    'content':'Nice to know my kind',
    'date_posted':'July29,2020'
},
{  'author':'Arijit Pal',
    'title':'Blog Post 2',
    'content':'Just dont overdo it',
    'date_posted':'July29,2020'
}]

@app.route("/")
def hello():
    return "<h1>charactersidha<h1>"
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)
@app.route("/about")
def about():
    return render_template('about.html',title='About')


if __name__=='__main__':
    app.run(debug=True)
