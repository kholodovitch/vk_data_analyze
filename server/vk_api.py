#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import vk_auth
import json
import urllib2
from urllib import urlencode

class vk_api(object):
    token = ""
    user_id = ""

    def call_api(self, method, params, token):
        params.append(("access_token", token))
        url = "https://api.vk.com/method/%s?%s" % (method, urlencode(params))
        return json.loads(urllib2.urlopen(url).read())["response"]

    def auth(self, email, password, client_id):
        self.token, self.user_id = vk_auth.auth(email, password, client_id, "photos")

    def get_albums(self):
        return self.call_api("photos.getAlbums", [("uid", self.user_id)], self.token)

    def get_albums(self, user_id):
        return self.call_api("photos.getAlbums", [("uid", user_id)], self.token)

    def users_get(self, uids):
        return self.call_api("users.get", [("uids", uids)], self.token)

    def users_get(self, uids, fields):
        return self.call_api("users.get", [("uids", uids), ("fields", fields)], self.token)

