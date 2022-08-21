from flask import Flask, render_template, request, redirect
import csv
import json


app = Flask(__name__)
print(__name__)

with open('/home/martin-bachvarov/scool/repos/portfolio-pyapp/profile_data.json', mode='r') as user:
    user_json = json.load(user)



@app.route('/')
def home_page():
    yo = render_template('test.html')
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
