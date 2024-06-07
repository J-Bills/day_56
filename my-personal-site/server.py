from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    #return '<h1>Hello World<h1/>'
    
    #returning the html template that we created
    return render_template('index.html')

@app.route('/angela')
def angela():    
    #returning the html template that we created
    return render_template('angela.html')

if __name__ == '__main__':
    app.run(debug=True)