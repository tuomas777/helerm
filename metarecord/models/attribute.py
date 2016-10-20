from django.db import models
from django.utils.translation import ugettext_lazy as _

from .base import BaseModel, StructuralElement


def reload_attribute_schema():
    whole_schema = []

    for attribute in Attribute.objects.prefetch_related('values'):
        attribute_schema = {
            'name': attribute.identifier,
            'class': 'CharField',
            'kwargs': {
                'max_length': 1024,
                'blank': True,
                'null': True,
                'verbose_name': attribute.name,
            }
        }

        values = attribute.values.all()
        if len(values):
            choices = [(value.value, value.value) for value in values]
            attribute_schema['kwargs']['choices'] = choices

        whole_schema.append(attribute_schema)

    for model in StructuralElement.__subclasses__():
        data_field = model._meta.get_field('attributes')
        data_field.reload_schema(whole_schema)


class Attribute(BaseModel):
    identifier = models.CharField(verbose_name=_('identifier'), max_length=64, unique=True, db_index=True)
    name = models.CharField(verbose_name=_('name'), max_length=256)

    class Meta:
        verbose_name = _('attribute')
        verbose_name_plural = _('attributes')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.identifier:
            self.identifier = self.pk
        super().save(*args, **kwargs)

    def is_free_text(self):
        return not self.values.exists()


class AttributeValue(BaseModel):
    attribute = models.ForeignKey(Attribute, verbose_name=_('attribute'), related_name='values')
    value = models.CharField(verbose_name=_('value'), max_length=1024)

    class Meta:
        verbose_name = _('attribute value')
        verbose_name_plural = _('attribute values')
        unique_together = ('attribute', 'value')

    def __str__(self):
        return self.value
