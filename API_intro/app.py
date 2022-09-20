from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)


# from flask import Flask, render_template
# app = Flask (__name__)
# @app.route('/')
# def index():
#     return render_template('index.html')

# if __name__ == "__main__":
#     app.run(debug=True)


# from flask import Flask, render_template, url_for
# from flask_sqlalchemy import SQLAlchemy
#from datetime import datetime

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
#db = SQLAlchemy(app)
#class ToDo(db.Model):
    #id = db.Column(db.integer, primary_key = True)
    #content = db.Column(db.String(200), nullable = False)
    #completed = db.Column(db.Integer, default = 0)
    #date_created = db.Column(db,DateTime, default=datetime.utcnow)

    #def __repr__(self):
    #return '<Task %r>' % self.id

# app = Flask (__name__)
# @app.route('/')
# def index():
#     return render_template('index.html')

# if __name__ == "__main__":
#     app.run(debug=True)


