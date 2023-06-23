import secrets
from app.ext import db
from app.models import Owners,Business,BusinessGallery
from werkzeug.utils import secure_filename
from os import getcwd,remove

USERS_PATH = getcwd() + '/app/assets/images/avatars/'
BG_PATH = getcwd() + '/app/assets/images/backgrounds/'
GALLERY_PATH = getcwd() + '/app/assets/images/gallery/'

STATIC_USERS_PATH = 'images/avatars/'
STATIC_BG_PATH = 'images/backgrounds/'
STATIC_GALLERY_PATH = 'images/gallery/'

def get_profile_image(image_name):
    return STATIC_USERS_PATH+str(image_name)

def get_bg_image(image_name):
    return STATIC_BG_PATH+str(image_name)

def get_current_owner(current_user):
    if current_user.is_authenticated:
        return Owners.query.filter(Owners.user_id == current_user.id).first()
    else: return None

def get_current_business(owner_id):
    return Business.query.filter(Business.owner_id == owner_id).first()

def save_profile_image(profile_image,filename):
    if filename.filename != '':
        current_image = profile_image
        file = filename
        file_filename = secure_filename(secrets.token_hex(10)+file.filename)
        file.save(USERS_PATH + file_filename)
        if current_image != 'default.png':
            remove(USERS_PATH + current_image)
        return file_filename
    else:
        return profile_image

def save_bg_image(bg_image,filename):
    if filename.filename != '':
        current_image = bg_image
        file = filename
        file_filename = secure_filename(secrets.token_hex(10)+file.filename)
        file.save(BG_PATH + file_filename)
        if current_image != 'default.jpg':
            remove(BG_PATH + current_image)
        return file_filename
    else:
        return bg_image

def get_gallery_images(business_id):
    gallery = BusinessGallery.query.filter(BusinessGallery.business_id==business_id).all()
    gallery_list = []
    for i in gallery:
        gallery_list.append(str(i.image))
    return gallery_list

def delete_gallery_images(images):
    for i in images:
        try:
            remove(GALLERY_PATH + i)
        except:
            pass
    return

def save_gallery_images(new_images):
    images_list = []
    for i in new_images:
        if i.filename != '':
            file = i
            file_filename = secure_filename(secrets.token_hex(10)+file.filename)
            file.save(GALLERY_PATH + file_filename)
            images_list.append(file_filename)
    return images_list
