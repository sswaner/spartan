import boto3
import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/policydetail')
def policydetail():
    return render_template('policydetail.html')

@app.route('/self-service')
def self_service():
    return render_template('self_service.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/products/product1')
def product1():
    return render_template('product1.html')

@app.route('/products/product2')
def product2():
    return render_template('product2.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0', threaded=True)
