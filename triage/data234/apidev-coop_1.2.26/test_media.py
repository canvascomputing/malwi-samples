# -*- coding: utf-8 -*-
"""media library unit testing"""

from django.conf import settings

import json
from datetime import datetime
from StringIO import StringIO
from unittest import skipIf

from PIL import Image as PilImage

from django.core.files import File
from django.core.urlresolvers import reverse
from django.template import Template, Context
from django.template.base import TemplateSyntaxError
from django.test.utils import override_settings

from model_mommy import mommy
if 'photologue' in settings.INSTALLED_APPS:
    from photologue.models import Photo, Gallery

from coop_cms.models import ArticleCategory, Document, Image, ImageSize, MediaFilter
from coop_cms.settings import get_article_class
from coop_cms.tests import BaseArticleTest, BaseTestCase, BeautifulSoup, MediaBaseTestCase


class ImageUploadTest(MediaBaseTestCase):
    """Image upload tests"""
    
    def test_view_form_no_filters(self):
        """view upload image when no filters"""
        self._log_as_mediamgr(perm=self._permission("add", Image))
        url = reverse('coop_cms_upload_image')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content)
        id_copyright = soup.select("input#id_copyright")
        self.assertEqual(1, len(id_copyright))
        id_size = soup.select("input#id_size")
        self.assertEqual(1, len(id_size))
        self.assertEqual("hidden", id_size[0]["type"])
        id_filters = soup.select("input#id_filters")
        self.assertEqual(1, len(id_filters))
        self.assertEqual("hidden", id_filters[0]["type"])
        
    def test_view_form_no_sizes(self):
        """view upload image when no sizes"""
        self._log_as_mediamgr(perm=self._permission("add", Image))
        url = reverse('coop_cms_upload_image')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content)
        id_size = soup.select("input#id_size")
        self.assertEqual(1, len(id_size))
        self.assertEqual("hidden", id_size[0]["type"])

    def test_view_form_with_filters(self):
        """view upload image when filters"""
        mommy.make(MediaFilter, name="icons")
        mommy.make(MediaFilter, name="big-images")
        
        self._log_as_mediamgr(perm=self._permission("add", Image))
        url = reverse('coop_cms_upload_image')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content)
        id_filters = soup.select("select#id_filters option")
        self.assertEqual(2, len(id_filters))
    
    def test_view_form_with_sizes(self):
        """view upload image when sizes configured"""
        size1 = mommy.make(ImageSize, name="icons")
        size2 = mommy.make(ImageSize, name="big-images")
        
        self._log_as_mediamgr(perm=self._permission("add", Image))
        url = reverse('coop_cms_upload_image')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content)
        id_sizes = soup.select("select#id_size option")
        self.assertEqual(['', str(size1.id), str(size2.id)], [x["value"] for x in id_sizes])
        
    def test_post_form_no_filters(self):
        """upload image when no filters"""
        self._log_as_mediamgr(perm=self._permission("add", Image))
        url = reverse('coop_cms_upload_image')
        
        data = {
            'image': self._get_file("unittest1.png"),
            'descr': 'a test file',
            'filters': ''
        }
        
        response = self.client.post(url, data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, 'close_popup_and_media_slide')
        
        images = Image.objects.all()
        self.assertEquals(1, images.count())
        self.assertEqual(images[0].name, data['descr'])
        self.assertEqual(images[0].filters.count(), 0)
        self.assertEqual(images[0].size, None)
        file_ = images[0].file
        file_.open('rb')
        self.assertEqual(file_.read(), self._get_file("unittest1.png").read())
        
    def test_post_form_size(self):
        """upload image with size"""
        self._log_as_mediamgr(perm=self._permission("add", Image))
        url = reverse('coop_cms_upload_image')
        img_size = mommy.make(ImageSize, size="128")
        data = {
            'image': self._get_file("unittest1.png"),
            'descr': 'a test file',
            'filters': '',
            'size': img_size.id,
        }
        
        response = self.client.post(url, data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, 'close_popup_and_media_slide')
        
        images = Image.objects.all()
        self.assertEquals(1, images.count())
        self.assertEqual(images[0].name, data['descr'])
        self.assertEqual(images[0].filters.count(), 0)
        self.assertEqual(images[0].size, img_size)
        file_ = images[0].file
        file_.open('rb')
        self.assertEqual(file_.read(), self._get_file("unittest1.png").read())
        
    def test_post_form_anonymous(self):
        """upload image anonymous user"""
        url = reverse('coop_cms_upload_image')
        
        data = {
            'image': self._get_file("unittest1.png"),
            'descr': 'a test file',
            'filters': ''
        }
        
        response = self.client.post(url, data=data, follow=False)
        self.assertEqual(response.status_code, 302)
        next_url = "/accounts/login/?next={0}".format(url)
        self.assertTrue(response['Location'].find(next_url) >= 0)
        
        images = Image.objects.all()
        self.assertEquals(0, images.count())
        
    def test_post_form_not_allowed(self):
        """upload image when user is not allowed"""
        self._log_as_mediamgr()
        url = reverse('coop_cms_upload_image')
        
        data = {
            'image': self._get_file("unittest1.png"),
            'descr': 'a test file',
            'filters': ''
        }
        
        response = self.client.post(url, data=data, follow=False)
        self.assertEqual(response.status_code, 403)
        
        images = Image.objects.all()
        self.assertEquals(0, images.count())
        
    def test_post_form_with_filters(self):
        """upload image with filters"""

        self._log_as_mediamgr(perm=self._permission("add", Image))
        url = reverse('coop_cms_upload_image')
        
        filter1 = mommy.make(MediaFilter, name="icons")
        mommy.make(MediaFilter, name="big-images")
        filter3 = mommy.make(MediaFilter, name="small-images")
        
        data = {
            'image': self._get_file("unittest1.png"),
            'descr': 'a test file',
            'filters': [str(f.id) for f in (filter1, filter3)],
        }
        
        response = self.client.post(url, data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, 'close_popup_and_media_slide')
        
        images = Image.objects.all()
        self.assertEquals(1, images.count())
        self.assertEqual(images[0].name, data['descr'])
        self.assertEqual(images[0].filters.count(), 2)
        self.assertEqual(list(images[0].filters.all().order_by('id')), [filter1, filter3])
        
        file_ = images[0].file
        file_.open('rb')
        self.assertEqual(file_.read(), self._get_file("unittest1.png").read())
        
    def test_post_form_with_filters_no_choice(self):
        """upload image when filters configured and choice is blank"""

        self._log_as_mediamgr(perm=self._permission("add", Image))
        url = reverse('coop_cms_upload_image')
        
        mommy.make(MediaFilter, name="icons")
        mommy.make(MediaFilter, name="big-images")
        mommy.make(MediaFilter, name="small-images")
        
        data = {
            'image': self._get_file("unittest1.png"),
            'descr': 'a test file',
            'filters': [],
        }
        
        response = self.client.post(url, data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, 'close_popup_and_media_slide')
        
        images = Image.objects.all()
        self.assertEquals(1, images.count())
        self.assertEqual(images[0].name, data['descr'])
        self.assertEqual(images[0].filters.count(), 0)
        
        file_ = images[0].file
        file_.open('rb')
        self.assertEqual(file_.read(), self._get_file("unittest1.png").read())
        
    def test_post_form_with_invalid_size(self):
        """upload image with invalid size"""

        self._log_as_mediamgr(perm=self._permission("add", Image))
        url = reverse('coop_cms_upload_image')
        
        data = {
            'image': self._get_file("unittest1.png"),
            'descr': 'a test file',
            'filters': [],
            'size': "hhjk",
        }
        
        response = self.client.post(url, data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.content, 'close_popup_and_media_slide')
        
        images = Image.objects.all()
        self.assertEquals(0, images.count())

    def test_post_form(self):
        """upload image with size"""
        self._log_as_mediamgr(perm=self._permission("add", Image))
        url = reverse('coop_cms_upload_image')
        data = {
            'image': self._get_file("unittest1.png"),
            'descr': '',
            'filters': '',
            'size': '',
            'copyright': '',
        }

        response = self.client.post(url, data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, 'close_popup_and_media_slide')

        images = Image.objects.all()
        self.assertEquals(1, images.count())
        self.assertEqual(images[0].name, 'unittest1')
        self.assertEqual(images[0].copyright, data['copyright'])
        self.assertEqual(images[0].filters.count(), 0)
        self.assertEqual(images[0].size, None)
        file_ = images[0].file
        file_.open('rb')
        self.assertEqual(file_.read(), self._get_file("unittest1.png").read())

    def test_post_form_copyright(self):
        """upload image with size"""
        self._log_as_mediamgr(perm=self._permission("add", Image))
        url = reverse('coop_cms_upload_image')
        data = {
            'image': self._get_file("unittest1.png"),
            'descr': 'a test file',
            'filters': '',
            'size': '',
            'copyright': 'copyright me',
        }

        response = self.client.post(url, data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, 'close_popup_and_media_slide')

        images = Image.objects.all()
        self.assertEquals(1, images.count())
        self.assertEqual(images[0].name, data['descr'])
        self.assertEqual(images[0].copyright, data['copyright'])
        self.assertEqual(images[0].filters.count(), 0)
        self.assertEqual(images[0].size, None)
        file_ = images[0].file
        file_.open('rb')
        self.assertEqual(file_.read(), self._get_file("unittest1.png").read())


