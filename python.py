from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
  mensaje='''
  <ol>
  <h1>Bienvenido a la calculadora de python</h1>
  <li>para Sumar escribe en el navegador 127.0.0.0.5000/sumar/10/20</li>
  <li>para Restar escribe en el navegador 127.0.0.0.5000/Restar/10/20</li>
  <li>para Multiplicar escribe en el navegador 127.0.0.0.5000/Mult/10/20</li>
  <li>para Dividir escribe en el navegador 127.0.0.0.5000/Div/10/20</li>
  <li>para saber el numero Mayor escribe en el navegador 127.0.0.0.5000/NumMax/10/20</li>
  <li>para saber el numero Menor escribe en el navegador 127.0.0.0.5000/NumMin/10/20</li>
  <footer>Edgar Uriel Morales Torres</footer>
</ol>
'''
  return mensaje
  
@app.route('/sumar/<s1>/<s2>')
def sum(s1,s2):
  val1=0
  val2=0
  sum=val1+val2
  return (sum("La suma de los numeros{s1} y {s2} es {sum}"))
  
@app.route('/Restar/<r1>/<r2>')
def Res(v1):
    return(Res("La resta de los numeros"))

@app.route('/Mult/<m1>/<m2>')
def Multi(v1):
    return (Multi("Las Multiplicaciones de los numeros"))

@app.route('/Div/<d1>/<d2>')
def div(v1):
  fact=1
  for x in range(1,int(v1)+1):
    fact*=x
    return (fact("el factorial de {v1}! es {fact}"))
  
@app.route('/NumMin/<e1>/<e2>')
def Men(v1):
    return (Men("El Numero menor es"))
  
@app.route('/NumMax/<a1>/<a2>')
def may(v1):
    return (may("el Numero mayor es"))
  

if __name__ == '__main__':
  app.run(debug=True)