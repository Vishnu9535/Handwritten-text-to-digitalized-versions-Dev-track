from flask import Flask
from flask import request
from flask import render_template
import output_model

app = Flask(__name__)
@app.route("/test", methods=['POST','GET'])
def test_page():
  if request.method == "POST":
    image = request.files.get('img', '')
    image = request.form["img"]
    image=output_model.input_image(image)
    print("img ",image)
    return "<h1> uploaded </h1>"
  else:
    return render_template('index.html')
  
