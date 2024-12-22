from flask import Flask, render_template, request, redirect, url_for
import database

application = Flask(__name__)

# Initialize database
database.init_db()

@application.route('/')
def ma():
    return render_template('index.html')

@application.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    num = request.form['num']
    database.save(name, num)
    return render_template('main.html')

@application.route('/list')
def list():
    students = database.get_all_students()
    return render_template('list.html', stu=students)

@application.route('/password')
def password():
    return render_template('password.html')
@application.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    print(f"삭제 요청 ID: {id}")  # 디버깅
    database.delete_student(id)
    print("삭제 완료")
    return redirect(url_for('admit'))


@application.route('/admit')
def admit():
    students = database.get_all_students()
    return render_template('admit.html', stu=students)


@application.route('/passwordcheck', methods=['POST'])
def passwordcheck():
    password = request.form['pass']
    if password == "1234":
        return render_template('main.html')
if __name__ == '__main__':
    application.run(host='0.0.0.0',debug=True,port=5500)
