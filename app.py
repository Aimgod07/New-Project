from flask import Flask, render_template

app = Flask(__name__)

JOBS=[{
  'id': 1,
  'title': "Frontend developer",
  'Salary': "Rs150000",
  'location':'Delhi,India'
    },
      {'id': 2,
  'title': "Backend developer",
  'Salary': "Rs160000",
  'location':'Banglore,India'},
     {'id': 3,
  'title': "Data Analyst",
  'Salary': "Rs120000",
  'location':'Chennai,India'}]

@app.route("/")
def hello_world():
  return render_template('home.html', Jobs =JOBS)

if __name__=="__main__":
  app.run(host='0.0.0.0', debug=True)