# -*- coding: utf-8 -*-
"""custom backend for sorl-thumbnail: keep image file name"""

import os.path

from sorl.thumbnail.base import ThumbnailBackend, EXTENSIONS
from sorl.thumbnail.conf import settings
from sorl.thumbnail.helpers import tokey, serialize


# activated by adding following line to the settings.py
# THUMBNAIL_BACKEND = 'coop_cms.thumbnail_backend.KeepNameThumbnailBackend'
# This backend keeps the filename

class KeepNameThumbnailBackend(ThumbnailBackend):
    """This backend keep the filename when generating a thumbnail image"""
    
    def _get_thumbnail_filename(self, source, geometry_string, options):
        """Computes the destination filename."""

        key = tokey(source.key, geometry_string, serialize(options))
        
        filename, _ext = os.path.splitext(os.path.basename(source.name))
        
        path = u'{0}/{1}'.format(key, filename)
        image_format = options['format']

        return u'{0}{1}.{2}'.format(settings.THUMBNAIL_PREFIX, path, EXTENSIONS[image_format])