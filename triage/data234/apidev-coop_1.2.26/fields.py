# -*- coding: utf-8 -*-
"""forms"""

import floppyforms


class HidableMultipleChoiceField(floppyforms.MultipleChoiceField):
    """
    The MultipleChoiceField doesn't return an <input type="hidden"> when hidden but an empty string
    Overload this field to restore an <input type="hidden">
    """
    hidden_widget = floppyforms.HiddenInput
