from flask import Flask,render_template

FI=Flask(__name__)


@FI.route('/first')
def first():
    return render_template('first.html')




@FI.route('/context')
def context():
    return render_template('context.html',name='venkydare',age=24.5)


if __name__=='__main__':
    FI.run(debug=True)