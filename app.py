from flask import Flask, render_template, request
import os

# Pages folder se functions import karein
from pages.qrgen import generate_qr
from pages.pdfaddpass import protect_pdf

app = Flask(__name__)

@app.route('/')
def index():
    # Index page par sabhi tools ki list dikhayenge
    return render_template('index.html')

@app.route('/qrgen', methods=['GET', 'POST'])
def qr_route():
    if request.method == 'POST':
        data = request.form.get('data')
        return generate_qr(data)
    return render_template('qrgen.html')

@app.route('/pdfaddpass', methods=['GET', 'POST'])
def pdf_route():
    if request.method == 'POST':
        # Yahan aapka PDF logic chalega
        return protect_pdf()
    return render_template('pdfaddpass.html')

if __name__ == '__main__':
    app.run(debug=True)
