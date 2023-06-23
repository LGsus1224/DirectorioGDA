from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,EmailField
from wtforms.validators import InputRequired,DataRequired,Email

class LoginForm(FlaskForm):
    username = StringField('Usuario',validators=[DataRequired(),InputRequired()],
                           render_kw={
                                'class':'form-control',
                                'placeholder':'Nombre de Usuario',
                                'id':'username'})
    password = PasswordField('Contraseña', validators=[DataRequired(),InputRequired()],
                             render_kw={
                                'class':'form-control border-end-0',
                                'placeholder':'Contraseña',
                                'autocomplete':'off',
                                'id':'inputChoosePassword'})


class SignupForm(FlaskForm):
    first_name = StringField('Nombre', validators=[DataRequired(),InputRequired()],
                            render_kw={
                                'class':'form-control',
                                'placeholder':'Jhon',
                            })
    last_name = StringField('Apellido', validators=[DataRequired(),InputRequired()],
                            render_kw={
                                'class':'form-control',
                                'placeholder':'García',
                            })
    email= EmailField('Correo Electrónico', validators=[DataRequired(),InputRequired(),Email()],
                        render_kw={
                            'class':'form-control',
                            'placeholder':'example@user.com'
                        })
    username = StringField('Usuario',validators=[DataRequired(),InputRequired()],
                           render_kw={
                                'class':'form-control',
                                'placeholder':'Nombre de Usuario',
                                'id':'username'})
    password = PasswordField('Contraseña', validators=[DataRequired(),InputRequired()],
                             render_kw={
                                'class':'form-control border-end-0',
                                'placeholder':'Contraseña',
                                'autocomplete':'off',
                                'id':'inputChoosePassword'})

