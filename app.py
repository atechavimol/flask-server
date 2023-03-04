from flask import Flask, render_template, request
from wtforms import Form, StringField, validators, SubmitField, TextAreaField
from Sender import Sender

app = Flask(__name__)


class InputForm(Form):
    python_file = TextAreaField('Python File')

    @app.route('/', methods=['GET', 'POST'])
    def index():
        form = InputForm(request.form)
        if request.method == 'POST' and form.validate():
            print("Python File: " + form.python_file.data)
            python_file = form.python_file.data
            # instead of this, do the load balancing
            return render_template('index.html', form=form)
        return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, host='localhost')
    # Sender.start_listening()


def send_job_to_picos(job):
    # send serial data to ALL pics connected
    # to see which ones are available
    # send the job to one of the available ones
    error = Sender.new_job(job)
    if error != None:
        print(error)
