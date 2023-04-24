from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/') 
def benvenuto():
  return render_template("formPost.html")

@app.route('/controlla') 
def controlla():
  return "pagina di controllo"

@app.route('/login' , methods = ['POST']) #Post nasconde i parametri nella barra di ricerca mentre con get li vediamo 
def login():
  nome = request.form['nome']
  cognome = request.form['cognome']
  sesso = request.form['sesso']
  nomeUtente = request.form['nomeUtente']
  if nome == 'admin' and cognome == 'xxx123##': 
    if sesso == 'Maschio':
     return render_template('login.html' , saluto = 'Benvenuto' , nome = nome , cognome = cognome) 
    else:
        return render_template('login.html' , saluto = 'Benvenuta' , nome = nome , cognome = cognome) 
  else: 
    return render_template('errorePassword.html') 

    if sesso == 'Maschio': 
        return render_template('formPost.html', sesso = sesso)
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)