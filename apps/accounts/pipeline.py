#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib
import json

from apps.accounts.models import UserProfile
def get_profile_picture(
    strategy,
    user,
    response,
    details,
    is_new=False,
    *args,
    **kwargs
    ):
    img_url = None
#    if strategy.backend.name == 'facebook':
    if "facebook" in kwargs['backend'].redirect_uri:
        img_url = 'http://graph.facebook.com/%s/picture?width=200&height=200' \
            % response['id']
    if "vk" in kwargs['backend'].redirect_uri:
        img_url = "https://api.vk.com/method/users.get?user_id=%s&v=5.26&fields=photo_100" % response['user_id']
        raw_json = urllib.urlopen(img_url).read()
        data = json.loads(raw_json)
        img_url = data['response'][0]['photo_100']
#        img_url = img_url['response']
#        img_url = "https://api.vk.com/method/users.get?access_token=ТОКЕН&uids=ID%s&fields=photo_big" \
#            % response['id']
    if "google" in kwargs['backend'].redirect_uri:
        if response.get('image') and response['image'].get('url'):
            img_url = response['image'].get('url')
            img_url = img_url.replace('sz=50', 'sz=200')


#    elif strategy.backend.name == 'twitter':
#        img_url = response.get('profile_image_url', '').replace('_normal', '')
    
    profile = UserProfile.objects.get_or_create(user = user)[0]
    profile.photo = img_url
    profile.save()