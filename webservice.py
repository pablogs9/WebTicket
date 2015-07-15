import sys
from flask import Flask,request,render_template
from werkzeug import secure_filename
from ticketPreview import ticketPreview

app = Flask('WebTickets')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['pic']
        try:
            size = int(request.form['size'])
            if size not in [4,10,25]:
                size = 10
        except:
            size = 10

        originalfilename = secure_filename(f.filename)

        with open('filecount.txt','r') as fc:
            countfilename = int(fc.read())
        with open('filecount.txt','w') as fc:
            fc.write(str(countfilename+1))

        filename = str(countfilename) + '-' + originalfilename
        f.save('uploads/' + filename)
        ticketPreview(filename,size)
        return '/static/images/{0}'.format(filename.split('.')[0] + ".jpg")

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/howdoesitlook")
def howdoesitlook():
    return render_template('app.html')

@app.route("/howdoesitreallylook")
def howdoesitreallylook():
    return render_template('samples.html')

if __name__ == "__main__":
    try:
        app.run(host=sys.argv[1], port=int(sys.argv[2]),debug=True)
    except:
        app.run(host="0.0.0.0", port=8000, debug=True)
