from search_test.settings import TIME_ZONE
from django.db.models import Model
from django.db.models.fields import CharField, TextField

class Product(Model):
  name = CharField(max_length=255)
  description = TextField()