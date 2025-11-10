from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title='Home page')


@app.route('/error')
def error404():
    return render_template('404.html', title='Error 404')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/blog')
def blog():
    return render_template('blog.html', title='Blog')


@app.route('/contact')
def contact():
    return render_template('contact.html', title='contact')


@app.route('/price')
def price():
    return render_template('price.html', title='Price')


@app.route('/project')
def project():
    return render_template('project.html', title='Project')


@app.route('/service')
def service():
    return render_template('service.html', title='Service')


@app.route('/team')
def team():
    return render_template('team.html', title='Team')


@app.route('/testiminial')
def testiminial():
    return render_template('testimonial.html', title='Testiminial')


if __name__ == '__main__':
    app.run(debug=True)