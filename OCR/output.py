from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask import Flask, request, render_template
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
from test_handwriting import get_text

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './imgfolder/files'

@app.route('/', methods=['GET',"POST"])
@app.route('/home', methods=['GET',"POST"])
def index():
    output_text="IgotText!"
    if request.method == "POST":
        if request.files:
            file = request.files["image"]
            file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))) 
            filename=os.listdir('./imgfolder/files')
            output_text=get_text('./imgfolder/files/'+filename[-1])
    return render_template('index.html', output_text=output_text)

    # return render_template(pred='{}'.format(output_text))
if __name__=="__main__":
    app.run(debug=True)
