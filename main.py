from flask import Flask, render_template
from data import db_session
from data.users import User
from data.jobs import Jobs
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/register')
def register():
    return render_template("register.html", title="Регистрация")


def add_user(surname, name, age, position, speciality, address, email):
    db_sess = db_session.create_session()
    user = User()
    user.surname = surname
    user.name = name
    user.age = age
    user.position = position
    user.speciality = speciality
    user.address = address
    user.email = email
    db_sess.add(user)
    db_sess.commit()


def add_job(team_leader, job, work_size, collaborators, start_date, is_finished):
    db_sess = db_session.create_session()
    jobs = Jobs()
    jobs.team_leader = team_leader
    jobs.job = job
    jobs.work_size = work_size
    jobs.collaborators = collaborators
    jobs.start_date = start_date
    jobs.is_finished = is_finished
    db_sess.add(jobs)
    db_sess.commit()


def adding_user():
    add_user("Scott", "Ridley", 21, "captain", "research engineer", "module_1", "scott_chief@mars.org")
    add_user("West", "Alex", 28, "cook", "spy", "module_2", "no_name@mars.org")
    add_user("Baggins", "Frodo", 51, "traveller", "hobbit", "module_2", "one_ring@mars.org")
    add_user("Potter", "Harry", 18, "cleaner", "wizard", "module_1", "sirius_died@mars.org")


def adding_job():
    add_job(1, "deployment of residential modules 1 and 2", 15, "2, 3", datetime.datetime.now(), False)
    add_job(1, "deployment of residential module 2", 23, "1, 3", datetime.datetime.now(), True)
    add_job(2, "deployment of residential modules 3 and 4", 65, "2, 4", datetime.datetime.now(), True)
    add_job(4, "deployment of residential modules 1 and 3", 37, "1, 2", datetime.datetime.now(), False)


def main():
    global lst
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()
    lst = []
    dct = {}
    for user in db_sess.query(User).all():
        dct[user.id] = [user.name, user.surname]
    for job in db_sess.query(Jobs).all():
        lst.append([job.job, ' '.join(dct[job.team_leader]), job.work_size, job.collaborators, job.is_finished])
    app.run()


if __name__ == '__main__':
    main()
