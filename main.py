from flask import Flask, render_template, redirect, abort, request
from data import db_session
from data.users import User
from data.programs import Programs
from data.ege import Ege
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from forms.loginform import LoginForm
from forms.user import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'k8ig8ob4mE99Qkk0VnAUIl77yy24Xwyj'
login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/')
@app.route('/index')
def index():
    db_sess = db_session.create_session()
    programs = db_sess.query(Programs)
    return render_template('index.html', programs=programs)


@app.route('/register', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


@app.route('/add_new',  methods=['GET', 'POST'])
@login_required
def add_programme():
    from forms.programmeform import ProgrammeForm
    form = ProgrammeForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        db_sess.expire_on_commit = False
        ege = Ege()
        ege.math_basic = form.math_basic.data
        ege.math_advanced = form.math_advanced.data
        ege.russian = form.russian.data
        ege.informatics = form.informatics.data
        ege.physics = form.physics.data
        ege.biology = form.biology.data
        ege.chemistry = form.chemistry.data
        ege.history = form.history.data
        ege.social_science = form.social_science.data
        ege.literature = form.literature.data
        ege.english = form.english.data
        ege.french = form.french.data
        ege.german = form.german.data
        ege.spanish = form.spanish.data
        ege.chinese = form.chinese.data
        ege.geography = form.geography.data
        db_sess.add(ege)
        db_sess.commit()
        programme = Programs()
        programme.name = form.title.data
        programme.faculty = form.faculty.data
        programme.ege = ege.id
        programme.price = form.price.data
        programme.region = form.region.data
        programme.city = form.city.data
        programme.link = form.link.data
        current_user.programs.append(programme)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/')
    return render_template('add_new.html', title='Добавление программы',
                           form=form)


@app.route('/programs/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_programme(id):
    from forms.programmeform import ProgrammeForm
    form = ProgrammeForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        programme = db_sess.query(Programs).filter(Programs.id == id,
                                                   Programs.admin == current_user
                                                   ).first()
        ege = db_sess.query(Ege).filter(Ege.id == Programs.ege,
                                        ).first()
        if programme:
            form.title.data = programme.name
            form.faculty.data = programme.faculty
            form.price.data = programme.price
            form.region.data = programme.region
            form.city.data = programme.city
            form.link.data = programme.link
            form.math_basic.data = ege.math_basic
            form.math_advanced.data = ege.math_advanced
            form.russian.data = ege.russian
            form.informatics.data = ege.informatics
            form.physics.data = ege.physics
            form.biology.data = ege.biology
            form.chemistry.data = ege.chemistry
            form.history.data = ege.history
            form.social_science.data = ege.social_science
            form.literature.data = ege.literature
            form.english.data = ege.english
            form.french.data = ege.french
            form.german.data = ege.german
            form.spanish.data = ege.spanish
            form.chinese.data = ege.chinese
            form.geography.data = ege.geography
            programme = Programs()
            programme.name = form.title.data
            programme.faculty = form.faculty.data
            programme.ege = ege.id
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        programme = db_sess.query(Programs).filter(Programs.id == id,
                                                   Programs.admin == current_user).first()
        ege = db_sess.query(Ege).filter(Ege.id == Programs.ege).first()
        if programme:
            ege.math_basic = form.math_basic.data
            ege.math_advanced = form.math_advanced.data
            ege.russian = form.russian.data
            ege.informatics = form.informatics.data
            ege.physics = form.physics.data
            ege.biology = form.biology.data
            ege.chemistry = form.chemistry.data
            ege.history = form.history.data
            ege.social_science = form.social_science.data
            ege.literature = form.literature.data
            ege.english = form.english.data
            ege.french = form.french.data
            ege.german = form.german.data
            ege.spanish = form.spanish.data
            ege.chinese = form.chinese.data
            ege.geography = form.geography.data
            programme.name = form.title.data
            programme.faculty = form.faculty.data
            programme.price = form.price.data
            programme.region = form.region.data
            programme.city = form.city.data
            programme.link = form.link.data
            programme.ege = ege.id
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('add_new.html',
                           title='Редактирование информации о программе',
                           form=form)


@app.route('/filter', methods=['GET', 'POST'])
def programme_filter():
    from forms.filterform import FilterForm
    form = FilterForm()
    if form.validate_on_submit():
        math_basic = form.math_basic.data
        math_advanced = form.math_advanced.data
        russian = form.russian.data
        informatics = form.informatics.data
        physics = form.physics.data
        biology = form.biology.data
        chemistry = form.chemistry.data
        history = form.history.data
        social_science = form.social_science.data
        literature = form.literature.data
        english = form.english.data
        french = form.french.data
        german = form.german.data
        spanish = form.spanish.data
        chinese = form.chinese.data
        geography = form.geography.data
        price = form.price.data
        region = form.region.data
        city = form.city.data
        return redirect(f'/filter/{math_basic}!{math_advanced}!{russian}!{physics}!{informatics}!'
                        f'{biology}!'
                        f'{chemistry}!{history}!{social_science}!{literature}!{english}!{french}!'
                        f'{german}!{spanish}!{chinese}!{geography}!{price}!{region}!{city}')
    return render_template('filter.html', title='Фильтр',
                           form=form)


@app.route('/filter/<int:math_basic>!<int:math_advanced>!<int:russian>!<int:physics>!<int:informatics>!'
           f'<int:biology>!'
           f'<int:chemistry>!<int:history>!<int:social_science>!<int:literature>!<int:english>!<int:french>!'
           f'<int:german>!<int:spanish>!<int:chinese>!<int:geography>!<int:price>!<int:region>!<string:city>',
           methods=['GET', 'POST'])
def filtered_programs(math_basic, math_advanced, russian, physics, informatics, biology, chemistry, history,
                      social_science, literature, english, french, german, spanish, chinese, geography, price,
                      region, city):
    db_sess = db_session.create_session()
    ege = db_sess.query(Ege.id).filter(Ege.math_basic == math_basic, Ege.math_advanced == math_advanced,
                                       Ege.russian == russian, Ege.physics == physics,
                                       Ege.informatics == informatics, Ege.biology == biology,
                                       Ege.chemistry == chemistry, Ege.history == history,
                                       Ege.social_science == social_science, Ege.literature == literature,
                                       Ege.english == english, Ege.french == french,
                                       Ege.german == german, Ege.spanish == spanish,
                                       Ege.chinese == chinese, Ege.geography == geography).all()
    programs = db_sess.query(Programs).filter(Programs.ege in ege,
                                              Programs.price == price,
                                              Programs.region == region,
                                              Programs.city == city).all()
    return render_template('index.html', programs=programs)


@app.route('/programs_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def programme_delete(id):
    db_sess = db_session.create_session()
    news = db_sess.query(Programs).filter(Programs.id == id,
                                          Programs.admin == current_user).first()
    if news:
        db_sess.delete(news)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


def main():
    db_session.global_init("db/programs.db")
    app.run(port=8080, host='127.0.0.1')


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


if __name__ == '__main__':
    main()
