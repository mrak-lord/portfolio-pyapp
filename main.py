from flask import Flask, render_template, request, redirect
import csv


app = Flask(__name__)
print(__name__)


user_json = {
  "name": "Martin Bachvarov",
  "jobTitle": "QA Master Engineer",
  "bio": "Lorem...",
  "from": "Bulgaria",
  "lives": "United Kingdom",
  "bornIn": "1988",
  "gender": "M",
  "skills": {
    "colOne": [
      {
        "name": "JavaScript",
        "progress": "45%"
      },
      {
        "name": "PHP",
        "progress": "24%"
      },
      {
        "name": "Python",
        "progress": "50%"
      },
      {
        "name": "JAVA",
        "progress": "79%"
      },
      {
        "name": "ReactJS",
        "progress": "36%"
      },
      {
        "name": "Figma",
        "progress": "69%"
      }
    ]
  },
  "education": [
    {
      "year": "2016",
      "degree": "ISTQB foundation level certificate",
      "school": "UDEMY",
      "text": "Lorem..."
    },
    {
      "year": "2013",
      "degree": "Physiotherapy bachelor degree",
      "school": "Medical University of Sofia, Bulgaria",
      "text": "Lorem..."
    },
    {
      "year": "2007",
      "degree": "High-School diploma",
      "school": "Jordan Jovkov high school of Tutrakan",
      "text": "Lorem..."
    }
  ],
  "experience": [
    {
      "year": "2019 - Current",
      "title": "QA: Rank Automation Engineer",
      "company": "Tandem Bank",
      "text": "Lorem..."
    },
    {
      "year": "2017",
      "title": "QA: Rank Manual Tester",
      "company": "ZIBID Ltd",
      "text": "Lorem ..."
    }

  ]
}



@app.route('/')
def home_page():
    return render_template('index-2.html', name=user_json['name'], jobTitle=user_json['jobTitle'], education=user_json['education'], experience=user_json['experience'], skills=user_json['skills'], bio=user_json['bio'], origin=user_json['from'], lives=user_json['lives'], bornIn=user_json['bornIn'], gender=user_json['gender'])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_db(data)
        return redirect('/thankyou')
    else:
        return 'something went wrong!'


def write_to_db(data):
    with open('database.csv', mode='a') as database:
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(data.values())


@app.route('/thankyou')
def thank_you():
    return render_template('thankyou.html')
