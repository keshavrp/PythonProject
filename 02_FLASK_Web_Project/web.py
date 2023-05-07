'''Web Server using the Python mini framework FLASK'''
import csv
from flask import Flask,render_template,request

app=Flask(__name__)
'''The application name is app'''

@app.route("/")
def home_page():
    '''This function will give the home page of the website '''
    return render_template('index.html')

@app.route('/<string:page_name>')
def page(page_name):
    '''This function will give the different pages'''
    return render_template(page_name)

def database(data):
    '''It creates a databse csv file in which the name,email and message are stored'''
    name=data['name']
    email=data['email']
    message=data['message']

    with open('data_base.csv', mode='a',encoding='utf8') as data_base:
        csv_writer=csv.writer(data_base, quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    '''This function will make the form functional'''
    if request.method=='POST':
        data=request.form.to_dict()
        #.to_dict() stores the data in the dictionary
        database(data)
        return render_template('thankyou.html')
    else:
        return 'Something went wrong.'
    