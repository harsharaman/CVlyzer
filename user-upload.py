from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def upload_page():
    return render_template('upload-page.html')

if __name__=='__main__':
    app.run(debug=True)