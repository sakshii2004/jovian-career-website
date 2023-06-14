from flask import Flask, render_template
from database import jobs_from_db

app = Flask(__name__)

@app.route("/")
def hello_world():
  JOBS = jobs_from_db()
  return render_template('home.html', jobs=JOBS)

if __name__=='__main__':
  app.run(host='0.0.0.0', debug=True)

 