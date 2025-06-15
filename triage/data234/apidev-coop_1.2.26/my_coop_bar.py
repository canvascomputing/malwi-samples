# -*- coding: utf-8 -*-
"""
Example of a custom coop_bar configuration
"""

from coop_cms import coop_bar_cfg

def load_commands(coop_bar):
    """This is where to define menus displayed by the coop_bar"""

    coop_bar.register([
        [
            coop_bar_cfg.edit_newsletter,
            coop_bar_cfg.cancel_edit_newsletter,
            coop_bar_cfg.save_newsletter,
            coop_bar_cfg.change_newsletter_settings,
            coop_bar_cfg.change_newsletter_template,
            coop_bar_cfg.test_newsletter,
        ],
        [
            coop_bar_cfg.cms_edit,
            coop_bar_cfg.cms_save,
            coop_bar_cfg.cms_cancel],
        [
            coop_bar_cfg.cms_new_article,
            coop_bar_cfg.cms_article_settings,
        ],
        [
            coop_bar_cfg.cms_publish,
        ],
        [
            coop_bar_cfg.cms_media_library,
            coop_bar_cfg.cms_upload_image,
            coop_bar_cfg.cms_upload_doc,
        ],
        [
            coop_bar_cfg.log_out,
        ],
    ])

