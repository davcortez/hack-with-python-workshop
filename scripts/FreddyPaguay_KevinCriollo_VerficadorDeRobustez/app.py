from flask import Flask, request, jsonify, render_template
import re

app = Flask(__name__)

def verificar_contrasena(contrasena):
    if len(contrasena) < 8:
        return "La contraseña debe tener al menos 8 caracteres."
    if not re.search("[a-z]", contrasena) or not re.search("[A-Z]", contrasena):
        return "La contraseña debe contener al menos una letra mayúscula y una minúscula."
    if not re.search("[0-9]", contrasena):
        return "La contraseña debe contener al menos un número."
    if not re.search("[!@#$%^&*()_+-=]", contrasena):
        return "La contraseña debe contener al menos un carácter especial."
    return "La contraseña es lo suficientemente robusta."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/verificar', methods=['POST'])
def verificar():
    data = request.get_json()
    contrasena = data['password']
    resultado = verificar_contrasena(contrasena)
    return jsonify({"result": resultado})

if __name__ == '__main__':
    app.run(debug=True)
