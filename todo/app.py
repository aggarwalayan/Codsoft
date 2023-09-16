from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.app_context().push()

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


@app.route('/')
def index():
    todo_list = Todo.query.all()
    print(todo_list)
    return render_template("home.html", todo_list = todo_list)

@app.route("/add", methods=["POST"])
def add(todo_id):
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/change_status/<int:todo_id>")
def change_status(todo_id):
    todo_item = Todo.query.filter_by(id=todo_id).first()
    todo_item.complete = not todo_item.complete
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo_item = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo_item)
    db.session.commit()
    return redirect(url_for("index"))

@app.route('/about')
def about():
    return render_template("about.html")

#to start the server by running app.py
if __name__ == "__main__":

    db.create_all()
    app.run(debug=True)