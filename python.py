from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
  mensaje='''
  <ol>
  <h1>Bienvenido a la calculadora de python</h1>
  <li>para Sumar escribe en el navegador 127.0.0.0.5000/sumar/10/20</li>
  <li>para Restar escribe en el navegador 127.0.0.0.5000/sumar/10/20</li>
  <li>para Multiplicar escribe en el navegador 127.0.0.0.5000/sumar/10/20</li>
  <li>para Dividir escribe en el navegador 127.0.0.0.5000/sumar/10/20</li>
  <li>para saber el numero Mayor escribe en el navegador 127.0.0.0.5000/sumar/10/20</li>
  <li>para saber el numero Menor escribe en el navegador 127.0.0.0.5000/sumar/10/20</li>
</ol>
'''
  return mensaje
  
@app.route('/sumar/<v1>/<v2>')
def factorial(v1):
  fact=1
  for x in range(1,int(v1)+1):
    fact*=x
    return (fact("el factorial de {v1}! es {fact}"))
  
@app.route('/Restar/<v1>/<v2>')
def factorial(v1):
  fact=1
  for x in range(1,int(v1)+1):
    fact*=x
    return (fact("el factorial de {v1}! es {fact}"))

@app.route('/Mult/<v1>')
def factorial(v1):
  fact=1
  for x in range(1,int(v1)+1):
    fact*=x
    return (fact("el factorial de {v1}! es {fact}"))
 
  @app.route('/Div/<v1>/<v2>')
def div(v1):
  fact=1
  for x in range(1,int(v1)+1):
    fact*=x
    return (fact("el factorial de {v1}! es {fact}"))
  
  

if __name__ == '__main__':
  app.run(debug=True)