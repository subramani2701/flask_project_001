from flask import Flask,redirect, render_template,url_for,request


app = Flask(__name__)

@app.route('/hello')

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

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('results.html', result = dict)


if __name__ == '__main__':
   app.run(debug=True)