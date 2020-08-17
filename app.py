from flask import Flask , render_template ,request ,url_for
from covid19 import getCovid

app = Flask(__name__)


@app.route('/',methods=['POST','GET'])
def index():
    try:
        if request.method =='POST':
            country = request.form['content']
            covid = getCovid(country)
            return render_template('index.html',cases=covid)
        else:
            return render_template('index.html')
    except:
        return render_template('error.html')
    

@app.route('/aboutCovid',methods=['GET'])
def  about():
    return render_template('about.html')

if __name__ =='__main__':
    app.run(debug=True)