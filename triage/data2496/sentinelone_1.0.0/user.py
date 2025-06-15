import six


class ApiToken(object):
    def __init__(self, **kwargs):
        self.expiresAt = kwargs.get('expiresAt', None)
        self.createdAt = kwargs.get('createdAt', None)


class SiteRole(object):
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.roles = kwargs.get('roles', None)

    def to_json(self):
        return self.__dict__


class User(object):

    def __init__(self, **kwargs):
        self.agreedEula = kwargs.get('agreedEula', None)
        self.agreementUrl = kwargs.get('agreementUrl', None)
        self.allowRemoteShell = kwargs.get('allowRemoteShell', None)

        if kwargs.get('apiToken', None):
            self.apiToken = ApiToken(**kwargs.get('apiToken'))
        else:
            self.apiToken = None

        self.dateJoined = kwargs.get('dateJoined', None)
        self.email = kwargs.get('email', None)
        self.emailReadOnly = kwargs.get('emailReadOnly', None)
        self.emailVerified = kwargs.get('emailVerified', None)
        self.groupsReadOnly = kwargs.get('groupsReadOnly', None)

        self.firstLogin = kwargs.get('firstLogin', None)
        self.fullName = kwargs.get('fullName', None)
        self.fullNameReadOnly = kwargs.get('fullNameReadOnly', None)
        self.id = kwargs.get('id', None)
        self.lastLogin = kwargs.get('lastLogin', None)
        self.lowestRole = kwargs.get('lowestRole', None)
        self.password = kwargs.get('password', None)
        self.rememberMe = kwargs.get('rememberMe', None)
        self.scope = kwargs.get('scope', None)
        self.scopeRoles = kwargs.get('scopeRoles', None)

        self.siteRoles = list()
        if kwargs.get('siteRoles', None):
            for item in kwargs.get('siteRoles'):
                if isinstance(item, dict):
                    self.siteRoles.append(SiteRole(**item))
                else:
                    self.siteRoles.append(item)
        else:
            self.siteRoles = None

        self.source = kwargs.get('source', None)
        self.tenantRoles = kwargs.get('tenantRoles', None)
        self.twoFaEnabled = kwargs.get('twoFaEnabled', None)
        self.twoFaEnabledReadOnly = kwargs.get('twoFaEnabledReadOnly', None)
        self.username = kwargs.get('username', None)
        self.pages = kwargs.get('pages', None)
        self.canGenerateApiToken = kwargs.get('canGenerateApiToken', None)

    def to_json(self):
        data = self.__dict__
        del data['apiToken']
        del data['agreedEula']
        del data['emailVerified']
        del data['firstLogin']
        del data['lastLogin']
        if self.scope == 'site':
            if self.siteRoles:
                site_roles_list = list()
                for role in self.siteRoles:
                    site_role_json = role.to_json()
                    site_roles_list.append(site_role_json)
                data['siteRoles'] = site_roles_list
            del data['tenantRoles']
        if self.scope == 'tenant':
            del data['siteRoles']
        if not self.scope:
            if self.siteRoles:
                site_roles_list = list()
                for role in self.siteRoles:
                    site_role_json = role.to_json()
                    site_roles_list.append(site_role_json)
                data['siteRoles'] = site_roles_list
        non_empty_json = {k: v for (k, v) in six.iteritems(data) if v is not None}
        return non_empty_json
