from flask import Flask, render_template, request, json
from wtforms import Form, StringField, validators, SubmitField, TextAreaField
#from sender import Sender

app = Flask(__name__)


class InputForm(Form):
    python_file = TextAreaField('Python File')

    @app.route('/')
    def index():
        form = InputForm(request.form)
        if request.method == 'POST' and form.validate():
            print("Python File: " + form.python_file.data)
            python_file = form.python_file.data
            # instead of this, do the load balancing
            return render_template('index.html', form=form)
        return render_template('index.html', form=form)

    @app.route('/newJob', methods=['POST'])
    def newJob():
        jobNum = int(request.form['jobNum'])
        send_job_to_picos(jobNum)
        return json.dumps({'status':'OK'})



if __name__ == '__main__':
    app.run(debug=True, host='localhost')
    # Sender.start_listening()


def send_job_to_picos(jobNum):
    # send serial data to ALL pics connected
    # to see which ones are available
    # send the job to one of the available ones
    jobFilename = {1: 'test1.py', 2: 'test2.py', 3: 'test3.py', 4: 'test4.py'}

    print(jobFilename[jobNum])
    #error = Sender.new_job(jobFilename[jobNum])
    # if error != None:
    #     print(error)
