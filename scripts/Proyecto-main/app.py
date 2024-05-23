from flask import Flask, render_template, request, redirect, url_for, flash
from grupaldb import initialize_db, add_password, get_password
from grupalcryptography import generate_key, load_key
from cryptography.fernet import Fernet

app = Flask(__name__)
app.secret_key = 'your_secret_key'

initialize_db()
generate_key()
key = load_key()
cipher_suite = Fernet(key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        service = request.form['service']
        password = request.form['password']
        if service and password:
            add_password(service, password, cipher_suite)
            flash('Contraseña añadida con éxito!')
            return redirect(url_for('index'))
        else:
            flash('Por favor, complete todos los campos.')
    return render_template('add_password.html')

@app.route('/get', methods=['GET', 'POST'])
def get():
    if request.method == 'POST':
        service = request.form['service']
        if service:
            password = get_password(service, cipher_suite)
            if password:
                flash(f'La contraseña para {service} es: {password}')
            else:
                flash('Servicio no encontrado.')
        else:
            flash('Por favor, ingrese el nombre del servicio.')
    return render_template('get_password.html')

if __name__ == '__main__':
    app.run(debug=True)
