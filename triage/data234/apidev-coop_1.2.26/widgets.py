# -*- coding: utf-8 -*-
"""widgets"""

from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.forms import TextInput as DjangoTextInput
from django.utils.text import mark_safe
from django.utils.translation import ugettext as _

from floppyforms.widgets import ClearableFileInput, Select, SelectMultiple, Input

from coop_cms.models import NavType
from coop_cms.utils import get_text_from_template



class ReadOnlyInput(Input):
    """readonly input"""
    template_name = 'coop_cms/widgets/readonlyinput.html'


class ImageEdit(ClearableFileInput):
    """image edit"""
    template_name = 'coop_cms/widgets/imageedit.html'
    
    def __init__(self, update_url, thumbnail_src, *args, **kwargs):
        super(ImageEdit, self).__init__(*args, **kwargs)
        self._extra_context = {
            'update_url': update_url,
            'thumbnail_src': thumbnail_src,
            'extra_classes': get_text_from_template("coop_cms/widgets/_imageedit_cssclass.html"),
        }
        
    def get_context(self, *args, **kwargs):
        """get context"""
        context = super(ImageEdit, self).get_context(*args, **kwargs)
        context.update(self._extra_context)
        return context


class ChosenWidgetMixin(object):
    """chosen jquery widget"""

    def _patch(self, kwargs):

        self._extra_context = {}
        if kwargs.pop("force_template", False):
            # chosen inherit from super template
            self._extra_context['super_template'] = self.template_name
            self.template_name = 'coop_cms/widgets/chosen.html'

        self._extra_context['on_popup'] = kwargs.pop("on_popup", False)

        return kwargs


class ChosenSelectMultiple(ChosenWidgetMixin, SelectMultiple):
    """chosen select multiple"""

    def __init__(self, attrs=None, *args, **kwargs):

        kwargs = self._patch(kwargs)

        if not attrs:
            attrs = {}
        attrs['data-placeholder'] = kwargs.pop('overlay', None)
        super(ChosenSelectMultiple, self).__init__(attrs, *args, **kwargs)

    def get_context(self, *args, **kwargs):
        """context"""
        context = super(ChosenSelectMultiple, self).get_context(*args, **kwargs)  # pylint: disable=E1002
        context.update(self._extra_context)
        return context

    class Media:
        """css and js required by widget"""
        js = (
            "{0}?v=1".format("chosen/chosen.jquery.min.js"),
        )
        css = {
            "all": ("{0}?v=1".format("chosen/chosen.css"),),
        }


class ChosenSelect(ChosenWidgetMixin, Select):
    """chosen select"""

    def __init__(self, attrs=None, *args, **kwargs):
        kwargs = self._patch(kwargs)

        if not attrs:
            attrs = {}
        attrs['data-placeholder'] = kwargs.pop('overlay', None)
        super(ChosenSelect, self).__init__(attrs, *args, **kwargs)

    def get_context(self, *args, **kwargs):
        """context"""
        context = super(ChosenSelect, self).get_context(*args, **kwargs)  # pylint: disable=E1002
        context.update(self._extra_context)
        return context

    class Media:
        """css and js required by widget"""
        js = (
            "{0}?v=1".format("chosen/chosen.jquery.min.js"),
        )
        css = {
            "all": ("{0}?v=1".format("chosen/chosen.css"),),
        }


class GenericFieldRawIdWidget(DjangoTextInput):
    """
    A Widget for displaying Generic "raw_id" interface rather than
    in a <select> box.
    """
    def __init__(self, instance, attrs=None):
        super(GenericFieldRawIdWidget, self).__init__(attrs)
        nav_types = NavType.objects.all()
        self.base_nav_urls = []
        self.instance = instance
        for nav_type in nav_types:
            self.base_nav_urls.append(
                (
                    nav_type.content_type.id,
                    reverse(
                        'admin:{0}_{1}_changelist'.format(
                            nav_type.content_type.app_label,
                            nav_type.content_type.model
                        )
                    )
                )
            )

    def get_nav_types_url_html(self):
        """returns html for JS"""
        html = u'<ul class="nav_type_urls">{0}</ul>'.format(
            u''.join(
                [
                    u'<li rel="{0}">{1}</li>'.format(nav_type_id, nav_type_url)
                    for nav_type_id, nav_type_url in self.base_nav_urls
                ]
            )
        )
        return html

    def render(self, name, value, attrs=None):
        if attrs is None:
            attrs = {}
        extra = []

        if "class" not in attrs:
            attrs['class'] = u'vGenericRawIdAdminField'  # The JavaScript code looks for this hook.
            # the correct API to determine the ID dynamically.
            extra.append(u'<a href="" class="related-lookup" id="lookup_id_{0}" title="{1}"></a>'.format(
                name, _(u'Lookup'))
            )
        output = [super(GenericFieldRawIdWidget, self).render(name, value, attrs)] + extra
        output.append(self.get_nav_types_url_html())
        if self.instance:
            output.append(self.label_for_value(self.instance))
        return mark_safe(''.join(output))

    def label_for_value(self, instance):
        try:
            model_class = instance.content_type.model_class()
            label = model_class.objects.get(id=instance.object_id)
        except AttributeError:
            label = u''
        except ObjectDoesNotExist:
            label = u"<Not Found>"

        if label:
            return u"{0}:{1} ({2})".format(
                instance.content_type,
                instance.object_id,
                label
            )
        return u''
