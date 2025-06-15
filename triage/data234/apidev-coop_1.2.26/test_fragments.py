# -*- coding: utf-8 -*-
"""test fragments feature"""

from django.conf import settings

from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.template import Template, Context

from model_mommy import mommy

from coop_cms.forms import ArticleForm
from coop_cms.models import BaseArticle, Fragment, FragmentType, FragmentFilter
from coop_cms.settings import get_article_class
from coop_cms.tests import BaseTestCase, BeautifulSoup


class BaseFragmentTest(BaseTestCase):
    """base class for fragments test"""

    def __init__(self, *args, **kwargs):
        super(BaseFragmentTest, self).__init__(*args, **kwargs)
        self.user = None

    def setUp(self):
        """before each test"""
        super(BaseFragmentTest, self).setUp()
        self._default_article_templates = settings.COOP_CMS_ARTICLE_TEMPLATES
        settings.COOP_CMS_ARTICLE_TEMPLATES = (
            ('test/article_with_fragments.html', 'Article with fragments'),
            ('test/article_with_fragments_extra_id.html', 'Article with fragments extra id'),
            ('test/article_with_fragments_template.html', 'Article with fragments template'),
        )

    def tearDown(self):
        """after each test"""
        super(BaseFragmentTest, self).tearDown()
        #restore
        settings.COOP_CMS_ARTICLE_TEMPLATES = self._default_article_templates

    def _log_as_editor(self):
        """_log as editor"""
        self.user = user = User.objects.create_user('toto', 'toto@toto.fr', 'toto')

        content_type1 = ContentType.objects.get_for_model(get_article_class())
        content_type2 = ContentType.objects.get_for_model(Fragment)

        for content_type in (content_type1, content_type2):

            perm = 'change_{0}'.format(content_type.model)
            can_edit = Permission.objects.get(content_type=content_type, codename=perm)
            user.user_permissions.add(can_edit)

            perm = 'add_{0}'.format(content_type.model)
            can_add = Permission.objects.get(content_type=content_type, codename=perm)
            user.user_permissions.add(can_add)

        user.is_active = True
        user.save()
        return self.client.login(username='toto', password='toto')

    def _log_as_regular_user(self):
        """log a reguar user"""
        user = User.objects.create_user('titi', 'titi@toto.fr', 'titi')

        #ContentType.objects.get_for_model(get_article_class())

        user.is_active = True
        user.save()
        return self.client.login(username='titi', password='titi')


