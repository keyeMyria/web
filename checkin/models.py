from datetime import time

from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone


class Profile(models.Model):
    name = models.CharField(max_length=100, verbose_name="Navn")
    card_id = models.CharField(max_length=100, verbose_name="Kortnummer")