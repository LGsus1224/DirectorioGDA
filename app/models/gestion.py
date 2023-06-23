from app.ext import db
import enum


class Owners(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    profile_image = db.Column(db.String(250), nullable=False, default='default.png')
    bg_image = db.Column(db.String(250), nullable=False, default='default.jpg')
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'),nullable=False)

    def __init__(self):
        super(Owners,self).__init__()


class Business(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    tradename = db.Column(db.String(100), nullable=False, default='Mi Negocio')
    business_name = db.Column(db.String(100), nullable=False, default='Nombre Comercial')
    address = db.Column(db.String(150), nullable=False, default='Dirección Comercial')
    phone = db.Column(db.String(10), nullable=False, default='0999999999')
    short_description = db.Column(db.String(80), nullable=False, default='Bienvenido a mi Negocio')
    description = db.Column(db.String(500), nullable=False, default='Descripción larga de mi negocio')
    owner_id = db.Column(db.Integer(), db.ForeignKey('owners.id', ondelete='CASCADE'), nullable=False)
    owner = db.relationship('Owners', backref='Business')

    def __init__(self):
        super(Business,self).__init__()


class categoriesEnum(enum.Enum):
    stores = 'stores'
    tourism = 'tourism'
    restaurants = 'restaurants'
    mechanics = 'mechanics'
    drinks_and_licors = 'drinks_and_licors'
    coffee_and_bar = 'coffee_and_bar'
    marketing = 'marketing'
    health = 'health'
    others = 'others'

class Categories(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    category = db.Column(db.Enum(categoriesEnum), nullable=False, unique=True)

    def __init__(self):
        super(Categories,self).__init__()


class labelsEnum(enum.Enum):
    parquing = 'parquing'
    pets = 'pets'
    wifi = 'wifi'
    card_payment = 'card_payment'
    pizzeria = 'pizzeria'

class Labels(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    label = db.Column(db.Enum(labelsEnum), nullable=False, unique=True)

    def __init__(self):
        super(Labels,self).__init__()


class BusinessCategories(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    business_id = db.Column(db.Integer(), db.ForeignKey('business.id',ondelete="CASCADE"), nullable=False)
    category_id = db.Column(db.Integer(), db.ForeignKey('categories.id',ondelete="CASCADE"), nullable=False)
    business = db.relationship('Business', backref='BusinessCategories')
    category = db.relationship('Categories', backref='BusinessCategories')

    def __init__(self):
        super(BusinessCategories,self).__init__()


class BusinessLabels(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    business_id = db.Column(db.Integer(), db.ForeignKey('business.id',ondelete="CASCADE"), nullable=False)
    label_id = db.Column(db.Integer(), db.ForeignKey('labels.id',ondelete="CASCADE"), nullable=False)
    business = db.relationship('Business', backref='BusinessLabels')
    label = db.relationship('Labels', backref='BusinessLabels')

    def __init__(self):
        super(BusinessLabels,self).__init__()


class BusinessGallery(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    business_id = db.Column(db.Integer(), db.ForeignKey('business.id',ondelete="CASCADE"), nullable=False)
    image = db.Column(db.String(150), nullable=False)

    def __init__(self):
        super(BusinessGallery,self).__init__()


class daysEnum(enum.Enum):
    monday = 'monday'
    tuesday = 'tuesday'
    wednesday = 'wednesday'
    thursday = 'thursday'
    friday = 'friday'
    saturday = 'saturday'
    sunday = 'sunday'

class WorkHours(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    business_id = db.Column(db.Integer(), db.ForeignKey('business.id',ondelete="CASCADE"), nullable=False)
    day = db.Column(db.Enum(daysEnum), nullable=False)
    open_hour = db.Column(db.Time(), nullable=False)
    close_hour = db.Column(db.Time(), nullable=False)

    def __init__(self):
        super(WorkHours,self).__init__()
