import sys
from flask import Flask,request,render_template
from werkzeug import secure_filename
from ticketPreview import ticketPreview

app = Flask('WebTickets')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['pic']
        size = int(request.form['size'])

        originalfilename = secure_filename(f.filename)

        with open('filecount.txt','r') as fc:
            countfilename = int(fc.read())
        with open('filecount.txt','w') as fc:
            fc.write(str(countfilename+1))

        filename = str(countfilename) + '-' + originalfilename
        f.save('uploads/' + filename)
        ticketPreview(filename,size)
        return '<meta http-equiv="refresh" content="0; url=static/images/{0}" />'.format(filename)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        try:
            app.run(host=sys.argv[1], port=int(sys.argv[2]),debug=True)
        except:
            print "Usage: python webservice.py [IP] [Port]"
    else:
        app.run(host="0.0.0.0", port=8000, debug=True)
