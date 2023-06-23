from app.ext import db
from flask import Blueprint,render_template,redirect,url_for
from flask_login import login_required,current_user
# utils
from app.common.business_utils import (
    get_current_owner,
    get_current_business,
    get_profile_image,
    get_bg_image,
    save_profile_image,
    save_bg_image,
    get_gallery_images,
    save_gallery_images,
    delete_gallery_images
    )
# forms
from .forms import (
    UpdateImagesForm,
    OwnerDataForm,
    BusinessDataForm,
    BusinessDescriptionForm,
    CategoriesLabelsForm,
    UpdateBusinessGalleryForm,
    )
# models
from app.models import (
    BusinessCategories,
    BusinessLabels,
    Owners,
    Business,
    Categories,
    Labels,
    BusinessGallery
    )


mod_owner_bp = Blueprint('mod_owner_bp', __name__, url_prefix='/my_business')


@mod_owner_bp.route('/profile', methods=['GET'])
@login_required
def profile():
    images_form = UpdateImagesForm()
    owner_form = OwnerDataForm()
    business_form = BusinessDataForm()
    c_l_form = CategoriesLabelsForm()
    business_description_form = BusinessDescriptionForm()
    business_gallery_form = UpdateBusinessGalleryForm()
    # query
    owner = get_current_owner(current_user)
    business = get_current_business(owner.id)
    profile_image = get_profile_image(owner.profile_image)
    bg_image = get_bg_image(owner.bg_image)
    gallery = get_gallery_images(business.id)
    # form preconfig
    business_form.short_description.default = business.short_description
    business_form.process()
    business_description_form.description.default = business.description
    business_description_form.process()
    business_gallery_form.images_to_delete.choices = [(str(i),str(i)) for i in gallery]
    my_categories = BusinessCategories.query.filter(BusinessCategories.business_id==business.id).all()
    my_labels = BusinessLabels.query.filter(BusinessLabels.business_id==business.id).all()
    c_l_form.categories.data = [i.category.category.value for i in my_categories]
    c_l_form.labels.data = [i.label.label.value for i in my_labels]
    return render_template('user-profile.html', owner=owner, business=business,
                            profile_image=profile_image, bg_image=bg_image,gallery=gallery,
                            images_form=images_form, owner_form=owner_form,business_form=business_form,
                            business_description_form=business_description_form,c_l_form=c_l_form,
                            business_gallery_form=business_gallery_form,
                            my_categories=my_categories,my_labels=my_labels
                            )


@mod_owner_bp.route('/update/owner/images/<owner_id>', methods=['POST'])
@login_required
def update_owner_images(owner_id):
    try:
        form = UpdateImagesForm()
        profile_image = form.profile_image.data
        bg_image = form.bg_image.data
        owner = Owners.query.filter(Owners.id==owner_id).first()
        owner.profile_image = save_profile_image(owner.profile_image,profile_image)
        owner.bg_image = save_bg_image(owner.bg_image,bg_image)
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        return redirect(url_for('mod_owner_bp.profile'))


@mod_owner_bp.route('/update/owner/data/<owner_id>', methods=['POST'])
@login_required
def update_owner_data(owner_id):
    form = OwnerDataForm()
    try:
        if not form.validate_on_submit(): raise Exception('Formulario no valido')
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        owner = Owners.query.filter(Owners.id==owner_id).first()
        owner.first_name = first_name
        owner.last_name = last_name
        owner.email = email
        db.session.commit()
    except Exception as e:
        db.session.rollback()
    finally:
        return redirect(url_for('mod_owner_bp.profile'))


@mod_owner_bp.route('/update/business/data/<business_id>', methods=['POST'])
@login_required
def update_business_data(business_id):
    form = BusinessDataForm()
    try:
        if not form.validate_on_submit(): raise Exception('Formulario no valido')
        tradename = form.tradename.data
        business_name = form.business_name.data
        address = form.address.data
        phone = form.phone.data
        short_description = form.short_description.data
        business = Business.query.filter(Business.id==business_id).first()
        business.tradename = tradename
        business.business_name = business_name
        business.address = address
        business.phone = phone
        business.short_description = short_description
        db.session.commit()
    except Exception as e:
        db.session.rollback()
    finally:
        return redirect(url_for('mod_owner_bp.profile'))


@mod_owner_bp.route('/update/business/description/<business_id>', methods=['POST'])
@login_required
def update_business_description(business_id):
    form = BusinessDescriptionForm()
    try:
        if not form.validate_on_submit(): raise Exception('Formulario no valido')
        description = form.description.data
        business = Business.query.filter(Business.id==business_id).first()
        business.description = description
        db.session.commit()
    except Exception as e:
        db.session.rollback()
    finally:
        return redirect(url_for('mod_owner_bp.profile'))


@mod_owner_bp.route('/update/business/categories_and_labels/<business_id>', methods=['POST'])
@login_required
def update_business_categories_and_labels(business_id):
    form = CategoriesLabelsForm()
    try:
        if not form.validate_on_submit(): raise Exception('Formulario no valido')
        categories = form.categories.data
        labels = form.labels.data
        current_categories = BusinessCategories.query.filter(
            BusinessCategories.business_id==business_id).all()
        current_labels = BusinessLabels.query.filter(
            BusinessLabels.business_id==business_id).all()
        for i in current_categories:
            db.session.delete(i)
        for i in current_labels:
            db.session.delete(i)
        for i in categories:
            category = Categories.query.filter(Categories.category==i).first()
            new_category = BusinessCategories()
            new_category.business_id = business_id
            new_category.category_id = category.id
            db.session.add(new_category)
        for i in labels:
            label = Labels.query.filter(Labels.label==i).first()
            new_label = BusinessLabels()
            new_label.business_id = business_id
            new_label.label_id = label.id
            db.session.add(new_label)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
    finally:
        return redirect(url_for('mod_owner_bp.profile'))


@mod_owner_bp.route('/update/business/gallery/<business_id>', methods=['POST'])
@login_required
def update_business_gallery(business_id):
    form = UpdateBusinessGalleryForm()
    try:
        gallery = get_gallery_images(business_id)
        form.images_to_delete.choices = [(str(i),str(i)) for i in gallery]
        if not form.validate_on_submit(): raise Exception('Formulario no valido')
        new_images = form.new_images.data
        images_to_delete = form.images_to_delete.data
        delete_gallery_images(images_to_delete)
        for i in images_to_delete:
            registro = BusinessGallery.query.filter(BusinessGallery.business_id==business_id,
                                                    BusinessGallery.image==i).first()
            db.session.delete(registro)
            db.session.commit()
        images_ready_to_save = save_gallery_images(new_images)
        for i in images_ready_to_save:
            new_image = BusinessGallery()
            new_image.business_id=business_id
            new_image.image=i
            db.session.add(new_image)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
    finally:
        return redirect(url_for('mod_owner_bp.profile'))
