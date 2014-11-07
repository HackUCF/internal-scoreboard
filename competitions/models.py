from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User


class Competition(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField()
    internal = models.BooleanField('Scored internally', default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('competitions.competition', args=(self.slug,))


class ChallengeCategory(models.Model):
    name = models.CharField(max_length=32, unique=True, help_text='Put it in lowercase, for style.')

    class Meta:
        verbose_name_plural = 'Challenge categories'

    def __str__(self):
        return self.name


class Challenge(models.Model):
    name = models.CharField(max_length=128)
    value = models.IntegerField('Point Value')
    competition = models.ForeignKey(Competition, related_name='challenges')
    category = models.ForeignKey(ChallengeCategory, related_name='challenge', blank=True, null=True)
    solver = models.ManyToManyField(User, related_name='solved_challenges', blank=True)

    def __str__(self):
        return self.name