from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms import BooleanField, SubmitField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired
from data import db_session
from data.regions import Region
from data.users import User
from data.programs import Programs


class FilterForm(FlaskForm):
    region_choice = []
    uni_choice = []
    city_choice = []
    db_sess = db_session.create_session()
    for region in db_sess.query(Region).all():
        region_choice.append((region.id, region.name))
    for programme in db_sess.query(Programs).all():
        city_choice.append((programme.id, programme.city))
    for university in db_sess.query(User).filter(User.is_admin == 1).all():
        uni_choice.append((university.id, university.name))
    university = SelectField('Университет', choices=uni_choice)
    price = IntegerField('Цена')
    russian = IntegerField('Русский Язык', default=0)
    math_basic = IntegerField('Математика', default=0)
    math_advanced = IntegerField('Профильная Математика', default=0)
    physics = IntegerField('Физика', default=0)
    informatics = IntegerField('Информатика', default=0)
    chemistry = IntegerField('Химия', default=0)
    biology = IntegerField('Биология', default=0)
    geography = IntegerField('География', default=0)
    history = IntegerField('История', default=0)
    social_science = IntegerField('Обществознание', default=0)
    literature = IntegerField('Литература', default=0)
    english = IntegerField('Английский язык', default=0)
    french = IntegerField('Французский язык', default=0)
    german = IntegerField('Немецкий язык', default=0)
    spanish = IntegerField('Испанский язык', default=0)
    chinese = IntegerField('Китайский язык', default=0)
    region = SelectField('Регион', validators=[DataRequired()], choices=region_choice)
    city = SelectField('Город', validators=[DataRequired()], choices=city_choice)
    submit = SubmitField('Применить')
