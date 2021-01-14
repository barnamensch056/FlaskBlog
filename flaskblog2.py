from flask import Flask,render_template,url_for,flash,redirect
from forms import RegistrationForm,LoginForm
app = Flask(__name__)

app.config['SECRET_KEY']='a7c722cb787c25547e48a923df3df99b'
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
@app.route("/register",methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash('Account created for {}!'.format(form.username.data),'success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register Soon',form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'barnamensch056' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html',title='Login',form=form)

if __name__=='__main__':
    app.run(debug=True)
