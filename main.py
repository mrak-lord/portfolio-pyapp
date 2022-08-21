from flask import Flask, render_template, request, redirect
import csv


app = Flask(__name__)
print(__name__)


@app.route('/')
def home_page():
    return render_template('index-2.html')


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
