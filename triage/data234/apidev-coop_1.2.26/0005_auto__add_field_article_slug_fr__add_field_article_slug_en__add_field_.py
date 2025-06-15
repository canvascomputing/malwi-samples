# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Article.slug_fr'
        db.add_column('basic_cms_article', 'slug_fr',
                      self.gf('django.db.models.fields.CharField')(db_index=True, max_length=100, unique=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Article.slug_en'
        db.add_column('basic_cms_article', 'slug_en',
                      self.gf('django.db.models.fields.CharField')(db_index=True, max_length=100, unique=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Article.title_fr'
        db.add_column('basic_cms_article', 'title_fr',
                      self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True),
                      keep_default=False)

        # Adding field 'Article.title_en'
        db.add_column('basic_cms_article', 'title_en',
                      self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True),
                      keep_default=False)

        # Adding field 'Article.content_fr'
        db.add_column('basic_cms_article', 'content_fr',
                      self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True),
                      keep_default=False)

        # Adding field 'Article.content_en'
        db.add_column('basic_cms_article', 'content_en',
                      self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True),
                      keep_default=False)

        # Adding field 'Article.summary_fr'
        db.add_column('basic_cms_article', 'summary_fr',
                      self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True),
                      keep_default=False)

        # Adding field 'Article.summary_en'
        db.add_column('basic_cms_article', 'summary_en',
                      self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True),
                      keep_default=False)


        # Changing field 'Article.slug'
        db.alter_column('basic_cms_article', 'slug', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100))

    def backwards(self, orm):
        # Deleting field 'Article.slug_fr'
        db.delete_column('basic_cms_article', 'slug_fr')

        # Deleting field 'Article.slug_en'
        db.delete_column('basic_cms_article', 'slug_en')

        # Deleting field 'Article.title_fr'
        db.delete_column('basic_cms_article', 'title_fr')

        # Deleting field 'Article.title_en'
        db.delete_column('basic_cms_article', 'title_en')

        # Deleting field 'Article.content_fr'
        db.delete_column('basic_cms_article', 'content_fr')

        # Deleting field 'Article.content_en'
        db.delete_column('basic_cms_article', 'content_en')

        # Deleting field 'Article.summary_fr'
        db.delete_column('basic_cms_article', 'summary_fr')

        # Deleting field 'Article.summary_en'
        db.delete_column('basic_cms_article', 'summary_en')


        # Changing field 'Article.slug'
        db.alter_column('basic_cms_article', 'slug', self.gf('django_extensions.db.fields.AutoSlugField')(populate_from='title', allow_duplicates=False, max_length=100, separator=u'-', unique=True, overwrite=False))

    models = {
        'basic_cms.article': {
            'Meta': {'object_name': 'Article'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'basic_cms_article_rel'", 'null': 'True', 'blank': 'True', 'to': "orm['coop_cms.ArticleCategory']"}),
            'content': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'content_en': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'content_fr': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'headline': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_newsletter': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_homepage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'publication': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'}),
            'slug_en': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'slug_fr': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'summary_en': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'summary_fr': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'temp_logo': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'title_en': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'title_fr': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'})
        },
        'basic_cms.navtree': {
            'Meta': {'object_name': 'NavTree'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'default'", 'unique': 'True', 'max_length': '100', 'db_index': 'True'}),
            'types': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['coop_cms.NavType']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'coop_cms.articlecategory': {
            'Meta': {'object_name': 'ArticleCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '100', 'separator': "u'-'", 'blank': 'True', 'unique': 'True', 'populate_from': "'name'", 'overwrite': 'False'})
        },
        'coop_cms.navtype': {
            'Meta': {'object_name': 'NavType'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label_rule': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'search_field': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['basic_cms']