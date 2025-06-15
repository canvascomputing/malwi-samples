# -*- coding: utf-8 -*-
"""generic views"""

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.messages.api import success as success_message, error as error_message
from django.core.cache import cache
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.forms.models import modelformset_factory
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.translation import ugettext as _, get_language
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.views.generic.list import ListView as DjangoListView

from coop_html_editor import utils as html_editor_utils

from coop_cms.logger import logger
from coop_cms.settings import is_cache_enabled


class ListView(DjangoListView):
    """generic list view"""
    ordering = ''
    
    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['model'] = self.model
        return context
    
    def get_queryset(self):
        if self.ordering:
            if type(self.ordering) in (list, tuple):
                return self.model.objects.order_by(*self.ordering)
            else:
                return self.model.objects.order_by(self.ordering)
        else:
            return self.model.objects.all()


class EditableObjectView(View):
    """Base class for html-inline editable objects"""
    model = None
    template_name = ""
    form_class = None
    field_lookup = "pk"
    edit_mode = False
    varname = "object"
    object = None
    form = None
    cache_enabled = None

    def is_cache_enabled(self):
        """check if cache is enable for this view"""
        if self.cache_enabled is None:
            return is_cache_enabled()
        return self.cache_enabled

    def can_cache(self):
        """check if content can be set/get from cache"""
        if self.can_edit_object():
            # Never cache for editors
            return False

        return self.is_cache_enabled()

    def can_edit_object(self):
        """check edit perms"""
        can_edit_perm = 'can_edit_{0}'.format(self.varname)
        user = self.request.user
        return user.is_authenticated() and user.is_active and user.has_perm(can_edit_perm, self.object)
        
    def can_access_object(self):
        """check access perms: 404 if not"""
        return True
    
    def can_view_object(self):
        """check view perm: 403 if not"""
        if self.edit_mode:
            return self.can_edit_object()
        else:
            can_view_perm = 'can_view_{0}'.format(self.varname)
            return self.request.user.has_perm(can_view_perm, self.object)
    
    def get_object(self):
        """get the object to edit"""
        lookup = {self.field_lookup: self.kwargs[self.field_lookup]}
        return get_object_or_404(self.model, **lookup)
    
    def get_context_data(self):
        """template context"""
        return {
            'form': self.form if self.edit_mode else None,
            'editable': self.can_edit_object(),
            'edit_mode': self.edit_mode,
            'title': getattr(self.object, 'title', u'{0}'.format(self.object)),
            'coop_cms_edit_url': self.get_edit_url(),
            'coop_cms_cancel_url': self.get_cancel_url(),
            'coop_cms_can_view_callback': self.can_view_object,
            'coop_cms_can_edit_callback': self.can_edit_object,
            self.varname: self.object,
            'raw_' + self.varname: self.object,
        }
        
    def get_edit_url(self):
        """url for object editing"""
        return self.object.get_edit_url()
    
    def get_cancel_url(self):
        """url after cancel editing"""
        if hasattr(self.object, 'get_cancel_url'):
            return self.object.get_cancel_url()
        else:
            return self.object.get_absolute_url()
        
    def get_template(self):
        """get template"""
        return self.template_name
    
    def handle_object_not_found(self):
        """called if object not found"""
        pass

    def get_form_class(self):
        return self.form_class

    def get_form_kwargs(self):
        return {}

    def get_form(self, *args, **kwargs):
        kwargs.update(self.get_form_kwargs())
        form_class = self.get_form_class()
        return form_class(*args, **kwargs)

    def get_cache_key(self, obj):
        language = get_language()
        class_name = obj.__class__
        cache_key = u'{0}-{1}-{2}-{3}'.format(settings.SITE_ID, language, class_name, obj.id)
        return cache_key

    def get(self, request, *args, **kwargs):
        """handle http get -> view"""

        try:
            self.object = self.get_object()
        except Http404:
            return_this = self.handle_object_not_found()
            if return_this:
                return return_this
            else:
                raise
        
        if not self.can_access_object():
            raise Http404
        
        if not self.can_view_object():
            logger.warning("PermissionDenied")
            raise PermissionDenied

        if self.can_cache():
            response_content = cache.get(self.get_cache_key(self.object))
            if response_content:
                return HttpResponse(response_content)
        
        self.form = self.get_form(instance=self.object)
        
        response = render(
            request,
            self.get_template(),
            self.get_context_data()
        )

        if response.status_code == 200 and self.can_cache():
            cache.set(self.get_cache_key(self.object), response.content)

        return response

    def after_save(self, object):
        """called after save"""
        pass
    
    def post(self, request, *args, **kwargs):
        """handle http post -> edit"""
        if not self.edit_mode:
            raise Http404
        
        self.object = self.get_object()
        
        if not self.can_edit_object():
            logger.warning("PermissionDenied")
            raise PermissionDenied

        self.form = self.get_form(request.POST, request.FILES, instance=self.object)

        forms_args = html_editor_utils.extract_forms_args(request.POST)
        inline_html_forms = html_editor_utils.make_forms(forms_args, request.POST)

        if self.form.is_valid() and all([_form.is_valid() for _form in inline_html_forms]):

            if self.is_cache_enabled():
                cache.delete(self.get_cache_key(self.object))

            self.object = self.form.save()
            
            self.after_save(self.object)
            
            if inline_html_forms:
                [_the_form.save() for _the_form in inline_html_forms]

            success_message(request, _(u'The object has been saved properly'))

            return HttpResponseRedirect(self.object.get_absolute_url())
        else:
            error_text = u'<br />'.join(
                [u'{0}'.format(_form.errors) for _form in [self.form]+inline_html_forms if _form.errors]
            )
            error_message(request, _(u'An error occurred: {0}').format(error_text))
            logger.debug(u"error: {0}".format(error_text))
    
        return render(
            request,
            self.get_template(),
            self.get_context_data()
        )


