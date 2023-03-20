from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def products():
    return render_template('index.html')
    # return 'this is products page'

@app.route('/products')
def hello_world():
    return "<p>Hthis is product page!</p>"

if __name__=="__main__":
    app.run(debug=True)
   