class ImageSizeTest(MediaBaseTestCase):
    """Test media library slide"""
    
    @override_settings(COOP_CMS_MAX_IMAGE_WIDTH="600")
    def test_image_max_width_no_size(self):
        """get image with no size upscale"""
        image = mommy.make(Image)
        url = image.get_absolute_url()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = StringIO(self.get_safe_content(response))
        img = PilImage.open(data)
        self.assertEqual(img.size[0], 130)
        
    @override_settings(COOP_CMS_MAX_IMAGE_WIDTH="600")
    def test_image_max_width_size(self):
        """get image with size"""
        size = mommy.make(ImageSize, size="60")
        image = mommy.make(Image, size=size)
        url = image.get_absolute_url()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = StringIO(self.get_safe_content(response))
        img = PilImage.open(data)
        self.assertEqual(img.size[0], 60)
        
    @override_settings(COOP_CMS_MAX_IMAGE_WIDTH="60")
    def test_image_max_width_size_no_scale(self):
        """get image with size downscale"""
        image = mommy.make(Image)
        url = image.get_absolute_url()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = StringIO(self.get_safe_content(response))
        img = PilImage.open(data)
        self.assertEqual(img.size[0], 60)
        
    @override_settings(COOP_CMS_MAX_IMAGE_WIDTH="coop_cms.tests.dummy_image_width")
    def test_image_max_width_size_lambda(self):
        """get image from function"""
        image = mommy.make(Image)
        url = image.get_absolute_url()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = StringIO(self.get_safe_content(response))
        img = PilImage.open(data)
        self.assertEqual(img.size[0], 20)
        
    @override_settings(COOP_CMS_MAX_IMAGE_WIDTH="")
    def test_image_max_width_size_none(self):
        """get image with size setting is empty"""
        image = mommy.make(Image)
        url = image.get_absolute_url()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = StringIO(self.get_safe_content(response))
        img = PilImage.open(data)
        self.assertEqual(img.size[0], 130)

    def test_image_no_size(self):
        """get image: no size"""
        image = mommy.make(Image, size=None)
        url = image.get_absolute_url()
        self.assertEqual(url, image.file.url)

    def test_image_size(self):
        """get image: with size"""
        image_size = mommy.make(ImageSize, size="128x128")
        image = mommy.make(Image, size=image_size)
        url = image.get_absolute_url()
        self.assertNotEqual(url, image.file.url)

    def test_image_wrong_size(self):
        """get image: wrong size"""
        image_size = mommy.make(ImageSize, size="blabla")
        image = mommy.make(Image, size=image_size)
        url = image.get_absolute_url()
        self.assertEqual(url, image.file.url)

    def test_image_size_crop(self):
        """get image: cropped"""
        image_size = mommy.make(ImageSize, size="128x128", crop="center")
        image = mommy.make(Image, size=image_size)
        url = image.get_absolute_url()
        self.assertNotEqual(url, image.file.url)


