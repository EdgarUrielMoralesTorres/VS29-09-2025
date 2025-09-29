from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "test"

@app.route('/factorial/<v1>')
def factorial(v1):
  f=1
  for x in range(1,6):
    f*=x
  return (f("el factorial de {v1}! es {f}"))

if __name__ == '__main__':
  app.run(debug=True)