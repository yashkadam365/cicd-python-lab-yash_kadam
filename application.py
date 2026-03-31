from flask import Flask

application = Flask(__name__)
@application.route('/')

def hello_world():
  return "<h1>CI/CD Pipeline is Live!</h1><p>Version 2.0 🚀</p>"
if __name__ == '__main__':
  application.run(debug=True)
