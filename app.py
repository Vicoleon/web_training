from flask import Flask,render_template

app= Flask(__name__)

jobs = [
    {
        'id': 1,
        'title': 'Software Engineer',
        'location': 'San Francisco, CA',
        'salary': 120000
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'New York, NY',
        'salary': 110000
    },
    {
        'id': 3,
        'title': 'Product Manager',
        'location': 'Boston, MA',
        'salary': 130000
    },
    {
        'id': 4,
        'title': 'UI/UX Designer',
        'location': 'Austin, TX',
        'salary': 90000
    },
    {
        'id': 5,
        'title': 'DevOps Engineer',
        'location': 'Seattle, WA',
        'salary': 115000
    }
]


@app.route("/")
def hello_world():
    return render_template("home.html",jobs=jobs)

if __name__=="__main__":
  app.run(host='0.0.0.0', debug=True, port=81)

