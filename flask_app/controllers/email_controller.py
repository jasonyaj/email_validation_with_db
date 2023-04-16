from flask import session, render_template, request, redirect
from flask_app import app, EMAIL_REGEX
from flask_app.models.email_model import Email

# landing page includes email input
@app.route('/')
def get_email():
    return render_template('index.html')

# page used to collect, validate and transfer email
@app.route('/process', methods=['POST'])
def process_email():
    print(request.form)
    email_entry = {
        'email': request.form['email']
    }
    if Email.validate_email(email_entry) == False:
        return redirect('/')
    else:
        new_email = Email.add_email(email_entry)
        session['email'] = request.form['email']
        return redirect('/emails')

# displays all the emails and a successful new email entry message
@app.route('/emails')
def display_emails():
    data = {}
    list_of_emails = Email.get_all_emails(data)
    return render_template('emails.html', list_of_emails=list_of_emails)
