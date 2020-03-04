from flask import Flask, render_template

app = Flask('__name__')

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/programs/ielts")
def ielts():
    return render_template('ielts.html')

@app.route("/programs/pte")
def pte():
    return render_template('pte.html')

@app.route("/programs/prep")
def prep():
    return render_template('prep.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/blog")
def blog():
    return render_template('blog.html')



if __name__ == '__main__':
    app.run(debug=True)
