from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/') 
def benvenuto():
  return render_template("InserisciPesoeAltezza.html")

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


@app.route('/IMC') 
def indiceMassaCorporea():
    pesoUtente = float(request.args.get('peso'))
    altezzaUtente = float(request.args.get('altezza'))
    IMC = pesoUtente / ((altezzaUtente / 100) ** 2)
    if IMC < 20:
        img = "/static/images/pizza.jpg"
        return render_template("IMC.html" , risultato = 'Sei sottopeso!', foto = img)
    elif IMC > 20 and IMC < 30:
        img = "/static/images/pasta.jpg"
        return render_template("IMC.html" , risultato = 'Sei normopeso!', foto = img)
    else: 
        img = "/static/images/verdura.jpg"
        return render_template("IMC.html" , risultato = 'Sei sovrappeso!', foto = img)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)