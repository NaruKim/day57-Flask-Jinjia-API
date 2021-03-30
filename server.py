from flask import Flask, render_template
import random
import datetime
import requests

AGE = "https://api.agify.io"
GENDER = "https://api.genderize.io"
BLOG = "https://api.npoint.io/5abcca6f4e39b4955965"

app = Flask(__name__)

@app.route('/')
def home():
    this_year = datetime.datetime.now().year
    random_number = random.randint(1,10)
    return render_template('index.html', num=random_number, year=this_year)

@app.route('/guess/<n>')
def guess(n):
    parameters = {'name':n}
    response = requests.get(AGE, params=parameters)
    response2 = requests.get(GENDER, params=parameters)
    return render_template('age.html', data=response.json(), data2=response2.json())

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    response = requests.get(BLOG)
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)