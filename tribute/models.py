from django.db import models
from django.utils import timezone
import json


class Game(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(default=timezone.now)
    last_edit = models.DateTimeField(blank=True, null=True)
    big_picture = models.CharField(max_length=500)
    palette = models.TextField(max_length=200, blank=True, null=True)

    def publish(self):
        self.last_edit = timezone.now()
        self.save()

    def __str__(self):
        return self.name

    def set_palette(self, x):
        self.palette = json.dumps(x)

    def get_palette(self, x):
        return json.loads(self.palette)


class Card(models.Model):
    TYPE = (
        (0,'Period'),
        (1,'Event'),
        (2,'Scene'),
        (3,'Legacy')
    )
    game_id = models.ForeignKey(Game)
    parent = models.ForeignKey('self')
    position = models.IntegerField()
    card_type = models.IntegerField(choices=TYPE)
    title = models.CharField(max_length=200)
    is_bright = models.BooleanField()
    text = models.TextField()

    def __str__(self):
        return self.title

    def publish(self):
        self.save()