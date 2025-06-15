# -*- coding: utf-8 -*-

from coop_cms.tests import BaseArticleTest
from coop_cms.utils import dehtml


class DehtmlTest(BaseArticleTest):
    
    def test_simple_text(self):
        text = u"This is a simple text"
        self.assertEqual(dehtml(text), text)

    def test_paragraph(self):
        text = u"This is a simple text"
        html_text = u'<p>{0}</p>'.format(text)
        self.assertEqual(dehtml(html_text), text)

    def test_paragraph_inside(self):
        text = u"<h1>This is a title</h1><p>This is a paragraph</p><p>This is another paragraph</p>"
        self.assertEqual(dehtml(text), u"This is a title\n\nThis is a paragraph\n\nThis is another paragraph")

    def test_nbsp(self):
        text = u"This is a simple text"
        html_text = text.replace(u' ', u'&nbsp;')
        self.assertNotEqual(html_text, text)
        self.assertEqual(dehtml(html_text), text)

    def test_gt_lt(self):
        text = u"This is a simple text"
        html_text = u'&gt;' + text + u"&lt;"
        self.assertEqual(dehtml(html_text), u">" + text + u"<")

    def test_special_chars(self):
        text = u"This &ouml;is &auml; simple text&uuml;"
        html_text = u"This &ouml;is &auml; simple text&uuml;"
        self.assertEqual(dehtml(html_text, allow_html_chars=True), text)

    def test_charset_chars(self):
        text = u"à l'Opéra Grand Avignon"
        html_text = u"<p>&agrave; l&#39;Op&eacute;ra Grand Avignon</p>"
        self.assertEqual(dehtml(html_text, allow_html_chars=False), text)

    def test_charset_chars_allowed(self):
        text = u"&agrave; l&#39;Op&eacute;ra Grand Avignon"
        html_text = u"<p>&agrave; l&#39;Op&eacute;ra Grand Avignon</p>"
        self.assertEqual(dehtml(html_text, allow_html_chars=True), text)

    def test_special_chars_two(self):
        text = u"This \xf6is \xe4 simple text\xfc"
        html_text = u"This &ouml;is &auml; simple text&uuml;"
        self.assertEqual(dehtml(html_text), text)
