from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms import BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired
from data import db_session
from data.regions import Region



class ProgrammeForm(FlaskForm):
    region_choice = []
    db_sess = db_session.create_session()
    for region in db_sess.query(Region).all():
        region_choice.append((region.id, region.name))
    title = StringField('Название', name='Название', validators=[DataRequired()])
    faculty = StringField('Факультет', validators=[DataRequired()])
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
    price = IntegerField('Цена', validators=[DataRequired()])
    region = SelectField('Регион', validators=[DataRequired()], choices=region_choice)
    city = StringField('Город', validators=[DataRequired()])
    link = StringField("Cсылка", validators=[DataRequired()])
    submit = SubmitField('Применить')
