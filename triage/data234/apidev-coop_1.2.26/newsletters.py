# -*- coding: utf-8 -*-
"""newsleters"""

from datetime import datetime
import sys
from tempfile import NamedTemporaryFile

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.encoding import smart_text
from django.utils.translation import ugettext as _
from django.views.generic import View

from colorbox.decorators import popup_redirect
try:
    from wkhtmltopdf.utils import convert_to_pdf, make_absolute_paths
    from wkhtmltopdf.views import PDFResponse
except ImportError:
    pass

from coop_cms.forms.newsletters import NewsletterSchedulingForm, NewsletterTemplateForm
from coop_cms import models
from coop_cms.generic_views import EditableObjectView
from coop_cms.logger import logger
from coop_cms.settings import get_newsletter_form, get_newsletter_settings_form
from coop_cms.utils import send_newsletter, slugify


@login_required
@popup_redirect
def newsletter_settings(request, newsletter_id=None):
    """edit or created newsletter"""

    if newsletter_id:
        newsletter = get_object_or_404(models.Newsletter, id=newsletter_id)
    else:
        newsletter = None

    form_class = get_newsletter_settings_form()

    if request.method == "POST":
        form = form_class(request.user, request.POST, instance=newsletter)
        if form.is_valid():
            newsletter = form.save()
            return HttpResponseRedirect(newsletter.get_absolute_url())
    else:
        form = form_class(request.user, instance=newsletter)

    return render(
        request,
        'coop_cms/popup_newsletter_settings.html',
        locals()
    )


@login_required
@popup_redirect
def change_newsletter_template(request, newsletter_id):
    """change newsletter template"""
    newsletter = get_object_or_404(models.Newsletter, id=newsletter_id)

    if not request.user.has_perm('can_edit_newsletter', newsletter):
        raise PermissionDenied

    if request.method == "POST":
        form = NewsletterTemplateForm(newsletter, request.user, request.POST)
        if form.is_valid():
            newsletter.template = form.cleaned_data['template']
            newsletter.save()
            return HttpResponseRedirect(newsletter.get_edit_url())
    else:
        form = NewsletterTemplateForm(newsletter, request.user)

    return render(
        request,
        'coop_cms/popup_change_newsletter_template.html',
        {'form': form, 'newsletter': newsletter}
    )


@login_required
@popup_redirect
def test_newsletter(request, newsletter_id):
    """test newsletter"""
    newsletter = get_object_or_404(models.Newsletter, id=newsletter_id)

    if not request.user.has_perm('can_edit_newsletter', newsletter):
        raise PermissionDenied

    dests = settings.COOP_CMS_TEST_EMAILS

    if request.method == "POST":
        try:
            nb_sent = send_newsletter(newsletter, dests)

            messages.add_message(
                request, messages.SUCCESS,
                _(u"The test email has been sent to {0} addresses: {1}").format(nb_sent, u', '.join(dests))
            )
            return HttpResponseRedirect(newsletter.get_absolute_url())

        except Exception:
            messages.add_message(request, messages.ERROR, _(u"An error occured! Please contact your support."))
            logger.error(
                'Internal Server Error: {0}'.format(request.path),
                exc_info=sys.exc_info,
                extra={
                    'status_code': 500,
                    'request': request
                }
            )
            return HttpResponseRedirect(newsletter.get_absolute_url())

    return render(
        request,
        'coop_cms/popup_test_newsletter.html',
        {'newsletter': newsletter, 'dests': dests}
    )


@login_required
@popup_redirect
def schedule_newsletter_sending(request, newsletter_id):
    """schedule sending"""
    newsletter = get_object_or_404(models.Newsletter, id=newsletter_id)
    instance = models.NewsletterSending(newsletter=newsletter)

    if request.method == "POST":
        form = NewsletterSchedulingForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(newsletter.get_edit_url())
    else:
        form = NewsletterSchedulingForm(instance=instance, initial={'scheduling_dt': datetime.now()})

    return render(
        request,
        'coop_cms/popup_schedule_newsletter_sending.html',
        {'newsletter': newsletter, 'form': form}
    )


class NewsletterView(EditableObjectView):
    """newsletter view for edition"""
    model = models.Newsletter
    form_class = get_newsletter_form()
    field_lookup = "id"
    varname = "newsletter"
    editable = True

    def can_view_object(self):
        if self.object.is_public:
            return True
        return super(NewsletterView, self).can_edit_object()

    def get_context_data(self):
        """context"""
        context_data = super(NewsletterView, self).get_context_data()
        context_data.update({
            'title': self.object.subject,
            'by_email': self.request.GET.get('by_email', False),
            'editable': self.editable,
        })
        return context_data

    def after_save(self, article):
        """after save"""
        pass

    def get_template(self):
        """get template"""
        return self.object.get_template_name()


class NewsletterPdfView(View):
    """convert the newsletter to pdf"""

    def get(self, request, *args, **kwargs):
        """handle GET request : convert newsletter to pdf"""

        newsletter = get_object_or_404(models.Newsletter, id=self.kwargs['id'])

        # Call the newsletter view as a regular function
        newsletter_view = NewsletterView.as_view(editable=False)
        response = newsletter_view(request, id=newsletter.id)

        # Save the Html into a temporary file
        temp_file = self.save_to_temporary_file(response.content)

        # convert this file to pdf
        pdf_content = convert_to_pdf(
            filename=temp_file.name,
            header_filename=None,
            footer_filename=None,
            cmd_options={}
        )

        # Generate name of the pdf file
        filename = u'newsletter_{0}.pdf'.format(slugify(newsletter.subject))

        # returns PDF response
        return PDFResponse(pdf_content, show_content_in_browser=False, filename=filename)

    def save_to_temporary_file(self, content):
        """
        put content into a temporary file
        Inspired by django-wkhtmltopdf
        """

        # Turn path to absolute
        content = smart_text(content)
        content = make_absolute_paths(content)

        try:
            # Python3 has 'buffering' arg instead of 'bufsize'
            temp_file = NamedTemporaryFile(
                mode='w+b', buffering=-1, suffix='.html', prefix='tmp', dir=None, delete=True)
        except TypeError:
            temp_file = NamedTemporaryFile(
                mode='w+b', bufsize=-1, suffix='.html', prefix='tmp', dir=None, delete=True
            )

        try:
            temp_file.write(content.encode('utf-8'))
            temp_file.flush()
            return temp_file
        except:
            # Clean-up tempfile if an Exception is raised.
            temp_file.close()
            raise
