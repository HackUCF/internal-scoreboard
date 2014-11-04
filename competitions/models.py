from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User


class Competition(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('competitions.competition', args=(self.slug,))


class Challenge(models.Model):
    name = models.CharField(max_length=128)
    value = models.IntegerField('Point Value')
    competition = models.ForeignKey(Competition, related_name='challenges')
    solver = models.ManyToManyField(User, related_name='solved_challenges', blank=True)

    def __str__(self):
        return self.name