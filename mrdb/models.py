from django.db import models
from django.utils import timezone

# Create your models here. https://docs.djangoproject.com/en/1.9/ref/models/fields/#field-types
"""
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
"""

class Titles(models.Model):
    idkey = models.IntegerField()
    type = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    year = models.CharField(max_length=4)
    summary = models.TextField()
    rating = models.CharField(max_length=50)
    diversity_score = models.IntegerField()
    bechdel_test = models.BooleanField()
    release_date = models.DateField()
    activate = models.BooleanField()

class Associated_Persons(models.Model):
    idkey = models.IntegerField()
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


"""
class Productions(model.Model):
    idkey = models.ForeignKey()
    title = 
    production_company_network



class Persons_Diversity(models.Model):
    persons_name = 
    diversity_type =

class Character_Diversity(models.Model):
    idkey = models.ForeignKey()
    title = 
    diversity_type

class Diversity_Categories(models.Model):
    diversity_category = 
    diversity_type = 
"""