class FragmentsTest(BaseFragmentTest):
    """Test ragments"""

    editable_field_tpl = '<div class="inline-editable" id="html_editor_html_editor__coop_cms__Fragment__id__{0}__content">' + \
        '{1}</div>\n<input type="hidden" id="html_editor_html_editor__coop_cms__Fragment__id__{0}__content_hidden" ' + \
        'name="html_editor__coop_cms__Fragment__id__{0}__content" value="{1}" />'
    

    def test_fragment_position(self):
        """test position is taken into account"""

        fragment_type1 = mommy.make(FragmentType)
        fragment_type2 = mommy.make(FragmentType)
        
        fragment1 = mommy.make(Fragment, type=fragment_type1)
        fragment2 = mommy.make(Fragment, type=fragment_type1)
        fragment3 = mommy.make(Fragment, type=fragment_type1)
        fragment4 = mommy.make(Fragment, type=fragment_type1)
        
        fragment_g1 = mommy.make(Fragment, type=fragment_type2)
        fragment_g2 = mommy.make(Fragment, type=fragment_type2)
        fragment_g3 = mommy.make(Fragment, type=fragment_type2)
        
        fragment5 = mommy.make(Fragment, type=fragment_type1)
        
        for idx, elt in enumerate([fragment1, fragment2, fragment3, fragment4, fragment5]):
            self.assertEqual(idx+1, elt.position)
        
        for idx, elt in enumerate([fragment_g1, fragment_g2, fragment_g3]):
            self.assertEqual(idx+1, elt.position)
            
    def test_fragment_position_extra_id(self):
        """test position is taken into account when extra id is defined"""

        fragment_type1 = mommy.make(FragmentType)
        fragment_type2 = mommy.make(FragmentType)
        fragment_filter1 = mommy.make(FragmentFilter)
        fragment_filter2 = mommy.make(FragmentFilter)
        
        fragments_1 = [
            mommy.make(Fragment, type=fragment_type1, filter=fragment_filter1),
            mommy.make(Fragment, type=fragment_type1, filter=fragment_filter1),
            mommy.make(Fragment, type=fragment_type1, filter=fragment_filter1),
            mommy.make(Fragment, type=fragment_type1, filter=fragment_filter2),
            mommy.make(Fragment, type=fragment_type1, filter=fragment_filter1),
            mommy.make(Fragment, type=fragment_type1),
            mommy.make(Fragment, type=fragment_type1),
        ]

        fragments_2 = [
            mommy.make(Fragment, type=fragment_type2, filter=fragment_filter1),
            mommy.make(Fragment, type=fragment_type2, filter=fragment_filter2),
            mommy.make(Fragment, type=fragment_type2, filter=fragment_filter2),
        ]

        for idx, elt in enumerate([fragments_1[0], fragments_1[1], fragments_1[2], fragments_1[4]]):
            self.assertEqual(idx+1, elt.position)
            
        for idx, elt in enumerate([fragments_1[3]]):
            self.assertEqual(idx+1, elt.position)
        
        for idx, elt in enumerate([fragments_2[0]]):
            self.assertEqual(idx+1, elt.position)
            
        for idx, elt in enumerate([fragments_2[1], fragments_2[2]]):
            self.assertEqual(idx+1, elt.position)
            
        for idx, elt in enumerate([fragments_1[5], fragments_1[6]]):
            self.assertEqual(idx+1, elt.position)
            
    def test_fragment_position_update(self):
        """test position can be modified"""

        fragment_type1 = mommy.make(FragmentType)
        mommy.make(FragmentType)
        
        fragment1 = mommy.make(Fragment, type=fragment_type1)
        fragment2 = mommy.make(Fragment, type=fragment_type1)
        fragment3 = mommy.make(Fragment, type=fragment_type1)
        
        fragment1.save()
        fragment2.save()
        fragment3.save()
        
        for idx, elt in enumerate([fragment1, fragment2, fragment3]):
            self.assertEqual(idx+1, elt.position)
            
    def test_view_fragments(self):
        """test view fragments"""

        ft_name = u"contacts"
        fragment_type1 = mommy.make(FragmentType, name=ft_name)
        
        fragment1 = mommy.make(Fragment, type=fragment_type1, content="Azerty")
        fragment2 = mommy.make(Fragment, type=fragment_type1, content="Qsdfgh")
        fragment3 = mommy.make(Fragment, type=fragment_type1, content="Wxcvbn")
        
        tpl = Template('{% load coop_edition %}{% coop_fragments ft_name %}')
        html = tpl.render(Context({"ft_name": ft_name}))
        
        positions = [html.find('{0}'.format(f.content)) for f in [fragment1, fragment2, fragment3]]
        for pos in positions:
            self.assertTrue(pos >= 0)
        sorted_positions = positions[:]
        sorted_positions.sort()
        self.assertEqual(positions, sorted_positions)
        
    def test_view_fragments_extra_id_in_edit_mode(self):
        """in edit mode: coop-fragment-type"""
        ft_name = u"contacts"
        fragment_type1 = mommy.make(FragmentType, name=ft_name)
        fragment_filter1 = mommy.make(FragmentFilter, extra_id="1")
        fragment_filter2 = mommy.make(FragmentFilter, extra_id="2")
        
        fragments = [
            mommy.make(Fragment, type=fragment_type1, content="Azerty", filter=fragment_filter1),
            mommy.make(Fragment, type=fragment_type1, content="Qsdfgh", filter=fragment_filter1),
            mommy.make(Fragment, type=fragment_type1, content="Wxcvbn", filter=fragment_filter2),
            mommy.make(Fragment, type=fragment_type1, content="Zsxdrg", filter=None),
        ]

        article = mommy.make(get_article_class(), title='test')
        
        tpl = Template('{% load coop_edition %}{% coop_fragments ft_name x %}')
        html = tpl.render(Context({"ft_name": ft_name, "x": 1, "form": ArticleForm(instance=article)}))
        
        positions = [html.find('{0}'.format(f.content)) for f in [fragments[0], fragments[1]]]
        for pos in positions:
            self.assertTrue(pos >= 0)
        self.assertEqual(positions, sorted(positions))
        
        soup = BeautifulSoup(html)
        ft_tags = soup.select(".coop-fragment-type")
        self.assertEqual(len(ft_tags), 1)
        ft_tag = ft_tags[0]
        self.assertEqual(ft_tag['rel'], str(fragment_type1.id))
        self.assertEqual(ft_tag['data-filter'], str(fragment_filter1.id))

        for frag in [fragments[2], fragments[3]]:
            self.assertTrue(html.find(frag.content) < 0)

    def test_view_fragments_extra_id_in_view_mode(self):
        """in view mode: no coop-fragment-type"""
        ft_name = u"contacts"
        fragment_type1 = mommy.make(FragmentType, name=ft_name)
        fragment_filter1 = mommy.make(FragmentFilter, extra_id="1")
        fragment_filter2 = mommy.make(FragmentFilter, extra_id="2")

        fragments = [
            mommy.make(Fragment, type=fragment_type1, content="Azerty", filter=fragment_filter1),
            mommy.make(Fragment, type=fragment_type1, content="Qsdfgh", filter=fragment_filter1),
            mommy.make(Fragment, type=fragment_type1, content="Wxcvbn", filter=fragment_filter2),
            mommy.make(Fragment, type=fragment_type1, content="Zsxdrg", filter=None),
        ]

        tpl = Template('{% load coop_edition %}{% coop_fragments ft_name x %}')
        html = tpl.render(Context({"ft_name": ft_name, "x": 1}))

        positions = [html.find('{0}'.format(f.content)) for f in [fragments[0], fragments[1]]]
        for pos in positions:
            self.assertTrue(pos >= 0)
        self.assertEqual(positions, sorted(positions))

        soup = BeautifulSoup(html)
        ft_tags = soup.select(".coop-fragment-type")
        self.assertEqual(len(ft_tags), 0)

        for frag in [fragments[2], fragments[3]]:
            self.assertTrue(html.find(frag.content) < 0)

    def test_fragments_with_extra_id(self):
        """test fragments with extra id"""

        ft_name = u"contacts"
        
        tpl = Template('{% load coop_edition %}{% coop_fragments ft_name x %}')
        tpl.render(Context({"ft_name": ft_name, 'x': 2}))
        
        self.assertEqual(FragmentType.objects.count(), 1)
        self.assertEqual(FragmentType.objects.filter(name=ft_name).count(), 1)

        self.assertEqual(FragmentFilter.objects.count(), 1)
        self.assertEqual(FragmentFilter.objects.filter(extra_id='2').count(), 1)
        
    def test_view_fragments_name_as_string(self):
        """test fragments name hardcode in templatetag"""

        fragment_type1 = mommy.make(FragmentType, name="contacts")
        
        fragment1 = mommy.make(Fragment, type=fragment_type1, content="Azerty")
        fragment2 = mommy.make(Fragment, type=fragment_type1, content="Qsdfgh")
        fragment3 = mommy.make(Fragment, type=fragment_type1, content="Wxcvbn")
        
        tpl = Template('{% load coop_edition %}{% coop_fragments "contacts" %}')
        html = tpl.render(Context({"ft_name": "contacts"}))
        
        positions = [html.find('{0}'.format(f.content)) for f in [fragment1, fragment2, fragment3]]
        for pos in positions:
            self.assertTrue(pos >= 0)
        sorted_positions = positions[:]
        sorted_positions.sort()
        self.assertEqual(positions, sorted_positions)
        
    def test_view_fragments_args_as_string(self):
        """test name and extra id hardcoded"""

        fragment_type1 = mommy.make(FragmentType, name="contacts")
        fragment_filter1 = mommy.make(FragmentFilter, extra_id="hello")
        fragment_filter2 = mommy.make(FragmentFilter, extra_id="2")
        
        fragment1 = mommy.make(Fragment, type=fragment_type1, content="Azerty", filter=fragment_filter1)
        fragment2 = mommy.make(Fragment, type=fragment_type1, content="Qsdfgh", filter=fragment_filter1)
        fragment3 = mommy.make(Fragment, type=fragment_type1, content="Wxcvbn", filter=fragment_filter2)
        fragment4 = mommy.make(Fragment, type=fragment_type1, content="Zsxdrg", filter=None)
        
        tpl = Template('{% load coop_edition %}{% coop_fragments "contacts" "hello" %}')
        html = tpl.render(Context({"ft_name": "contacts"}))
        
        positions = [html.find('{0}'.format(f.content)) for f in [fragment1, fragment2]]
        for pos in positions:
            self.assertTrue(pos >= 0)
        sorted_positions = positions[:]
        sorted_positions.sort()
        self.assertEqual(positions, sorted_positions)
        
        for frag in [fragment3, fragment4]:
            self.assertTrue(html.find(frag.content) < 0)
        
    def test_view_fragments_order(self):
        """test fragments displayed in position order"""

        ft_name = u"contacts"
        fragment_type1 = mommy.make(FragmentType, name=ft_name)
        
        fragment1 = mommy.make(Fragment, type=fragment_type1, content="Azerty", position=3)
        fragment2 = mommy.make(Fragment, type=fragment_type1, content="Qsdfgh", position=1)
        fragment3 = mommy.make(Fragment, type=fragment_type1, content="Wxcvbn", position=2)
        
        tpl = Template('{% load coop_edition %}{% coop_fragments ft_name %}')
        html = tpl.render(Context({"ft_name": ft_name}))
        
        positions = [html.find('{0}'.format(f.content)) for f in [fragment2, fragment3, fragment1]]
        for pos in positions:
            self.assertTrue(pos >= 0)
        sorted_positions = positions[:]
        sorted_positions.sort()
        self.assertEqual(positions, sorted_positions)
        
    def test_view_only_specified_fragments(self):
        """test display only right fragements"""

        ft_name = u"contacts"
        fragment_type1 = mommy.make(FragmentType, name=ft_name)
        fragment_type2 = mommy.make(FragmentType, name="AAAA")
        
        fragment1 = mommy.make(Fragment, type=fragment_type1, content="Azerty")
        fragment2 = mommy.make(Fragment, type=fragment_type1, content="Qsdfgh")
        fragment3 = mommy.make(Fragment, type=fragment_type1, content="Wxcvbn")
        
        fragment_g1 = mommy.make(Fragment, type=fragment_type2, content="POIUYT")
        
        tpl = Template('{% load coop_edition %}{% coop_fragments ft_name %}')
        html = tpl.render(Context({"ft_name": ft_name}))
        
        positions = [html.find('{0}'.format(f.content)) for f in [fragment2, fragment3, fragment1]]
        for pos in positions:
            self.assertTrue(pos >= 0)
        
        positions = [html.find('{0}'.format(f.content)) for f in [fragment_g1]]
        for pos in positions:
            self.assertTrue(pos == -1)
            
    def test_view_only_specified_extra_id(self):
        """text extra_id is taken into account"""
        ft_name = u"contacts"
        fragment_type1 = mommy.make(FragmentType, name=ft_name)
        fragment_type2 = mommy.make(FragmentType, name="AAAA")
        
        fragment_filter1 = mommy.make(FragmentFilter, extra_id="hello")
        fragment_filter2 = mommy.make(FragmentFilter, extra_id="2")
        
        fragments = [
            mommy.make(Fragment, type=fragment_type1, content="Azerty", filter=fragment_filter1),
            mommy.make(Fragment, type=fragment_type1, content="Qsdfgh", filter=fragment_filter1),
            mommy.make(Fragment, type=fragment_type1, content="Wxcvbn", filter=fragment_filter2),
            mommy.make(Fragment, type=fragment_type1, content="Zsxdrg", filter=None),
            mommy.make(Fragment, type=fragment_type2, content="POIUYT", filter=fragment_filter1),
        ]
        
        tpl = Template('{% load coop_edition %}{% coop_fragments ft_name "hello" %}')
        html = tpl.render(Context({"ft_name": ft_name}))
        
        positions = [html.find('{0}'.format(f.content)) for f in [fragments[1], fragments[0]]]
        for pos in positions:
            self.assertTrue(pos >= 0)
        
        positions = [html.find('{0}'.format(f.content)) for f in [fragments[4], fragments[2], fragments[3]]]
        for pos in positions:
            self.assertTrue(pos == -1)

    def test_view_extra_id_named_args(self):
        """text extra_id is taken into account extra_id is given as named arg"""
        ft_name = u"contacts"
        fragment_type1 = mommy.make(FragmentType, name=ft_name)
        fragment_type2 = mommy.make(FragmentType, name="AAAA")

        fragment_filter1 = mommy.make(FragmentFilter, extra_id="hello")
        fragment_filter2 = mommy.make(FragmentFilter, extra_id="2")

        fragments = [
            mommy.make(Fragment, type=fragment_type1, content="Azerty", filter=fragment_filter1),
            mommy.make(Fragment, type=fragment_type1, content="Qsdfgh", filter=fragment_filter1),
            mommy.make(Fragment, type=fragment_type1, content="Wxcvbn", filter=fragment_filter2),
            mommy.make(Fragment, type=fragment_type1, content="Zsxdrg", filter=None),
            mommy.make(Fragment, type=fragment_type2, content="POIUYT", filter=fragment_filter1),
        ]

        tpl = Template('{% load coop_edition %}{% coop_fragments ft_name extra_id="hello" %}')
        html = tpl.render(Context({"ft_name": ft_name}))

        positions = [html.find('{0}'.format(f.content)) for f in [fragments[1], fragments[0]]]
        for pos in positions:
            self.assertTrue(pos >= 0)

        positions = [html.find('{0}'.format(f.content)) for f in [fragments[4], fragments[2], fragments[3]]]
        for pos in positions:
            self.assertTrue(pos == -1)

    def test_view_extra_id_named_args_end(self):
        """text extra_id is taken into account extra_id is given as named arg in last position"""
        ft_name = u"contacts"
        fragment_type1 = mommy.make(FragmentType, name=ft_name)
        fragment_type2 = mommy.make(FragmentType, name="AAAA")

        fragment_filter1 = mommy.make(FragmentFilter, extra_id="hello")
        fragment_filter2 = mommy.make(FragmentFilter, extra_id="2")

        fragments = [
            mommy.make(Fragment, type=fragment_type1, content="Azerty", filter=fragment_filter1),
            mommy.make(Fragment, type=fragment_type1, content="Qsdfgh", filter=fragment_filter1),
            mommy.make(Fragment, type=fragment_type1, content="Wxcvbn", filter=fragment_filter2),
            mommy.make(Fragment, type=fragment_type1, content="Zsxdrg", filter=None),
            mommy.make(Fragment, type=fragment_type2, content="POIUYT", filter=fragment_filter1),
        ]

        tpl = Template(
            '{% load coop_edition %}{% coop_fragments ft_name template_name="test/_fragment.html" extra_id="hello" %}'
        )
        html = tpl.render(Context({"ft_name": ft_name}))

        positions = [html.find('{0}'.format(f.content)) for f in [fragments[1], fragments[0]]]
        for pos in positions:
            self.assertTrue(pos >= 0)

        positions = [html.find('{0}'.format(f.content)) for f in [fragments[4], fragments[2], fragments[3]]]
        for pos in positions:
            self.assertTrue(pos == -1)
            
    def test_view_fragments_edit_mode(self):
        """test view in edit mode"""

        ft_name = u"contacts"
        fragment_type1 = mommy.make(FragmentType, name=ft_name)
        fragment_type2 = mommy.make(FragmentType, name="AAAA")
        
        fragments = [
            mommy.make(Fragment, type=fragment_type1, content="Azerty"),
            mommy.make(Fragment, type=fragment_type1, content="Qsdfgh"),
            mommy.make(Fragment, type=fragment_type1, content="Wxcvbn"),
            mommy.make(Fragment, type=fragment_type2, content="POIUYT"),
        ]

        article = mommy.make(get_article_class(), title='test')

        tpl = Template('{% load coop_edition %}{% coop_fragments ft_name %}')
        html = tpl.render(Context({"ft_name": ft_name, "form": ArticleForm(instance=article)}))

        positions = [
            html.find(self.editable_field_tpl.format(f.id, f.content))
            for f in [fragments[0], fragments[1], fragments[2]]
        ]
        for pos in positions:
            self.assertTrue(pos >= 0)
        self.assertEqual(positions, sorted(positions))
        
        positions = [html.find(self.editable_field_tpl.format(f.id, f.content)) for f in [fragments[3]]]
        for pos in positions:
            self.assertTrue(pos == -1)
            
    def test_view_fragments_extra_id_edit_mode(self):
        """test view with extra id in edit mode"""
        ft_name = u"contacts"
        fragment_type1 = mommy.make(FragmentType, name=ft_name)
        fragment_type2 = mommy.make(FragmentType, name="AAAA")
        
        fragment_filter1 = mommy.make(FragmentFilter, extra_id="hello")
        fragment_filter2 = mommy.make(FragmentFilter, extra_id="2")

        article = mommy.make(get_article_class(), title='test')
        
        fragments = [
            mommy.make(Fragment, type=fragment_type1, content="Azerty", filter=fragment_filter1),
            mommy.make(Fragment, type=fragment_type1, content="Qsdfgh", filter=fragment_filter1),
            mommy.make(Fragment, type=fragment_type1, content="Wxcvbn", filter=fragment_filter2),
            mommy.make(Fragment, type=fragment_type1, content="Zsxdrg", filter=None),
            mommy.make(Fragment, type=fragment_type2, content="POIUYT")
        ]
        
        tpl = Template('{% load coop_edition %}{% coop_fragments ft_name "hello" %}')
        html = tpl.render(Context({"ft_name": ft_name, "form": ArticleForm(instance=article)}))

        positions = [
            html.find(self.editable_field_tpl.format(fragment.id, fragment.content))
            for fragment in [fragments[0], fragments[1]]
        ]
        for pos in positions:
            self.assertTrue(pos >= 0)
        self.assertEqual(positions, sorted(positions))
        
        positions = [
            html.find(self.editable_field_tpl.format(fragment.id, fragment.content))
            for fragment in [fragments[4], fragments[2], fragments[3]]
        ]
        for pos in positions:
            self.assertTrue(pos == -1)
            
    def test_fragments_with_template(self):
        """test template_name argument of the template tag"""
        ft_name = u"contacts"
        
        tpl = Template('{% load coop_edition %}{% coop_fragments ft_name template_name="test/_fragment.html" %}')
        html = tpl.render(Context({"ft_name": ft_name}))
        
        self.assertEqual(FragmentType.objects.count(), 1)
        self.assertEqual(FragmentType.objects.filter(name=ft_name).count(), 1)
        
        soup = BeautifulSoup(html)
        self.assertEqual(0, len(soup.select('.panel')))
        
    def test_view_fragments_with_template(self):
        """test view with template_name arguement"""
        ft_name = u"contacts"
        fragment_type = mommy.make(FragmentType, name=ft_name)
        
        mommy.make(Fragment, type=fragment_type)
        
        tpl = Template('{% load coop_edition %}{% coop_fragments ft_name template_name="test/_fragment.html" %}')
        html = tpl.render(Context({"ft_name": ft_name}))
        
        self.assertEqual(FragmentType.objects.count(), 1)
        self.assertEqual(FragmentType.objects.filter(name=ft_name).count(), 1)
        
        soup = BeautifulSoup(html)
        self.assertEqual(1, len(soup.select('.panel')))
        
    def test_view_fragments_template_edit_mode(self):
        """test with template_name in edit_mode"""
        ft_name = u"contacts"
        fragment_type = mommy.make(FragmentType, name=ft_name)
        
        mommy.make(Fragment, type=fragment_type)

        article = mommy.make(get_article_class(), title='test')
        
        tpl = Template('{% load coop_edition %}{% coop_fragments ft_name template_name="test/_fragment.html" %}')
        html = tpl.render(Context({"ft_name": ft_name, "form": ArticleForm(instance=article)}))
        
        self.assertEqual(FragmentType.objects.count(), 1)
        self.assertEqual(FragmentType.objects.filter(name=ft_name).count(), 1)
        
        soup = BeautifulSoup(html)
        self.assertEqual(1, len(soup.select('.panel')))
        self.assertEqual(1, len(soup.select('.panel input')))
        self.assertEqual(1, len(soup.select('.panel .inline-editable')))
    
    def test_view_fragments_with_template2(self):
        """test with another template"""
        ft_name = u"contacts"
        fragment_type = mommy.make(FragmentType, name=ft_name)
        
        mommy.make(Fragment, type=fragment_type)
        mommy.make(Fragment, type=fragment_type)

        tpl = Template('{% load coop_edition %}{% coop_fragments ft_name template_name="test/_fragment.html" %}')
        html = tpl.render(Context({"ft_name": ft_name}))
        
        self.assertEqual(FragmentType.objects.count(), 1)
        self.assertEqual(FragmentType.objects.filter(name=ft_name).count(), 1)
        soup = BeautifulSoup(html)
        self.assertEqual(2, len(soup.select('.panel')))
        
    def test_view_fragments_with_template3(self):
        """test with another other template"""
        ft_name = u"contacts"
        fragment_type = mommy.make(FragmentType, name=ft_name)
        
        mommy.make(Fragment, type=fragment_type)
        mommy.make(Fragment, type=fragment_type)

        article = mommy.make(get_article_class(), title='test')
        
        tpl = Template('{% load coop_edition %}{% coop_fragments ft_name template_name="test/_fragment.html" %}')
        html = tpl.render(Context({"ft_name": ft_name, "form": ArticleForm(instance=article)}))
        
        self.assertEqual(FragmentType.objects.count(), 1)
        self.assertEqual(FragmentType.objects.filter(name=ft_name).count(), 1)
        soup = BeautifulSoup(html)
        self.assertEqual(3, len(soup.select('.panel'))) # 1 extra panel if_cms_edition and fragment index > 0


