from flask import Flask, request, render_template, redirect, url_for, flash
from twilio.rest import Client
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Twilio credentials
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
twilio_phone_number = 'your_twilio_phone_number'

client = Client(account_sid, auth_token)

def generate_otp():
    return str(random.randint(100000, 999999))

otp_dict = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-otp', methods=['POST'])
def send_otp():
    phone_number = request.form['phone']
    otp = generate_otp()
    otp_dict[phone_number] = otp
    message = client.messages.create(
        body=f'Your OTP is {otp}',
        from_=twilio_phone_number,
        to=phone_number
    )
    flash('OTP sent to your phone number.')
    return redirect(url_for('verify', phone=phone_number))

@app.route('/verify')
def verify():
    phone_number = request.args.get('phone')
    return render_template('verify.html', phone_number=phone_number)

@app.route('/verify-otp', methods=['POST'])
def verify_otp():
    phone_number = request.form['phone']
    otp = request.form['otp']
    if otp_dict.get(phone_number) == otp:
        flash('OTP verified successfully!')
        return redirect(url_for('index'))
    else:
        flash('Invalid OTP. Please try again.')
        return redirect(url_for('verify', phone=phone_number))

if __name__ == '__main__':
    app.run(debug=True)