class EditableFormsetView(TemplateView):
    """Base class for editing several objects on the same page"""
    template_name = ""
    model = None
    form_class = None
    extra = 1
    edit_mode = False
    success_url = ""
    success_view_name = ""
    formset = None
    
    def can_edit_objects(self):
        """check edit perms"""
        ct = ContentType.objects.get_for_model(self.model)
        can_edit_perm = '{0}.change_{1}'.format(ct.app_label, ct.model)
        user = self.request.user
        return user.is_authenticated() and user.is_active and user.has_perm(can_edit_perm, None)
        
    def can_view_objects(self):
        """check view perms"""
        if self.edit_mode:
            return self.can_edit_objects()
        return True
    
    def get_context_data(self):
        """template context"""
        context = {
            'editable': True,
            'edit_mode': self.edit_mode,
            'coop_cms_edit_url': self.get_edit_url(),
            'coop_cms_cancel_url': self.get_cancel_url(),
            'coop_cms_can_view_callback': self.can_view_objects,
            'coop_cms_can_edit_callback': self.can_edit_objects,
            'objects': self.get_queryset(),
            'raw_objects': self.get_queryset(),
        }
        if self.edit_mode:
            context['formset'] = self.formset
        return context
        
    def get_form_class(self):
        """get form class"""
        return self.form_class
    
    def get_queryset(self):
        """get objects"""
        return self.model.objects.all()
    
    def get_template(self):
        """get template"""
        return self.template_name
    
    def get_cancel_url(self):
        """url to go after cancel edition"""
        return self.get_success_url()
    
    def get_edit_url(self):
        """url for editing object"""
        return ''
        
    def get_success_url(self):
        """url to go after edition success"""
        return self.success_url or reverse(self.success_view_name) if self.success_view_name else ''
    
    def get_formset_class(self):
        """formset class"""
        return modelformset_factory(self.model, self.get_form_class(), extra=self.extra)
    
    def get_formset(self, *args, **kwargs):
        """formset"""
        Formset = self.get_formset_class()
        return Formset(queryset=self.get_queryset(), *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        """handle http get --> view"""
        if not self.can_view_objects():
            raise PermissionDenied
            
        self.formset = self.get_formset()
        return render(
            request,
            self.get_template(),
            self.get_context_data()
        )
    
    def _pre_save_object(self, form):
        """before saving an object"""
        return True
    
    def _post_save_object(self, obj, form):
        """after saving an object"""
        pass
    
    def post(self, request, *args, **kwargs):
        """handle http post -> edit"""
        if not self.edit_mode:
            raise Http404
    
        if not self.can_edit_objects():
            raise PermissionDenied
        
        self.formset = self.get_formset(request.POST, request.FILES)
        
        forms_args = html_editor_utils.extract_forms_args(request.POST)
        inline_html_forms = html_editor_utils.make_forms(forms_args, request.POST)

        # Handle case where formset post data has value which are not in the queryset
        formset_index_error = False
        try:
            formset_is_valid = self.formset.is_valid()
        except IndexError:
            formset_index_error = True
            formset_is_valid = False

        if formset_is_valid and all([_form.is_valid() for _form in inline_html_forms]):
            for form in self.formset:
                if self._pre_save_object(form):
                    obj = form.save()
                    self._post_save_object(obj, form)
            
            if inline_html_forms:
                [_html_form.save() for _html_form in inline_html_forms]
            
            success_message(request, _(u'The objects have been saved properly'))

            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            if formset_index_error:
                logger.warning(_(u'Index error in formset: some objects may be missing'))
                error_message(request, _(u'An error occured: At least one object is missing. Please try again.'))
                return HttpResponseRedirect(self.get_cancel_url())
            else:
                for _form in self.formset:
                    errors = _form.errors
                    if errors:
                        logger.warning(errors)
        
        return render(
            request,
            self.get_template(),
            self.get_context_data()
        )
