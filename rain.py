from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")

    user = User()
    user.surname = 'Scott'
    user.name = 'Ridley'
    user.age = 21
    user.position = 'captain'
    user.speciality = 'research engineer'
    user.address = 'module_1'
    user.email = 'scott_chief@mars.org'
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.surname = 'Potebnya'
    user.name = 'Danya'
    user.age = 15
    user.position = 'shturman'
    user.speciality = 'testirovshik_unitazov'
    user.address = 'module_2'
    user.email = 'danya_potebnya@mars.org'
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.surname = 'Dragunov'
    user.name = 'Konstantin'
    user.age = 26
    user.position = 'driver'
    user.speciality = 'gospodin'
    user.address = 'module_3'
    user.email = 'gospodin_konstantin@mars.org'
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.surname = 'Baretskiy'
    user.name = 'Stas'
    user.age = 45
    user.position = 'pos_1'
    user.speciality = 'producer'
    user.address = 'module_4'
    user.email = 'stas228@mars.org'
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    # app.run()


if __name__ == '__main__':
    main()
