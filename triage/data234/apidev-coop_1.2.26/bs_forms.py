# -*- coding: utf-8 -*-
"""Boptstrap-css friendly forms"""

import floppyforms as forms

from coop_cms.templatetags.coop_utils import is_checkbox


class BootstrapableMixin(object):

    def _bs_patch_field_class(self):
        for field_name in self.fields:
            field = self.fields[field_name]
            if not is_checkbox(field):
                if 'class' in field.widget.attrs:
                    val = field.widget.attrs['class']
                    field.widget.attrs['class'] = val + " form-control"
                else:
                    field.widget.attrs['class'] = "form-control"

            if self.fields[field_name].required:
                self.fields[field_name].widget.attrs['required'] = 'required'


class Form(forms.Form, BootstrapableMixin):

    def __init__(self, *args, **kwargs):
        super(Form, self).__init__(*args, **kwargs)
        self._bs_patch_field_class()


class ModelForm(forms.ModelForm, BootstrapableMixin):

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self._bs_patch_field_class()
