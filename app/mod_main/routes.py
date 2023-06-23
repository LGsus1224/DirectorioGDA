from app.ext import db
from flask import Blueprint,render_template,redirect,url_for
from flask_login import current_user
from app.common.html_enum_options import html_categories,html_labels
# utils
from app.common.business_utils import (
    get_current_owner,
    get_bg_image,
    get_profile_image,
    get_gallery_images
    )
# models
from app.models import (Owners,Business,BusinessCategories,BusinessLabels,Categories)

mod_main_bp = Blueprint('mod_main_bp', __name__)


@mod_main_bp.route('/', methods=['GET'])
def index():
    owner = get_current_owner(current_user)
    current_business = Business.query.all()
    current_owners = []
    current_categories = {}
    for i in current_business:
        publish_owner = Owners.query.filter(Owners.id==i.owner_id).first()
        if publish_owner != None:
            current_owners.append(publish_owner)
            business_categories = BusinessCategories.query.filter(BusinessCategories.business_id==i.id).all()
            current_categories[publish_owner.id] = business_categories
    return render_template('index.html',owner=owner,html_categories=html_categories,
                           current_business=current_business,current_owners=current_owners,
                           current_categories=current_categories)


@mod_main_bp.route('/negocio/<business_id>', methods=['GET'])
def business_description(business_id):
    try:
        business = Business.query.filter(Business.id==business_id).first()
        if business == None: raise Exception('No existe el negocio buscado')
        owner = get_current_owner(current_user)
        business_owner = Owners.query.filter(Owners.id==business.owner_id).first()
        profile_image = get_profile_image(business_owner.profile_image)
        bg_image = get_bg_image(business_owner.bg_image)
        business_gallery = get_gallery_images(business_id)
        business_categories = BusinessCategories.query.filter(BusinessCategories.business_id==business_id).all()
        business_labels = BusinessLabels.query.filter(BusinessLabels.business_id==business_id).all()
        return render_template('business-description.html', owner=owner, business=business,
                                business_owner=business_owner, bg_image=bg_image,profile_image=profile_image,
                                html_categories=html_categories,html_labels=html_labels,business_categories=business_categories,
                                business_labels=business_labels,business_gallery=business_gallery)
    except:
        return redirect(url_for('mod_main_bp.index'))


@mod_main_bp.route('/categoria/<category>', methods=['GET'])
def business_by_category(category):
    try:
        owner = get_current_owner(current_user)
        business_filtered = db.session.query(BusinessCategories).join(Categories).filter(Categories.category == category).all()
        current_business = []
        current_categories = {}
        for i in business_filtered:
            business = Business.query.filter(Business.id==i.business_id).first()
            if business != None:
                business_categories = BusinessCategories.query.filter(BusinessCategories.business_id==business.id).all()
                current_categories[business.id] = business_categories
                current_business.append(business)
        return render_template('business-by-category.html', category=category, owner=owner, current_business=current_business,
                               current_categories=current_categories, html_categories=html_categories)
    except:
        return redirect(url_for('mod_main_bp.index'))