from flask import Flask, render_template_string


app = Flask(__name__)

@app.route('/')
def html():
    html5 = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Site simples</title>
</head>
<body>
    <h1>Olá mundo !</h1>
</body>
</html>
'''
    return render_template_string(html5)

app.run(debug=True)