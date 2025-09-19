from flask import Flask, render_template

app = Flask(__name__)

# flask funsonene
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/audun')
def audun():
    return render_template('audun.html')

@app.route('/mio')
def mio():
    return render_template('mio.html')

@app.route('/ommeg')
def ommeg():
    return render_template('ommeg.html')

if __name__ == "__main__":
    app.run(debug=True)
