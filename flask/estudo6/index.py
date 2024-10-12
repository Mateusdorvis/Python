from flask import Flask, request, render_template

app = Flask(__name__, template_folder='template')
@app.route('/',)
def pegar():
    return render_template('index.html', msg='Eu amo python')
    
  
app.run(debug=True)