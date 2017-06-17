from django.db import models

from .quality_item import QualityItem
from videoclases.models.homework import Homework


class QualityControl(models.Model):
    homework = models.ManyToManyField(Homework)
    list_items = models.ManyToManyField(QualityItem)

    def __unicode__(self):
        return u" - ".join([str(hw) for hw in self.homework.all()])