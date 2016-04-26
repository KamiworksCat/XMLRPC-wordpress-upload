from __future__ import unicode_literals

from django.db import models
from django.db.models import permalink
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _


class Blog(models.Model):
    title = models.CharField(_('Blog Title'), max_length=100, unique=True)
    slug = models.SlugField(_('Blog slug'), max_length=100, unique=True)
    body = models.TextField(_('Blog content'))
    posted = models.DateTimeField(auto_now_add=True, verbose_name=_('Date Posted'))
    modified = models.DateTimeField(_('Last Modified Date'), auto_now=True, null=True)
    category = models.ManyToManyField('Category')
    tag = models.ManyToManyField('Tags')

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return 'view_blog_post', None, {'slug': self.slug}

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)


class Category(models.Model):
    title = models.CharField(_('Category Title'), max_length=100, db_index=True)
    slug = models.SlugField(_('Category Slug'), max_length=100, db_index=True)
    posted = models.DateTimeField(auto_now_add=True, verbose_name=_('Date Posted'))
    modified = models.DateTimeField(_('Last Modified Date'), auto_now=True, null=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return 'view_blog_category', None, {'slug': self.slug}

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)


class Tags(models.Model):
    title = models.CharField(_('Tag Title'), max_length=100, db_index=True)
    slug = models.SlugField(_('Tag Slug'), max_length=100, db_index=True)
    posted = models.DateTimeField(auto_now_add=True, verbose_name=_('Date Posted'))
    modified = models.DateTimeField(_('Last Modified Date'), auto_now=True, null=True)

    class Meta:
        verbose_name_plural = 'Tags'

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return 'view_blog_tag', None, {'slug': self.slug}

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Tags, self).save(*args, **kwargs)
