from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.core.models import Page
from wagtail.images.models import Image, AbstractImage, AbstractRendition


class HomePage(Page):
    pass


class CustomImage(AbstractImage):
    caption = models.CharField(max_length=255, blank=True)

    admin_form_fields = Image.admin_form_fields + (
        # Then add the field names here to make them appear in the form:
        'caption',
    )


class CustomRendition(AbstractRendition):
    image = models.ForeignKey(CustomImage, related_name='renditions', on_delete=models.CASCADE)

    class Meta:
        unique_together = (
            ('image', 'filter_spec', 'focal_point_key'),
        )
