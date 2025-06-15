# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Article.login_required'
        db.add_column(u'basic_cms_article', 'login_required',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Article.login_required'
        db.delete_column(u'basic_cms_article', 'login_required')


    models = {
        u'basic_cms.article': {
            'Meta': {'object_name': 'Article'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "u'basic_cms_article_rel'", 'null': 'True', 'blank': 'True', 'to': u"orm['coop_cms.ArticleCategory']"}),
            'content': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'headline': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'homepage_for_site': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'homepage_article'", 'null': 'True', 'blank': 'True', 'to': u"orm['sites.Site']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_newsletter': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'publication': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'publication_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'default': '[1]', 'to': u"orm['sites.Site']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'}),
            'subtitle': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'temp_logo': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'})
        },
        u'basic_cms.navtree': {
            'Meta': {'object_name': 'NavTree'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'default'", 'unique': 'True', 'max_length': '100', 'db_index': 'True'}),
            'types': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'basic_cms_navtree_set'", 'blank': 'True', 'to': u"orm['coop_cms.NavType']"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'coop_cms.articlecategory': {
            'Meta': {'object_name': 'ArticleCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_rss': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'default': '[1]', 'to': u"orm['sites.Site']", 'symmetrical': 'False'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '100', 'separator': "u'-'", 'blank': 'True', 'unique': 'True', 'populate_from': "'name'", 'overwrite': 'False'})
        },
        u'coop_cms.navtype': {
            'Meta': {'object_name': 'NavType'},
            'content_type': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['contenttypes.ContentType']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label_rule': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'search_field': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['basic_cms']