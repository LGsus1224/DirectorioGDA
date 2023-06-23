from app.ext import db
from .db_enum_options import categories,labels
from app.models import Categories,Labels


def db_create_models():
    db.create_all()


def create_categories():
    try:
        for i in categories:
            new_category = Categories()
            new_category.category = i[0]
            db.session.add(new_category)
            db.session.commit()
    except Exception as e:
        db.session.rollback()


def create_labels():
    try:
        for i in labels:
            new_label = Labels()
            new_label.label = i[0]
            db.session.add(new_label)
            db.session.commit()
    except Exception as e:
        db.session.rollback()

