from flask import Flask, render_template, request
app = Flask(__name__, static_folder='static')
arr=[]
@app.route('/', methods=['get', 'post'])
def home():
	if request.method=='POST':
		arr.append(request.form['link'])
		print request.form['link']
	return render_template('home.html', arr=arr)


app.run(debug=True)
