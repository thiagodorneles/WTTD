# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
# from eventex.core.managers import (EmailContactManager, PhoneContactManager, FaxContactManager)
from eventex.core.managers import KindContactManager, PeriodManager

class Speaker(models.Model):
    name = models.CharField(_('Nome'), max_length=255)
    slug = models.SlugField(_('Slug'))
    url = models.URLField(_('Url'))
    description = models.TextField(_(u'Descrição'), blank=True)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('core:speaker_detail', (), {'slug':self.slug})

class Contact(models.Model):
    KINDS = (
        ('P', _('Telefone')),
        ('F', _('Fax')),
        ('E', _('E-mail')),
    )
    speaker = models.ForeignKey('Speaker', verbose_name=_('palestrante'))
    kind = models.CharField(_('tipo'), max_length=1, choices=KINDS)
    value = models.CharField(_('valor'), max_length=255)

    objects = models.Manager()
    emails = KindContactManager('E')
    phones = KindContactManager('P')
    faxes = KindContactManager('F')
    # emails = EmailContactManager()
    # phones = PhoneContactManager()
    # faxes = FaxContactManager()

    def __unicode__(self):
        return self.value

class Talk(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.TimeField(blank=True)
    speakers = models.ManyToManyField('Speaker', verbose_name=_('palestrante'))

    objects = PeriodManager()

    @property
    def slides(self):
        return self.media_set.filter(kind='SL')

    @property
    def videos(self):
        return self.media_set.filter(kind='YT')

    class Meta:
        verbose_name = _('palestra')
        verbose_name_plural = _('palestras')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/palestras/%d/' % self.pk

class Course(Talk):
    slots = models.IntegerField()
    notes = models.TextField()

    objects = PeriodManager()

class Media(models.Model):
    MEDIAS = (
        ('YT', _('YouTube')),
        ('SL', _('SlideShare')),
    )

    talk = models.ForeignKey('Talk')
    kind = models.CharField(_('Tipo'), max_length=2, choices=MEDIAS)
    title = models.CharField(_(u'Título'), max_length=255)
    media_id = models.CharField(_('Ref'), max_length=255)

    def __unicode__(self):
        return u'%s - %s' % (self.talk.title, self.title)