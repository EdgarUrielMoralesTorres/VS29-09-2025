from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
  mensaje='''
  <ol>
  <h1>Bienvenido a la calculadora de python</h1>
  <li>para Sumar escribe en el navegador 127.0.0.0.5000/sumar/valor 1/valor 2</li>
  <li>para Restar escribe en el navegador 127.0.0.0.5000/Restar/valor 1/valor 2</li>
  <li>para Multiplicar escribe en el navegador 127.0.0.0.5000/Mult/valor 1/valor 2</li>
  <li>para Dividir escribe en el navegador 127.0.0.0.5000/Div/valor 1/valor 2</li>
  <li>para saber el numero Mayor escribe en el navegador 127.0.0.0.5000/NumMax/valor 1/valor 2</li>
  <li>para saber el numero Menor escribe en el navegador 127.0.0.0.5000/NumMin/valor 1/valor 2</li>
  
  <footer><br>
  <h1>Edgar Uriel Morales Torres 
  5-D</h1></footer>
</ol>
'''
  return mensaje
  
@app.route('/sumar/<int:s1>/<int:s2>')
def sumar(s1,s2):
  resultado=s1+s2
  return (f"La suma de los numeros {s1} y {s2} es {resultado}")
  
@app.route('/Restar/<int:r1>/<int:r2>')
def Res(r1,r2):
    resultadoRes=r1-r2
    return (f"La resta de los numeros {r1} y {r2} es {resultadoRes}")

@app.route('/Mult/<int:m1>/<int:m2>')
def Mult(m1,m2):
    resultadosMul=m1*m2
    return (f"Las multiplicaciones de los numeros {m1} y {m2} es {resultadosMul}")

@app.route('/Div/<int:d1>/<int:d2>')
def Div(d1,d2):
    resultadosDiv=d1/d2
    return (f"la divicion de los numeros {d1} y {d2} es {resultadosDiv}")
  
@app.route('/NumMin/<int:e1>/<int:e2>')
def NumMin(e1,e2):
    menResul=0
    if(e1>e2):
        menResul=e2
    else:
        if(e2>e1):
         menResul=e1
    return(f"el numero menor de {e1} y {e2} es {menResul}")
    
  
@app.route('/NumMax/<int:a1>/<int:a2>')
def NumMax(a1,a2):
    maxResul=0
    if(a1>a2):
        maxResul=a1
    else:
        if(int(a2)>int(a1)):
         maxResul=a2
    return(f"el numero mayor de {a1} y {a2} es {maxResul}")

if __name__ == '__main__':
  app.run(debug=True)