class MediaLibraryTest(MediaBaseTestCase):
    """Test media library slide"""

    def test_show_images_empty(self):
        """show images empty"""
        self._log_as_mediamgr()
        url = reverse('coop_cms_media_images')
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        
    def test_show_documents_empty(self):
        """show documents empty"""
        self._log_as_mediamgr()
        url = reverse('coop_cms_media_documents')
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
            
    def test_show_media_anonymous(self):
        """show images empty anonymous"""
        url = reverse('coop_cms_media_images')
        response = self.client.get(url)
        self.assertEqual(302, response.status_code)
        next_url = "/accounts/login/?next={0}".format(url)
        self.assertTrue(response['Location'].find(next_url) >= 0)
        
    def test_show_media_not_staff(self):
        """show images empty user is not a staff member"""
        self._log_as_mediamgr(is_staff=False)
        url = reverse('coop_cms_media_images')
        response = self.client.get(url)
        self.assertEqual(403, response.status_code)
    
    def test_show_images(self):
        """show images"""
        self._log_as_mediamgr()
        mommy.make(Image, _quantity=2)
        url = reverse('coop_cms_media_images')
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        soup = BeautifulSoup(response.content)
        nodes = soup.select(".library-thumbnail")
        self.assertEqual(2, len(nodes))
        
    def test_show_images_pagination(self):
        """show images with pagination"""
        self._log_as_mediamgr()
        mommy.make(Image, _quantity=16)
        url = reverse('coop_cms_media_images')
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        soup = BeautifulSoup(response.content)
        nodes = soup.select(".library-thumbnail")
        self.assertEqual(12, len(nodes))
    
    def test_show_images_page_2(self):
        """show images page 2"""
        self._log_as_mediamgr()
        mommy.make(Image, _quantity=16)
        url = reverse('coop_cms_media_images')+"?page=2"
        response = self.client.get(url, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(200, response.status_code)
        data = json.loads(response.content)
        soup = BeautifulSoup(data['html'])
        nodes = soup.select(".library-thumbnail")
        self.assertEqual(4, len(nodes))
        
    def test_show_images_media_filter(self):
        """show images with media filter"""
        self._log_as_mediamgr()
        media_filter = mommy.make(MediaFilter)
        images = []
        for i in range(16):
            images.append(mommy.make(Image, created=datetime(2014, 1, 1, 12, i)))
        images.reverse()
        
        images[5].filters.add(media_filter)
        images[15].filters.add(media_filter)
        url = reverse('coop_cms_media_images')+"?page=1&media_filter={0}".format(media_filter.id)
        response = self.client.get(url, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(200, response.status_code)
        data = json.loads(response.content)
        soup = BeautifulSoup(data['html'])
        nodes = soup.select(".library-thumbnail")
        self.assertEqual(2, len(nodes))
        expected = [x.file.url for x in (images[5], images[15])]
        actual = [node["rel"] for node in nodes]
        self.assertEqual(expected, actual)
    
    def test_show_images_media_filter_all(self):
        """show images empty with all media filter"""
        self._log_as_mediamgr()
        media_filter = mommy.make(MediaFilter)
        
        images = []
        for i in range(16):
            images.append(mommy.make(Image, created=datetime(2014, 1, 1, 12, i)))
        images.reverse()
        
        images[5].filters.add(media_filter)
        images[15].filters.add(media_filter)
        url = reverse('coop_cms_media_images')+"?page=1&media_filter={0}".format(0)
        response = self.client.get(url, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(200, response.status_code)
        data = json.loads(response.content)
        soup = BeautifulSoup(data['html'])
        nodes = soup.select(".library-thumbnail")
        self.assertEqual(12, len(nodes))
        expected = [x.file.url for x in images[:12]]
        actual = [node["rel"] for node in nodes]
        self.assertEqual(expected, actual)
    
    
class UploadDocTest(MediaBaseTestCase):
    """Download document"""

    def test_upload_public_doc(self):
        """upload public"""
        self._log_as_mediamgr(perm=self._permission("add", Document))
        data = {
            'file': self._get_file(),
            'is_private': False,
            'name': 'a test file',
        }
        response = self.client.post(reverse('coop_cms_upload_doc'), data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, 'close_popup_and_media_slide')
        public_docs = Document.objects.filter(is_private=False)
        self.assertEquals(1, public_docs.count())
        self.assertEqual(public_docs[0].name, data['name'])
        self.assertEqual(public_docs[0].category, None)
        file_ = public_docs[0].file
        file_.open('rb')
        self.assertEqual(file_.read(), self._get_file().read())
        
    def test_upload_public_doc_category(self):
        """upload public category"""
        self._log_as_mediamgr(perm=self._permission("add", Document))
        cat = mommy.make(ArticleCategory, name="my cat")
        data = {
            'file': self._get_file(),
            'is_private': False,
            'name': 'a test file',
            'category': cat.id,
        }
        response = self.client.post(reverse('coop_cms_upload_doc'), data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, 'close_popup_and_media_slide')
        public_docs = Document.objects.filter(is_private=False)
        self.assertEquals(1, public_docs.count())
        self.assertEqual(public_docs[0].name, data['name'])
        self.assertEqual(public_docs[0].category, cat)
        file_ = public_docs[0].file
        file_.open('rb')
        self.assertEqual(file_.read(), self._get_file().read())
        
    def test_upload_doc_missing_fields(self):
        """upload public: missing fields"""
        self._log_as_mediamgr(perm=self._permission("add", Document))
        data = {
            'is_private': False,
        }
        response = self.client.post(reverse('coop_cms_upload_doc'), data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.content, 'close_popup_and_media_slide')
        self.assertEquals(0, Document.objects.all().count())

    def test_upload_doc_anonymous_user(self):
        """upload: anonymous user"""

        data = {
            'file': self._get_file(),
            'is_private': False,
        }
        response = self.client.post(reverse('coop_cms_upload_doc'), data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.content, 'close_popup_and_media_slide')
        self.assertEquals(0, Document.objects.all().count())
        redirect_url = response.redirect_chain[-1][0]
        login_url = reverse('django.contrib.auth.views.login')
        self.assertTrue(redirect_url.find(login_url) >= 0)
        
    def test_upload_not_allowed(self):
        """upload: not allowed"""

        self._log_as_mediamgr()
        data = {
            'file': self._get_file(),
            'is_private': False,
        }
        response = self.client.post(reverse('coop_cms_upload_doc'), data=data, follow=True)
        self.assertEqual(response.status_code, 403)
        
    def test_upload_private_doc(self):
        """upload private doc"""
        self._log_as_mediamgr(perm=self._permission("add", Document))
        data = {
            'file': self._get_file(),
            'is_private': True,
        }
        response = self.client.post(reverse('coop_cms_upload_doc'), data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, 'close_popup_and_media_slide')
        private_docs = Document.objects.filter(is_private=True)
        self.assertEquals(1, private_docs.count())
        #TODO : on drone.io filename is unittest1_SomeRandom. Why?
        #self.assertNotEqual(private_docs[0].name, 'unittest1')
        self.assertNotEqual(private_docs[0].name, '')
        self.assertEqual(private_docs[0].category, None)
        file_ = private_docs[0].file
        file_.open('rb')
        self.assertEqual(file_.read(), self._get_file().read())


class DocsInMediaLibTest(MediaBaseTestCase):
    """view documents in media lib"""

    def test_view_docs(self):
        """view documents"""
        self._log_as_mediamgr(perm=self._permission("add", Document))
        file1 = File(self._get_file())
        doc1 = mommy.make(Document, is_private=True, file=file1)
        file2 = File(self._get_file())
        doc2 = mommy.make(Document, is_private=False, file=file2)
        
        response = self.client.get(reverse('coop_cms_media_documents'))
        self.assertEqual(response.status_code, 200)
        
        self.assertContains(response, reverse('coop_cms_download_doc', args=[doc1.id]))
        self.assertNotContains(response, doc1.file.url)
        self.assertNotContains(response, reverse('coop_cms_download_doc', args=[doc2.id]))
        self.assertContains(response, doc2.file.url)
        
    def test_view_docs_anonymous(self):
        """view docs anonymous"""
        url = reverse('coop_cms_media_documents')
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)
        redirect_url = response.redirect_chain[-1][0]
        login_url = reverse('django.contrib.auth.views.login')
        self.assertTrue(redirect_url.find(login_url) >= 0)
        
    def test_view_docs_not_allowed(self):
        """view docs not allowed"""
        self._log_as_mediamgr(is_staff=False)
        response = self.client.get(reverse('coop_cms_media_documents'), follow=True)
        self.assertEqual(response.status_code, 403)


@skipIf('photologue' not in settings.INSTALLED_APPS, "photologue is not installed")
class PhotologueInMediaLibTest(MediaBaseTestCase):
    """view documents in media lib"""

    def test_view_photos_empty(self):
        """view medialib when no photos"""
        self._log_as_mediamgr(perm=self._permission("add", Photo))

        response = self.client.get(reverse('coop_cms_media_photologue'))
        self.assertEqual(response.status_code, 200)

        soup = BeautifulSoup(response.content)
        nodes = soup.select(".library-thumbnail")
        self.assertEqual(0, len(nodes))

        nodes = soup.select(".media-filters a")
        self.assertEqual(0, len(nodes))

    def test_view_photos_not_empty(self):
        """view photos"""
        self._log_as_mediamgr(perm=self._permission("add", Photo))
        mommy.make(Photo)
        mommy.make(Photo)

        response = self.client.get(reverse('coop_cms_media_photologue'))
        self.assertEqual(response.status_code, 200)

        soup = BeautifulSoup(response.content)
        nodes = soup.select(".library-thumbnail")
        self.assertEqual(2, len(nodes))

        nodes = soup.select(".media-filters a")
        self.assertEqual(0, len(nodes))

    def test_view_anonymous(self):
        """view docs anonymous"""
        response = self.client.get(reverse('coop_cms_media_photologue'), follow=True)
        self.assertEqual(response.status_code, 200)
        redirect_url = response.redirect_chain[-1][0]
        login_url = reverse('django.contrib.auth.views.login')
        self.assertTrue(redirect_url.find(login_url) >= 0)

    def test_view_not_allowed(self):
        """view docs not allowed"""
        self._log_as_mediamgr(is_staff=False)
        response = self.client.get(reverse('coop_cms_media_photologue'), follow=True)
        self.assertEqual(response.status_code, 403)

    def test_view_photos_gallery(self):
        """view photos"""
        self._log_as_mediamgr(perm=self._permission("add", Photo))
        gallery = mommy.make(Gallery)

        photo1 = mommy.make(Photo)
        photo1.galleries.add(gallery)
        photo1.save()

        mommy.make(Photo)

        response = self.client.get(reverse('coop_cms_media_photologue'))
        self.assertEqual(response.status_code, 200)

        soup = BeautifulSoup(response.content)
        nodes = soup.select(".library-thumbnail")
        self.assertEqual(2, len(nodes))

        nodes = soup.select(".media-filters a")
        #All + gallery
        self.assertEqual(2, len(nodes))

    def test_view_photos_gallery_several(self):
        """view photos"""
        self._log_as_mediamgr(perm=self._permission("add", Photo))
        gallery = mommy.make(Gallery)
        mommy.make(Gallery)
        mommy.make(Gallery)

        photo1 = mommy.make(Photo)
        photo1.galleries.add(gallery)
        photo1.save()

        mommy.make(Photo)

        response = self.client.get(reverse('coop_cms_media_photologue'))
        self.assertEqual(response.status_code, 200)

        soup = BeautifulSoup(response.content)
        nodes = soup.select(".library-thumbnail")
        self.assertEqual(2, len(nodes))

        nodes = soup.select(".media-filters a")
        #All + galleries
        self.assertEqual(4, len(nodes))

    def test_view_photos_only_gallery(self):
        """view photos"""
        self._log_as_mediamgr(perm=self._permission("add", Photo))
        gallery1 = mommy.make(Gallery)
        gallery2 = mommy.make(Gallery)

        photo1 = mommy.make(Photo)
        photo1.galleries.add(gallery1)
        photo1.save()

        photo2 = mommy.make(Photo)
        photo2.galleries.add(gallery2)
        photo2.save()

        mommy.make(Photo)

        url = reverse('coop_cms_media_photologue')+"?gallery_filter={0}".format(gallery1.id)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        soup = BeautifulSoup(response.content)
        nodes = soup.select(".library-thumbnail")
        self.assertEqual(1, len(nodes))
        self.assertEqual(photo1.title, nodes[0]["title"])

        nodes = soup.select(".media-filters a")
        self.assertEqual(3, len(nodes))


class DownloadDocTest(MediaBaseTestCase):
    """Download document"""

    def test_download_public(self):
        """download public doc"""
        #create a public doc
        file_ = File(self._get_file())
        doc = mommy.make(Document, is_private=False, file=file_)
        
        #check the url
        private_url = reverse('coop_cms_download_doc', args=[doc.id])
        self.assertNotEqual(doc.get_download_url(), private_url)
        
        #login and download
        self._log_as_mediamgr()

        response = self.client.get(doc.get_download_url())
        self.assertEqual(response.status_code, 200)

        content = self.get_safe_content(response)
        self.assertEqual(content, self._get_file().read())
        
        #logout and download
        self.client.logout()
        response = self.client.get(doc.get_download_url())
        self.assertEqual(response.status_code, 200)
        content = self.get_safe_content(response)
        self.assertEqual(content, self._get_file().read())
        
    @skipIf('sanza.Profile' in settings.INSTALLED_APPS, "sanza.Profile installed")
    def test_download_private(self):
        """download private doc"""
            
        #create a public doc
        file_ = File(self._get_file())
        cat = mommy.make(ArticleCategory, name="private-doc")
        doc = mommy.make(Document, is_private=True, file=file_, category=cat)

        #check the url
        private_url = reverse('coop_cms_download_doc', args=[doc.id])
        self.assertEqual(doc.get_download_url(), private_url)
        
        #login and download
        self._log_as_mediamgr()
        response = self.client.get(doc.get_download_url())
        self.assertEqual(response.status_code, 200)
        self.assertEquals(response['Content-Disposition'], "attachment; filename=unittest1.txt")
        self.assertEquals(response['Content-Type'], "text/plain")
        #TODO: This change I/O Exception in UnitTest
        #self.assertEqual(response.content, self._get_file().read()) 
        
        #logout and download
        self.client.logout()
        response = self.client.get(doc.get_download_url(), follow=True)
        self.assertEqual(response.status_code, 200)
        redirect_url = response.redirect_chain[-1][0]
        login_url = reverse('django.contrib.auth.views.login')
        self.assertTrue(redirect_url.find(login_url) >= 0)
        

class ImageListTemplateTagTest(BaseTestCase):
    """Test image List template tag"""

    def test_non_existing_filter(self):
        """test not existing ist"""
        tpl = Template('{% load coop_utils %}{% coop_image_list "test" as image_list %}{{image_list|length}}')
        html = tpl.render(Context({}))
        self.assertEqual(html, "0")

    def test_empty_filter(self):
        """test empty filter"""
        mommy.make(MediaFilter, name="abcd")
        tpl = Template('{% load coop_utils %}{% coop_image_list "abcd" as image_list %}{{image_list|length}}')
        html = tpl.render(Context({}))
        self.assertEqual(html, "0")

    def test_filter_with_images(self):
        """test filter with image"""
        filter_ = mommy.make(MediaFilter, name="abcd")
        mommy.make(Image, filters=[filter_])
        tpl = Template('{% load coop_utils %}{% coop_image_list "abcd" as image_list %}{{image_list|length}}')
        html = tpl.render(Context({}))
        self.assertEqual(html, "1")

    def test_filter_with_images_var_name(self):
        """test filter: name from variable"""
        filter_ = mommy.make(MediaFilter, name="abcd")
        mommy.make(Image, filters=[filter_])
        tpl = Template('{% load coop_utils %}{% coop_image_list filter_name as image_list %}{{image_list|length}}')
        html = tpl.render(Context({"filter_name": filter_.name}))
        self.assertEqual(html, "1")

    def test_filter_as_missing(self):
        """test filter: as is missing"""
        filter_ = mommy.make(MediaFilter, name="abcd")
        mommy.make(Image, filters=[filter_])
        try:
            Template('{% load coop_utils %}{% coop_image_list "abcd" image_list %}{{image_list|length}}')
        except TemplateSyntaxError as msg:
            self.assertEqual("coop_image_list: usage --> {% coop_image_list 'filter_name' as var_name %}", unicode(msg))
        else:
            self.assertEqual("", "No exception")


class ArticleLogoTest(BaseArticleTest):
    """test article logo"""

    def _get_image(self, file_name='unittest1.png'):
        """get image"""
        return self._get_file(file_name)

    def setUp(self):
        """before each test"""
        super(ArticleLogoTest, self).setUp()
        self._default_article_templates = settings.COOP_CMS_ARTICLE_TEMPLATES
        settings.COOP_CMS_ARTICLE_TEMPLATES = (
            ('test/article_with_logo_size.html', 'Article with logo size'),
            ('test/article_with_logo_size_and_crop.html', 'Article with logo size and crop'),
            ('test/article_no_logo_size.html', 'Article no logo size and crop'),
        )
        self._default_logo_size = getattr(settings, 'COOP_CMS_ARTICLE_LOGO_SIZE', None)
        self._default_logo_crop = getattr(settings, 'COOP_CMS_ARTICLE_LOGO_CROP', None)

    def tearDown(self):
        """after each test"""
        super(ArticleLogoTest, self).tearDown()
        #restore
        settings.COOP_CMS_ARTICLE_TEMPLATES = self._default_article_templates
        settings.COOP_CMS_ARTICLE_LOGO_SIZE = self._default_logo_size
        settings.COOP_CMS_ARTICLE_LOGO_CROP = self._default_logo_crop

    def test_view_article_no_image(self, template_index=0, image=False):
        """article no image"""
        article_class = get_article_class()
        article = mommy.make(
            article_class,
            title=u"This is my article",
            content=u"<p>This is my <b>content</b></p>",
            template=settings.COOP_CMS_ARTICLE_TEMPLATES[template_index][0]
        )
        if image:
            article.logo = File(self._get_image())
            article.save()

        response = self.client.get(article.get_absolute_url())
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, article.title)
        self.assertContains(response, article.content)

    def test_view_article_no_image_crop(self):
        """test article no image crop"""
        self.test_view_article_no_image(1)

    def test_view_article_image_no_crop(self):
        """test article no image no crop"""
        self.test_view_article_no_image(0, True)

    def test_view_article_image_and_crop(self):
        """test article image and crop"""
        self.test_view_article_no_image(1, True)

    def test_edit_article_no_image(self, template_index=0, image=False, post_image=False):
        """test edit article no image"""
        article_class = get_article_class()
        if image:
            article = mommy.make(
                article_class,
                title=u"This is my article",
                content=u"<p>This is my <b>content</b></p>",
                slug="",
                template=settings.COOP_CMS_ARTICLE_TEMPLATES[template_index][0],
                logo=File(self._get_image())
            )
        else:
            article = mommy.make(
                article_class,
                title=u"This is my article",
                content=u"<p>This is my <b>content</b></p>",
                slug="",
                template=settings.COOP_CMS_ARTICLE_TEMPLATES[template_index][0]
            )

        self._log_as_editor()

        response = self.client.post(article.get_edit_url(), follow=True)
        self.assertEqual(response.status_code, 200)

        data = {
            'title': 'Title of the article',
            'content': 'The content',
        }
        if post_image:
            data['logo'] = self._get_image('unittest2.png')
        response = self.client.post(article.get_edit_url(), data=data, follow=True)
        self.assertEqual(response.status_code, 200)

        article = article_class.objects.get(id=article.id)

        self.assertEqual(data['title'], article.title)
        self.assertEqual(data['content'], article.content)

        self.assertContains(response, article.title)
        self.assertContains(response, article.content)

    def test_edit_article_no_image_crop(self):
        """test edit article no image and crop"""
        self.test_edit_article_no_image(1)

    def test_edit_article_image_no_post_no_crop(self):
        """test edit article image no crop"""
        self.test_edit_article_no_image(0, True, False)

    def test_edit_article_image_no_post_crop(self):
        """test edit article image no crop"""
        self.test_edit_article_no_image(1, True, False)

    def test_edit_article_image_post_no_crop(self):
        """test edit article image no crop"""
        self.test_edit_article_no_image(0, True, True)

    def test_edit_article_image_post_crop(self):
        """test edit article image crop"""
        self.test_edit_article_no_image(1, True, True)

    def test_view_article_no_image_template1(self):
        """test view article no image template 1"""
        self.test_view_article_no_image(2, False)

    def test_view_article_no_image_template2(self):
        """test view article no image template 2"""
        self.test_view_article_no_image(2, True)

    def test_view_article_no_image_template3(self):
        """test view article no image template 3"""
        settings.COOP_CMS_ARTICLE_LOGO_SIZE = "x100"
        settings.COOP_CMS_ARTICLE_LOGO_CROP = "top"
        self.test_view_article_no_image(2, True)

    def test_edit_article_no_image_template1(self):
        """test edit article no image template 1"""
        self.test_edit_article_no_image(2, False, False)

    def test_edit_article_no_image_template2(self):
        """test edit article no image template 2"""
        self.test_edit_article_no_image(2, True, False)

    def test_edit_article_no_image_template3(self):
        """test edit article no image template 3"""
        self.test_edit_article_no_image(2, True, True)

    def test_edit_article_no_image_template4(self):
        """test edit article no image template 4"""
        settings.COOP_CMS_ARTICLE_LOGO_SIZE = "x100"
        settings.COOP_CMS_ARTICLE_LOGO_CROP = "top"
        self.test_edit_article_no_image(2, True, True)
