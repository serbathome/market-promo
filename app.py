from flask import Flask, request, redirect, render_template
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', {})


@app.route('/sendmail', methods=['POST'])
def sendmail():
    sg = sendgrid.SendGridAPIClient(
        api_key=os.environ['SGKEY'])
    from_email = Email("bot@fedtech.ca")
    to_email = To("sales@fedtech.ca")
    subject = "New lead for Farm Market portal"
    content = Content(
        "text/plain", f"Please reach out to {request.form['email']}, he/she is willing to know more.")
    mail = Mail(from_email, to_email, subject, content)

    # Get a JSON-ready representation of the Mail object
    mail_json = mail.get()

    # Send an HTTP POST request to /mail/send
    sg.client.mail.send.post(request_body=mail_json)

    return redirect('https://market.devs.bz', code=302, Response=None)
