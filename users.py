from flask import Flask, render_template, request


class Student:
    def __init__(self, name, mail):
        self.name = name
        self.mail = mail


    def viewer(self):
        return [self.name, self.mail]


user_list = []

app = Flask(__name__)


@app.route('/')
def index():
    form_list = [user.viewer() for user in user_list]
    return render_template("index.html", form_list=form_list)


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        user_list.append(Student(request.form['username'], request.form['mail']))
        return f"<h1>Successfully added {request.form['username']} </h1> \n <p>E-mail: {request.form['mail']}</p> </p>"
    else:
        return render_template("add_user.html")


if __name__ == "__main__":
    app.run(debug=True)

