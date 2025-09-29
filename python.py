app = Flask(__name__)

@app.route('/')
def home():
    mensaje= "test"
    return mensaje

@app.route('/factorial')
def factorial(v1):
  f=1
    
if __name__ == '__main__':
  app.run(debug=True)