class FragmentsInArticleTest(BaseFragmentTest):
    """Articles related tests"""

    def _check_article(self, response, data):
        """check page content"""
        for value in data.values():
            self.assertContains(response, value)

    def test_view_article_no_fragments(self):
        """view article with no Fragment"""
        template = settings.COOP_CMS_ARTICLE_TEMPLATES[0][0]
        article = get_article_class().objects.create(title="test", template=template, publication=BaseArticle.PUBLISHED)
        response = self.client.get(article.get_absolute_url())
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, FragmentType.objects.count())
        self.assertEqual("parts", FragmentType.objects.all()[0].name)
        
    def test_view_article_with_fragments(self):
        """view article with Fragment"""
        template = settings.COOP_CMS_ARTICLE_TEMPLATES[0][0]
        
        article = get_article_class().objects.create(title="test", template=template, publication=BaseArticle.PUBLISHED)
        
        fragment_type = mommy.make(FragmentType, name="parts")
        fragment1 = mommy.make(Fragment, type=fragment_type, content="Azertyuiop")
        
        response = self.client.get(article.get_absolute_url())
        
        self.assertEqual(200, response.status_code)
        self.assertContains(response, fragment1.content)
        
    def test_view_article_with_fragments_extra_id(self):
        """view article with Fragment and extra_id"""
        template = settings.COOP_CMS_ARTICLE_TEMPLATES[1][0]
        article = get_article_class().objects.create(title="test", template=template, publication=BaseArticle.PUBLISHED)
        
        fragment_type = mommy.make(FragmentType, name="parts")
        fragment_filter1 = mommy.make(FragmentFilter, extra_id=str(article.id))
        fragment_filter2 = mommy.make(FragmentFilter, extra_id="hello")
        fragment1 = mommy.make(Fragment, type=fragment_type, content="Azertyuiop", filter=fragment_filter1)
        fragment2 = mommy.make(Fragment, type=fragment_type, content="QSDFGHJKLM", filter=fragment_filter2)
        fragment3 = mommy.make(Fragment, type=fragment_type, content="Wxcvbn,;:=", filter=None)
        
        response = self.client.get(article.get_absolute_url())
        self.assertEqual(200, response.status_code)
        self.assertContains(response, fragment1.content)
        self.assertNotContains(response, fragment2.content)
        self.assertNotContains(response, fragment3.content)
        
    def test_view_article_with_fragment_with_css(self):
        """view article with Fragment and css"""

        template = settings.COOP_CMS_ARTICLE_TEMPLATES[0][0]
        article = get_article_class().objects.create(title="test", template=template, publication=BaseArticle.PUBLISHED)
        
        fragment_type = mommy.make(FragmentType, name="parts")
        fragment1 = mommy.make(Fragment, type=fragment_type, content="Azertyuiop", css_class="this-is-my-fragment")
        
        response = self.client.get(article.get_absolute_url())
        self.assertEqual(200, response.status_code)
        self.assertContains(response, fragment1.content)
        
        soup = BeautifulSoup(response.content)
        fragment = soup.select("div."+fragment1.css_class)[0]
        self.assertEqual(fragment1.content, fragment.text)
        
    def test_edit_article_no_fragments(self):
        """edit article with no Fragment"""

        template = settings.COOP_CMS_ARTICLE_TEMPLATES[0][0]
        article = get_article_class().objects.create(title="test", template=template, publication=BaseArticle.PUBLISHED)
        
        data = {"title": 'salut', 'content': 'bonjour!'}
        
        self._log_as_editor()
        response = self.client.post(article.get_edit_url(), data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        self._check_article(response, data)
        
        data = {"title": 'bye', 'content': 'au revoir'}
        response = self.client.post(article.get_edit_url(), data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        self._check_article(response, data)
        
    def test_edit_article_with_fragments(self):
        """edit article with Fragment"""

        template = settings.COOP_CMS_ARTICLE_TEMPLATES[0][0]
        article = get_article_class().objects.create(title="test", template=template, publication=BaseArticle.PUBLISHED)
        
        fragment_type = mommy.make(FragmentType, name="parts")
        fragment1 = mommy.make(Fragment, type=fragment_type, content="Azertyuiop")
        
        new_fragment1_content = u"Qsdfghjklm"
        data = {
            "title": 'salut',
            'content': 'bonjour!',
            'html_editor__coop_cms__Fragment__id__{0}__content'.format(fragment1.id): new_fragment1_content,
        }
        
        self._log_as_editor()
        response = self.client.post(article.get_edit_url(), data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, data['title'])
        self.assertContains(response, data['content'])
        self.assertContains(response, new_fragment1_content)
        
    def test_edit_article_with_fragments_extra_id(self):
        """edit article with Fragment and extra_id"""

        template = settings.COOP_CMS_ARTICLE_TEMPLATES[1][0]
        article = get_article_class().objects.create(title="test", template=template, publication=BaseArticle.PUBLISHED)
        
        fragment_type = mommy.make(FragmentType, name="parts")
        fragment_filter = mommy.make(FragmentFilter, extra_id=str(article.id))
        fragment1 = mommy.make(Fragment, type=fragment_type, content="Azertyuiop", filter=fragment_filter)
        
        new_fragment1_content = u"Qsdfghjklm"
        data = {
            "title": 'salut',
            'content': 'bonjour!',
            'html_editor__coop_cms__Fragment__id__{0}__content'.format(fragment1.id): new_fragment1_content,
        }
        
        self._log_as_editor()
        response = self.client.post(article.get_edit_url(), data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, data['title'])
        self.assertContains(response, data['content'])
        self.assertContains(response, new_fragment1_content)
        
    def test_view_add_fragment(self):
        """can view add fragment"""
        template = settings.COOP_CMS_ARTICLE_TEMPLATES[0][0]
        get_article_class().objects.create(title="test", template=template, publication=BaseArticle.PUBLISHED)
        
        self._log_as_editor()
        
        url = reverse("coop_cms_add_fragment")
        response = self.client.get(url)
        
        self.assertEqual(200, response.status_code)
        
    def test_view_add_fragment_check_filters(self):
        """add fragment check filters"""
        template = settings.COOP_CMS_ARTICLE_TEMPLATES[1][0]
        article = get_article_class().objects.create(title="test", template=template, publication=BaseArticle.PUBLISHED)
        
        self._log_as_editor()
        
        url = article.get_edit_url()
        response = self.client.get(url)
        
        self.assertEqual(200, response.status_code)
        soup = BeautifulSoup(response.content)
        
        ft_tags = soup.select(".coop-fragment-type")
        ft_objs = FragmentType.objects.all()
        ff_objs = FragmentFilter.objects.all()
        
        self.assertEqual(len(ft_tags), 2)
        self.assertEqual(ft_objs.count(), 2)
        self.assertEqual(ff_objs.count(), 1)
        
        for i in range(2):
            self.assertEqual(int(ft_tags[i]["rel"]), ft_objs[i].id)
        
        self.assertEqual(ft_tags[0]["data-filter"], '')
        self.assertEqual(ft_tags[1]["data-filter"], str(ff_objs[0].id))
        
    def test_view_add_fragment_no_filter_check(self):
        """view add fragment"""
        template = settings.COOP_CMS_ARTICLE_TEMPLATES[0][0]
        article = get_article_class().objects.create(title="test", template=template, publication=BaseArticle.PUBLISHED)
        
        self._log_as_editor()
        
        url = article.get_edit_url()
        response = self.client.get(url)
        
        self.assertEqual(200, response.status_code)
        soup = BeautifulSoup(response.content)
        
        ft_tags = soup.select(".coop-fragment-type")
        ft_objs = FragmentType.objects.all()
        ff_objs = FragmentFilter.objects.all()
        
        self.assertEqual(len(ft_tags), 1)
        self.assertEqual(ft_objs.count(), 1)
        self.assertEqual(ff_objs.count(), 0)
        
        self.assertEqual(int(ft_tags[0]["rel"]), ft_objs[0].id)
        
        self.assertEqual(ft_tags[0]["data-filter"], '')
        
    def test_view_add_fragment_permission_denied(self):
        """view add fragment not allowed"""
        template = settings.COOP_CMS_ARTICLE_TEMPLATES[0][0]
        get_article_class().objects.create(title="test", template=template, publication=BaseArticle.PUBLISHED)
        
        url = reverse("coop_cms_add_fragment")
        response = self.client.get(url)
        self.assertEqual(302, response.status_code)
        
        self._log_as_regular_user()
        response = self.client.get(url)
        self.assertEqual(403, response.status_code)
        
    def _add_fragment(self, data, errors_count=0):
        """helper"""
        template = settings.COOP_CMS_ARTICLE_TEMPLATES[0][0]
        get_article_class().objects.create(title="test", template=template, publication=BaseArticle.PUBLISHED)
        
        self._log_as_editor()
        
        url = reverse("coop_cms_add_fragment")
        response = self.client.post(url, data=data, follow=True)
        self.assertEqual(200, response.status_code)
        
        soup = BeautifulSoup(response.content)
        errs = soup.select("ul.errorlist li")
        if errors_count:
            self.assertEqual(errors_count, len(errs))
        else:
            self.assertEqual([], errs)
            expected = u'<script>$.colorbox.close(); window.location=window.location;</script>'.format()
            self.assertEqual(response.content, expected)
        
        return response        
        
    def test_add_fragment(self):
        """add fragment"""
        fragment_type = mommy.make(FragmentType, name="parts")
        data = {
            'type': fragment_type.id,
            'name': 'abcd',
            'position': 0,
            'filter': '',
        }
        
        self._add_fragment(data)
        fragment = Fragment.objects.all()[0]
        
        self.assertEqual(fragment.type, fragment_type)
        self.assertEqual(fragment.name, data['name'])
        self.assertEqual(fragment.css_class, '')
        self.assertEqual(fragment.position, 1)
        self.assertEqual(fragment.filter, None)
        
    def test_add_fragment_filter(self):
        """add fragment with filter"""
        fragment_type = mommy.make(FragmentType, name="parts")
        fragment_filter = mommy.make(FragmentFilter, extra_id="2")
        data = {
            'type': fragment_type.id,
            'name': 'abcd',
            'position': 0,
            'filter': fragment_filter.id
        }
        
        self._add_fragment(data)
        fragment = Fragment.objects.all()[0]
        
        self.assertEqual(fragment.type, fragment_type)
        self.assertEqual(fragment.name, data['name'])
        self.assertEqual(fragment.css_class, '')
        self.assertEqual(fragment.position, 1)
        self.assertEqual(fragment.filter, fragment_filter)
        
    def test_add_fragment_position(self):
        """add fragment with position"""
        fragment_type = mommy.make(FragmentType, name="parts")
        data = {
            'type': fragment_type.id,
            'name': 'abcd',
            'position': 2,
            'filter': '',
        }
        
        self._add_fragment(data)
        fragment = Fragment.objects.all()[0]
        
        self.assertEqual(fragment.type, fragment_type)
        self.assertEqual(fragment.name, data['name'])
        self.assertEqual(fragment.css_class, '')
        self.assertEqual(fragment.position, 2)
        
    def test_add_fragment_invalid_filter(self):
        """add fragment invalid filter"""
        fragment_type = mommy.make(FragmentType, name="parts")
        data = {
            'type': fragment_type.id,
            'name': 'abcd',
            'position': 2,
            'filter': '0',
        }
        
        self._add_fragment(data, 1)
        self.assertEqual(0, Fragment.objects.count())
        
    def test_add_fragment_one_css(self):
        """add fragment css."""
        fragment_type = mommy.make(FragmentType, name="parts", allowed_css_classes="col-1,first-line")
        data = {
            'type': fragment_type.id,
            'name': 'abcd',
            'css_class': ['col-1'],
            'position': 0,
        }

        self._add_fragment(data)
        fragment = Fragment.objects.all()[0]

        self.assertEqual(fragment.type, fragment_type)
        self.assertEqual(fragment.name, data['name'])
        self.assertEqual(fragment.css_class, 'col-1')
        self.assertEqual(fragment.position, 1)

    def test_add_fragment_two_css(self):
        """add fragment css"""
        fragment_type = mommy.make(FragmentType, name="parts", allowed_css_classes="col-1,first-line")
        data = {
            'type': fragment_type.id,
            'name': 'abcd',
            'css_class': ['col-1', 'first-line'],
            'position': 0,
        }

        self._add_fragment(data)
        fragment = Fragment.objects.all()[0]

        self.assertEqual(fragment.type, fragment_type)
        self.assertEqual(fragment.name, data['name'])
        self.assertEqual(fragment.css_class, 'col-1 first-line')
        self.assertEqual(fragment.position, 1)

    def test_add_fragment_invalid_css(self):
        """add fragment css"""
        fragment_type = mommy.make(FragmentType, name="parts", allowed_css_classes="col-1")
        data = {
            'type': fragment_type.id,
            'name': 'abcd',
            'css_class': ['col-1', 'first-line'],
            'position': 0,
        }

        self._add_fragment(data, errors_count=1)

    def test_add_fragment_unknown_css(self):
        """add fragment css"""
        fragment_type = mommy.make(FragmentType, name="parts")
        data = {
            'type': fragment_type.id,
            'name': 'abcd',
            'css_class': 'okidki',
            'position': 0,
        }
        
        self._add_fragment(data, errors_count=1)
            
    def test_view_add_fragment_no_perm(self):
        """add fragment not allowed"""
        template = settings.COOP_CMS_ARTICLE_TEMPLATES[0][0]
        get_article_class().objects.create(title="test", template=template, publication=BaseArticle.PUBLISHED)
        
        fragment_type = mommy.make(FragmentType, name="parts")
        data = {
            'type': fragment_type,
            'name': 'abcd',
            'css_class': 'okidoki',
            'position': 0,
        }
        
        url = reverse("coop_cms_add_fragment")
        response = self.client.post(url, data=data, follow=False)
        self.assertEqual(302, response.status_code)
        next_url = "/accounts/login/?next={0}".format(url)
        self.assertTrue(response['Location'].find(next_url) >= 0)
        
        self._log_as_regular_user()
        response = self.client.post(url, data=data, follow=False)
        self.assertEqual(403, response.status_code)
        
        self.assertEqual(0, Fragment.objects.count())
        
    def test_view_edit_fragments_empty(self):
        """view edit fragment form: no fragments yet"""
        template = settings.COOP_CMS_ARTICLE_TEMPLATES[0][0]
        get_article_class().objects.create(title="test", template=template, publication=BaseArticle.PUBLISHED)
        
        self._log_as_editor()
        
        url = reverse("coop_cms_edit_fragments")
        response = self.client.get(url)
        
        self.assertEqual(200, response.status_code)
        
    def test_view_edit_fragments(self):
        """view edit fragment form"""

        template = settings.COOP_CMS_ARTICLE_TEMPLATES[0][0]
        get_article_class().objects.create(title="test", template=template, publication=BaseArticle.PUBLISHED)
        
        fragment1 = mommy.make(Fragment, name="azerty")
        fragment2 = mommy.make(Fragment, name="qwerty")
        
        self._log_as_editor()
        
        url = reverse("coop_cms_edit_fragments")
        response = self.client.get(url)
        
        self.assertEqual(200, response.status_code)
        self.assertContains(response, fragment1.name)
        self.assertContains(response, fragment2.name)
        
    def test_view_edit_fragments_perms(self):
        """view edit fragment form: not allowed"""

        template = settings.COOP_CMS_ARTICLE_TEMPLATES[0][0]
        get_article_class().objects.create(title="test", template=template, publication=BaseArticle.PUBLISHED)
        
        url = reverse("coop_cms_edit_fragments")
        response = self.client.get(url)
        
        self.assertEqual(302, response.status_code)
        
        self._log_as_regular_user()
        response = self.client.get(url)
        self.assertEqual(403, response.status_code)    
    
    def test_edit_fragment(self):
        """edit fragment"""

        template = settings.COOP_CMS_ARTICLE_TEMPLATES[0][0]
        get_article_class().objects.create(title="test", template=template, publication=BaseArticle.PUBLISHED)
        
        fragment_type1 = mommy.make(FragmentType)
        fragment_type2 = mommy.make(FragmentType)
        fragment1 = mommy.make(Fragment, name="azerty", type=fragment_type1)
        fragment2 = mommy.make(Fragment, name="qwerty", type=fragment_type2)
        
        data = {
            'form-0-id': fragment1.id,
            'form-0-type': fragment1.type.id,
            'form-0-name': fragment1.name+"!",
            'form-0-css_class': [],
            'form-0-position': 5,
            'form-0-delete_me': False,
            
            'form-1-id': fragment2.id,
            'form-1-type': fragment2.type.id,
            'form-1-name': fragment2.name+"+",
            'form-1-css_class': [],
            'form-1-position': 2,
            'form-1-delete_me': False,
            
            'form-TOTAL_FORMS': 2,
            'form-INITIAL_FORMS': 2,
            'form-MAX_NUM_FORMS': 2
        }
        
        self._log_as_editor()
        
        url = reverse("coop_cms_edit_fragments")
        response = self.client.post(url, data=data, follow=True)
        self.assertEqual(200, response.status_code)
        
        soup = BeautifulSoup(response.content)
        errs = soup.select("ul.errorlist li")
        self.assertEqual([], errs)
        
        expected = u'<script>$.colorbox.close(); window.location=window.location;</script>'.format()
        self.assertEqual(response.content, expected)
        
        self.assertEqual(2, Fragment.objects.count())
        fragment1 = Fragment.objects.get(id=fragment1.id)
        fragment2 = Fragment.objects.get(id=fragment2.id)

        self.assertEqual(fragment1.type, fragment_type1)
        self.assertEqual(fragment1.name, "azerty!")
        self.assertEqual(fragment1.css_class, "")
        self.assertEqual(fragment1.position, 5)

        self.assertEqual(fragment2.type, fragment_type2)
        self.assertEqual(fragment2.name, "qwerty+")
        self.assertEqual(fragment2.css_class, "")
        self.assertEqual(fragment2.position, 2)

    def test_edit_fragment_css_allowed(self):
        """edit fragment: css is allowed"""

        template = settings.COOP_CMS_ARTICLE_TEMPLATES[0][0]
        get_article_class().objects.create(title="test", template=template, publication=BaseArticle.PUBLISHED)

        fragment_type1 = mommy.make(FragmentType, allowed_css_classes="oups")
        fragment_type2 = mommy.make(FragmentType, allowed_css_classes="aaa,bbb")
        fragment1 = mommy.make(Fragment, name="azerty", type=fragment_type1)
        fragment2 = mommy.make(Fragment, name="qwerty", type=fragment_type2)

        data = {
            'form-0-id': fragment1.id,
            'form-0-type': fragment1.type.id,
            'form-0-name': fragment1.name+"!",
            'form-0-css_class': ["oups"],
            'form-0-position': 5,
            'form-0-delete_me': False,

            'form-1-id': fragment2.id,
            'form-1-type': fragment2.type.id,
            'form-1-name': fragment2.name+"+",
            'form-1-css_class': ["aaa", "bbb"],
            'form-1-position': 2,
            'form-1-delete_me': False,

            'form-TOTAL_FORMS': 2,
            'form-INITIAL_FORMS': 2,
            'form-MAX_NUM_FORMS': 2
        }

        self._log_as_editor()

        url = reverse("coop_cms_edit_fragments")
        response = self.client.post(url, data=data, follow=True)
        self.assertEqual(200, response.status_code)

        soup = BeautifulSoup(response.content)
        errs = soup.select("ul.errorlist li")
        self.assertEqual([], errs)

        expected = u'<script>$.colorbox.close(); window.location=window.location;</script>'.format()
        self.assertEqual(response.content, expected)

        self.assertEqual(2, Fragment.objects.count())
        fragment1 = Fragment.objects.get(id=fragment1.id)
        fragment2 = Fragment.objects.get(id=fragment2.id)

        self.assertEqual(fragment1.type, fragment_type1)
        self.assertEqual(fragment1.name, "azerty!")
        self.assertEqual(fragment1.css_class, "oups")
        self.assertEqual(fragment1.position, 5)

        self.assertEqual(fragment2.type, fragment_type2)
        self.assertEqual(fragment2.name, "qwerty+")
        self.assertEqual(fragment2.css_class, "aaa bbb")
        self.assertEqual(fragment2.position, 2)

    def test_edit_fragment_css_not_allowed(self):
        """edit fragment: invalid css"""

        template = settings.COOP_CMS_ARTICLE_TEMPLATES[0][0]
        get_article_class().objects.create(title="test", template=template, publication=BaseArticle.PUBLISHED)
        
        fragment_type1 = mommy.make(FragmentType, allowed_css_classes="")
        fragment_type2 = mommy.make(FragmentType)
        fragment1 = mommy.make(Fragment, name="azerty", type=fragment_type1)
        fragment2 = mommy.make(Fragment, name="qwerty", type=fragment_type2)
        
        data = {
            'form-0-id': fragment1.id,
            'form-0-type': fragment1.type.id,
            'form-0-name': fragment1.name+"!",
            'form-0-css_class': "oups",
            'form-0-position': 5,
            'form-0-delete_me': False,
            
            'form-1-id': fragment2.id,
            'form-1-type': fragment2.type.id,
            'form-1-name': fragment2.name+"+",
            'form-1-css_class': "aaa",
            'form-1-position': 2,
            'form-1-delete_me': False,
            
            'form-TOTAL_FORMS': 2,
            'form-INITIAL_FORMS': 2,
            'form-MAX_NUM_FORMS': 2
        }
        
        self._log_as_editor()
        
        url = reverse("coop_cms_edit_fragments")
        response = self.client.post(url, data=data, follow=True)
        self.assertEqual(200, response.status_code)
        
        soup = BeautifulSoup(response.content)
        errs = soup.select("ul.errorlist li")
        self.assertEqual(2, len(errs))
        
        self.assertEqual(2, Fragment.objects.count())
        fragment1 = Fragment.objects.get(id=fragment1.id)
        fragment2 = Fragment.objects.get(id=fragment2.id)

        self.assertEqual(fragment1.type, fragment_type1)
        self.assertEqual(fragment1.name, "azerty")
        self.assertEqual(fragment1.css_class, "")

        self.assertEqual(fragment2.type, fragment_type2)
        self.assertEqual(fragment2.name, "qwerty")
        self.assertEqual(fragment2.css_class, "")

    def test_edit_fragment_css_not_allowed2(self):
        """edit fragment: invalid css for only 1"""

        template = settings.COOP_CMS_ARTICLE_TEMPLATES[0][0]
        get_article_class().objects.create(title="test", template=template, publication=BaseArticle.PUBLISHED)

        fragment_type1 = mommy.make(FragmentType, allowed_css_classes="aaa")
        fragment_type2 = mommy.make(FragmentType)
        fragment1 = mommy.make(Fragment, name="azerty", type=fragment_type1)
        fragment2 = mommy.make(Fragment, name="qwerty", type=fragment_type2)

        data = {
            'form-0-id': fragment1.id,
            'form-0-type': fragment1.type.id,
            'form-0-name': fragment1.name+"!",
            'form-0-css_class': "oups",
            'form-0-position': 5,
            'form-0-delete_me': False,

            'form-1-id': fragment2.id,
            'form-1-type': fragment2.type.id,
            'form-1-name': fragment2.name+"+",
            'form-1-css_class': "aaa",
            'form-1-position': 2,
            'form-1-delete_me': False,

            'form-TOTAL_FORMS': 2,
            'form-INITIAL_FORMS': 2,
            'form-MAX_NUM_FORMS': 2
        }

        self._log_as_editor()

        url = reverse("coop_cms_edit_fragments")
        response = self.client.post(url, data=data, follow=True)
        self.assertEqual(200, response.status_code)

        soup = BeautifulSoup(response.content)
        errs = soup.select("ul.errorlist li")
        self.assertEqual(2, len(errs))

        self.assertEqual(2, Fragment.objects.count())
        fragment1 = Fragment.objects.get(id=fragment1.id)
        fragment2 = Fragment.objects.get(id=fragment2.id)

        self.assertEqual(fragment1.type, fragment_type1)
        self.assertEqual(fragment1.name, "azerty")
        self.assertEqual(fragment1.css_class, "")

        self.assertEqual(fragment2.type, fragment_type2)
        self.assertEqual(fragment2.name, "qwerty")
        self.assertEqual(fragment2.css_class, "")

    def test_edit_fragment_css_not_allowed3(self):
        """edit fragment: one invalid css """

        template = settings.COOP_CMS_ARTICLE_TEMPLATES[0][0]
        get_article_class().objects.create(title="test", template=template, publication=BaseArticle.PUBLISHED)

        fragment_type1 = mommy.make(FragmentType, allowed_css_classes="aaa,bbb")
        fragment_type2 = mommy.make(FragmentType)
        fragment1 = mommy.make(Fragment, name="azerty", type=fragment_type1)
        fragment2 = mommy.make(Fragment, name="qwerty", type=fragment_type2)

        data = {
            'form-0-id': fragment1.id,
            'form-0-type': fragment1.type.id,
            'form-0-name': fragment1.name+"!",
            'form-0-css_class': ["bbb", "oups"],
            'form-0-position': 5,
            'form-0-delete_me': False,

            'form-1-id': fragment2.id,
            'form-1-type': fragment2.type.id,
            'form-1-name': fragment2.name+"+",
            'form-1-css_class': "aaa",
            'form-1-position': 2,
            'form-1-delete_me': False,

            'form-TOTAL_FORMS': 2,
            'form-INITIAL_FORMS': 2,
            'form-MAX_NUM_FORMS': 2
        }

        self._log_as_editor()

        url = reverse("coop_cms_edit_fragments")
        response = self.client.post(url, data=data, follow=True)
        self.assertEqual(200, response.status_code)

        soup = BeautifulSoup(response.content)
        errs = soup.select("ul.errorlist li")
        self.assertEqual(2, len(errs))

        self.assertEqual(2, Fragment.objects.count())
        fragment1 = Fragment.objects.get(id=fragment1.id)
        fragment2 = Fragment.objects.get(id=fragment2.id)

        self.assertEqual(fragment1.type, fragment_type1)
        self.assertEqual(fragment1.name, "azerty")
        self.assertEqual(fragment1.css_class, "")

        self.assertEqual(fragment2.type, fragment_type2)
        self.assertEqual(fragment2.name, "qwerty")
        self.assertEqual(fragment2.css_class, "")

    def test_edit_fragment_delete(self):
        """delete fragment"""
        template = settings.COOP_CMS_ARTICLE_TEMPLATES[0][0]
        get_article_class().objects.create(title="test", template=template, publication=BaseArticle.PUBLISHED)
        
        fragment_type1 = mommy.make(FragmentType)
        fragment_type2 = mommy.make(FragmentType)
        fragment1 = mommy.make(Fragment, name="azerty", type=fragment_type1)
        fragment2 = mommy.make(Fragment, name="qwerty", type=fragment_type2)
        
        data = {
            'form-0-id': fragment1.id,
            'form-0-type': fragment1.type.id,
            'form-0-name': fragment1.name+"!",
            'form-0-css_class': "",
            'form-0-position': 5,
            'form-0-delete_me': False,
            
            'form-1-id': fragment2.id,
            'form-1-type': fragment2.type.id,
            'form-1-name': fragment2.name+"+",
            'form-1-css_class': "",
            'form-1-position': 2,
            'form-1-delete_me': True,
            
            'form-TOTAL_FORMS': 2,
            'form-INITIAL_FORMS': 2,
            'form-MAX_NUM_FORMS': 2
        }
        
        self._log_as_editor()
        
        url = reverse("coop_cms_edit_fragments")
        response = self.client.post(url, data=data, follow=True)
        self.assertEqual(200, response.status_code)
        
        soup = BeautifulSoup(response.content)
        errs = soup.select("ul.errorlist li")
        self.assertEqual([], errs)
        
        expected = u'<script>$.colorbox.close(); window.location=window.location;</script>'.format()
        self.assertEqual(response.content, expected)
        
        self.assertEqual(1, Fragment.objects.count())
        fragment1 = Fragment.objects.get(id=fragment1.id)
        self.assertEqual(Fragment.objects.filter(id=fragment2.id).count(), 0)

        self.assertEqual(fragment1.type, fragment_type1)
        self.assertEqual(fragment1.name, "azerty!")
        self.assertEqual(fragment1.css_class, "")
        self.assertEqual(fragment1.position, 5)
        
    def test_edit_fragment_invalid_position(self):
        """edit fragment: invalid pos"""

        template = settings.COOP_CMS_ARTICLE_TEMPLATES[0][0]
        get_article_class().objects.create(title="test", template=template, publication=BaseArticle.PUBLISHED)
        
        fragment_type1 = mommy.make(FragmentType)
        fragment_type2 = mommy.make(FragmentType)
        fragment1 = mommy.make(Fragment, name="azerty", type=fragment_type1)
        fragment2 = mommy.make(Fragment, name="qwerty", type=fragment_type2)
        
        data = {
            'form-0-id': fragment1.id,
            'form-0-type': fragment1.type.id,
            'form-0-name': fragment1.name+"!",
            'form-0-css_class': "",
            'form-0-position': "AAA",
            'form-0-delete_me': False,
            
            'form-1-id': fragment2.id,
            'form-1-type': fragment2.type.id,
            'form-1-name': fragment2.name+"+",
            'form-1-css_class': "",
            'form-1-position': 2,
            'form-1-delete_me': False,
            
            'form-TOTAL_FORMS': 2,
            'form-INITIAL_FORMS': 2,
            'form-MAX_NUM_FORMS': 2
        }
        
        self._log_as_editor()
        
        url = reverse("coop_cms_edit_fragments")
        response = self.client.post(url, data=data, follow=True)
        self.assertEqual(200, response.status_code)
        
        soup = BeautifulSoup(response.content)
        errs = soup.select("ul.errorlist li")
        self.assertEqual(1, len(errs))
    
    def test_edit_fragment_empty_name(self):
        """edit fragment empty name"""

        template = settings.COOP_CMS_ARTICLE_TEMPLATES[0][0]
        get_article_class().objects.create(title="test", template=template, publication=BaseArticle.PUBLISHED)
        
        fragment_type1 = mommy.make(FragmentType)
        fragment_type2 = mommy.make(FragmentType)
        fragment1 = mommy.make(Fragment, name="azerty", type=fragment_type1)
        fragment2 = mommy.make(Fragment, name="qwerty", type=fragment_type2)
        
        data = {
            'form-0-id': fragment1.id,
            'form-0-type': fragment1.type.id,
            'form-0-name': "",
            'form-0-css_class': "",
            'form-0-position': 1,
            'form-0-delete_me': False,
            
            'form-1-id': fragment2.id,
            'form-1-type': fragment2.type.id,
            'form-1-name': fragment2.name+"+",
            'form-1-css_class': "",
            'form-1-position': 2,
            'form-1-delete_me': False,
            
            'form-TOTAL_FORMS': 2,
            'form-INITIAL_FORMS': 2,
            'form-MAX_NUM_FORMS': 2
        }
        
        self._log_as_editor()
        
        url = reverse("coop_cms_edit_fragments")
        response = self.client.post(url, data=data, follow=True)
        self.assertEqual(200, response.status_code)
        
        soup = BeautifulSoup(response.content)
        errs = soup.select("ul.errorlist li")
        self.assertEqual(1, len(errs))

    def test_edit_fragment_permission_denied(self):
        """edit fragment: not allowed"""

        template = settings.COOP_CMS_ARTICLE_TEMPLATES[0][0]
        get_article_class().objects.create(title="test", template=template, publication=BaseArticle.PUBLISHED)
        
        fragment_type1 = mommy.make(FragmentType)
        fragment_type2 = mommy.make(FragmentType)
        fragment1 = mommy.make(Fragment, name="azerty", type=fragment_type1)
        fragment2 = mommy.make(Fragment, name="qwerty", type=fragment_type2)
        
        data = {
            'form-0-id': fragment1.id,
            'form-0-type': fragment1.type.id,
            'form-0-name': fragment1.name+"!",
            'form-0-css_class': "",
            'form-0-position': 5,
            'form-0-delete_me': False,
            
            'form-1-id': fragment2.id,
            'form-1-type': fragment2.type.id,
            'form-1-name': fragment2.name+"+",
            'form-1-css_class': "",
            'form-1-position': 2,
            'form-1-delete_me': False,
            
            'form-TOTAL_FORMS': 2,
            'form-INITIAL_FORMS': 2,
            'form-MAX_NUM_FORMS': 2
        }
        
        url = reverse("coop_cms_edit_fragments")
        response = self.client.post(url, data=data, follow=False)
        
        self.assertEqual(302, response.status_code)
        
        self.assertEqual(2, Fragment.objects.count())
        fragment1 = Fragment.objects.get(id=fragment1.id)
        fragment2 = Fragment.objects.get(id=fragment2.id)

        self.assertEqual(fragment1.type, fragment_type1)
        self.assertEqual(fragment1.name, "azerty")
        self.assertEqual(fragment1.css_class, "")
        self.assertEqual(fragment1.position, 1)
    
        self.assertEqual(fragment2.type, fragment_type2)
        self.assertEqual(fragment2.name, "qwerty")
        self.assertEqual(fragment2.css_class, "")
        self.assertEqual(fragment2.position, 1)

        self._log_as_regular_user()
        response = self.client.post(url, data=data)
        self.assertEqual(403, response.status_code)  
        
        self.assertEqual(2, Fragment.objects.count())
        fragment1 = Fragment.objects.get(id=fragment1.id)
        fragment2 = Fragment.objects.get(id=fragment2.id)

        self.assertEqual(fragment1.type, fragment_type1)
        self.assertEqual(fragment1.name, "azerty")
        self.assertEqual(fragment1.css_class, "")
        self.assertEqual(fragment1.position, 1)
    
        self.assertEqual(fragment2.type, fragment_type2)
        self.assertEqual(fragment2.name, "qwerty")
        self.assertEqual(fragment2.css_class, "")
        self.assertEqual(fragment2.position, 1)
