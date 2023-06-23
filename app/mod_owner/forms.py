from flask_wtf import FlaskForm
from wtforms import (
    FileField,StringField,EmailField,TelField,TextAreaField,
    SelectMultipleField,MultipleFileField
)
from wtforms.validators import DataRequired,InputRequired,Email,Length
from flask_wtf.file import FileSize,FileAllowed
# common
from app.common.db_enum_options import categories,labels


class UpdateImagesForm(FlaskForm):
    profile_image = FileField('Imagen de Perfil',validators=[
        FileAllowed(['png','jpg','jpeg'],'Solo se aceptan formatos .png .jpg .jpeg'),
        FileSize(max_size=1048576,message='Pesa máximo 1mb')
    ],
    render_kw={
        'class':'form-control',
    })
    bg_image = FileField('Imagen de Fondo',validators=[
        FileAllowed(['png','jpg','jpeg'],'Solo se aceptan formatos .png .jpg .jpeg'),
        FileSize(max_size=3000,message='Peso máximo 3mb')
    ],
    render_kw={
        'class':'form-control',
    })


class OwnerDataForm(FlaskForm):
    first_name = StringField('Nombre de Usuario',validators=[DataRequired(),InputRequired()],
                                render_kw={
                                    'class':'form-control',
                                    'placeholder':'Ingresa tu nombre'
                                })
    last_name = StringField('Apellido',validators=[DataRequired(),InputRequired()],
                                render_kw={
                                    'class':'form-control',
                                    'placeholder':'Ingresa tu nombre'
                                })
    email= EmailField('Correo Electrónico', validators=[DataRequired(),InputRequired(),Email()],
                        render_kw={
                            'class':'form-control',
                            'placeholder':'example@user.com'
                        })

class BusinessDataForm(FlaskForm):
    tradename = StringField('Nombre de negocio',validators=[DataRequired(),InputRequired()],
                            render_kw={
                                'class':'form-control',
                                'placeholder':'Mi negocio example'
                            })
    business_name = StringField('Nombre Comercial',validators=[DataRequired(),InputRequired()],
                                render_kw={
                                    'class':'form-control',
                                    'placeholder':'Nombre Comercial'
                                })
    address = StringField('Dirección Comercial',validators=[DataRequired(),InputRequired()],
            render_kw={
                'class':'form-control',
                'placeholder':'Dirección ejemplo 123'
            })
    phone = TelField('Teléfono',validators=[DataRequired(),InputRequired(),Length(max=10)],
                        render_kw={
                            'class':'form-control',
                            'placeholder':'099------'
                        })
    short_description = TextAreaField('Descripción Corta', validators=[DataRequired(),InputRequired(),Length(max=80)],
                                    render_kw={
                                        'class':'form-control',
                                        'placeholder':'Descripción breve.',
                                        'rows':3
                                    })


class BusinessDescriptionForm(FlaskForm):
    description = TextAreaField('Descripción de tu negocio', validators=[DataRequired(),InputRequired(),Length(max=500)],
                                    render_kw={
                                        'class':'form-control',
                                        'placeholder':'Aqui describe tu negocio.',
                                        'rows':22
                                    })

class CategoriesLabelsForm(FlaskForm):
    categories = SelectMultipleField('Categorías',choices=categories,validate_choice=True,
                                        render_kw={
                                            'class':'form-control select',
                                            'placeholder':'Selecciona las categorías de tu negocio'
                                        })
    labels = SelectMultipleField('Etiquetas',choices=labels,validate_choice=True,
                                        render_kw={
                                            'class':'form-control select',
                                            'placeholder':'Selecciona las etiquetas de tu negocio'
                                        })


class UpdateBusinessGalleryForm(FlaskForm):
    new_images = MultipleFileField('Subir Imagenes',validators=[
        FileAllowed(['png','jpg','jpeg'],'Solo se aceptan formatos .png .jpg .jpeg'),
        FileSize(max_size=2097152,message='Peso máximo 2mb'),], render_kw={
        'class':'form-control',
    })
    images_to_delete = SelectMultipleField('Imágenes a eliminar',choices=[],render_kw={
        'class':'form-control',
        'style':'display:none;'
    })

