from sample import DynamicValue
from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def index():
    return render_templates('index.html')

@app.route('/click')
def click():
    pass

if __name__=="__main__":
    dynamicweb=DynamicValue()
    app.run(debug=True)
