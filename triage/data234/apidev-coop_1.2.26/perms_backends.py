# -*- coding: utf-8 -*-
"""permission backend"""


class ArticlePermissionBackend(object):
    """Permission backend : check if a user is allowed to view/edit an editable object"""
    supports_object_permissions = True
    supports_anonymous_user = True
    supports_inactive_user = True

    def authenticate(self, *args, **kwargs):
        """authentication: return None --> no authentication through this backed"""
        return None

    def has_perm(self, user_obj, perm, obj=None):
        """has_perm : check if user is allowed to access obj for perm"""

        if obj:
            #get the 'perm' attribute of the object
            field = getattr(obj, perm, None)
            if field:
                if not callable(field):
                    #if an attribute : use the value
                    is_authorized = field
                else:
                    #if a method call it with user
                    is_authorized = field(user_obj)
                return is_authorized
        return False
