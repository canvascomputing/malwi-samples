# -*- coding: utf-8 -*-
"""fragments are block of html which can be dynamically added"""

from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import PermissionDenied
from django.forms.models import modelformset_factory
from django.shortcuts import render
from django.utils.translation import ugettext as _

from colorbox.decorators import popup_close

from coop_cms.forms.fragments import AddFragmentForm, EditFragmentForm
from coop_cms import models


@login_required
@popup_close
def add_fragment(request):
    """add a fragment to the current template"""

    content_type = ContentType.objects.get_for_model(models.Fragment)
    perm = '{0}.add_{1}'.format(content_type.app_label, content_type.model)
    if not request.user.has_perm(perm):
        raise PermissionDenied

    if request.method == "POST":
        form = AddFragmentForm(request.POST)
        if form.is_valid():
            form.save()
            # popup_close decorator will close and refresh
            return None
    else:
        form = AddFragmentForm()

    context_dict = {
        'form': form,
    }

    return render(
        request,
        'coop_cms/popup_add_fragment.html',
        context_dict
    )


@login_required
@popup_close
def edit_fragments(request):
    """edit fragments of the current template"""

    content_type = ContentType.objects.get_for_model(models.Fragment)
    perm = '{0}.add_{1}'.format(content_type.app_label, content_type.model)
    if not request.user.has_perm(perm):
        raise PermissionDenied

    edit_fragment_formset = modelformset_factory(models.Fragment, EditFragmentForm, extra=0)

    if request.method == "POST":
        formset = edit_fragment_formset(request.POST, queryset=models.Fragment.objects.all())
        if formset.is_valid():
            formset.save()
            # popup_close decorator will close and refresh
            return None
    else:
        formset = edit_fragment_formset(queryset=models.Fragment.objects.all())

    context_dict = {
        'form': formset,
        'title': _(u"Edit fragments of this template?"),
    }

    return render(
        request,
        'coop_cms/popup_edit_fragments.html',
        context_dict
    )
