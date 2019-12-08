from flask import Flask,render_template
app=Flask(__name__)
@app.route('/shaker/<int:marks>')
def hello(marks):
    return render_template('index.html',marks=marks)
if __name__=='__main__':
    app.run()