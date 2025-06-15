# -*- coding: utf-8 -*-
"""
Default CMS application : It define a simple Article
"""

from coop_cms.bs_forms import Form, ModelForm

#Just for compatibility


class BootstrapForm(Form):  # pylint: disable=R0901
    """Deprecated: Just for compatibility"""
    pass


class BootstrapModelForm(ModelForm):  # pylint: disable=R0901
    """Deprecated: Just for compatibility"""
    pass
