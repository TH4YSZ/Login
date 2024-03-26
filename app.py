from flask import Flask, request , render_template
import mysql.connector

app = Flask(__name__)

conexao = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="login"
)

cursor = conexao.cursor()

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/login", methods=['POST'])
def login():
    data = request.json  

    email = data.get('email')  
    senha = data.get('senha') 

    cursor.execute("SELECT email, senha FROM usuarios")
    resultados = cursor.fetchall()
    
    for resultado in resultados:
        if email == resultado[0] and senha == resultado[1]:
            return "Login bem-sucedido :)"
        
    cursor.close()
    conexao.close()

    return "Credenciais inválidas"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
