from flask import Flask, make_response,redirect, render_template,url_for,request


app = Flask(__name__)


# @app.route('/login',methods = ['POST', 'GET'])
# def login():
#    if request.method == 'POST':
#       user = request.form['nm']
#       return redirect(url_for('success',name = user))
#    else:
#       user = request.args.get('nm')
#       return redirect(url_for('success',name = user))
   
@app.route('/hello/<user>')
def hello_name(user):
   return render_template('hello.html',name=user)

@app.route('/marks')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('marks.html', result = dict)


@app.route("/")
def index():
   return render_template("index_one.html")

# @app.route('/')
# def student():
#    return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def new_result():
   if request.method == 'POST':
      result = request.form
      return render_template("new_results.html",result = result)
   
@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST':
      user = request.form['nm']
   
   resp = make_response(render_template('readcookie.html'))
   resp.set_cookie('userID', user)
   
   return resp

@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return '<h1>welcome '+name+'</h1>'


if __name__ == '__main__':
   app.run(debug=True)