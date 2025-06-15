################################################################################
# MIT License
#
# Copyright (c) 2016 Meezio SAS <dev@meez.io>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
################################################################################

from flask import request


class Lang:
    @staticmethod
    def best_match(available_languages, default=None):
        """ Determine best language from list of available languages and from Accept-Language Header.

        :param list available_languages: List of available languages to match with.
        :param str default: Language returned when no match found.
        :return str: The best matching language or None if no matching.
        """
        for lang in request.accept_languages.values():
            if lang in available_languages:
                return lang
            elif len(lang) > 2 and lang[:2] in available_languages:
                return lang[:2]

        return default
