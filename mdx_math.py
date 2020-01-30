# -*- coding: utf-8 -*-

'''
Math extension for Python-Markdown
==================================

Adds support for displaying math formulas using
[MathJax](http://www.mathjax.org/).

Author: 2015-2017, Dmitry Shachnev <mitya57@gmail.com>.
'''

from markdown.inlinepatterns import InlineProcessor
from markdown.extensions import Extension

class inlineMathProcessor( InlineProcessor ):
    def handleMatch( self, m, data ):
        # MathJAX handles all the math. Just set the uses_math flag, and
        # protect the contents from markdown expansion.
        self.md.uses_math = True
        return m.group(0), m.start(0), m.end(0)

class MathExtension(Extension):
    def __init__(self, *args, **kwargs):
        self.config = {
            'enable_dollar_delimiter':
                [False, 'Enable single-dollar delimiter'],
        }
        super(MathExtension, self).__init__(*args, **kwargs)

    def extendMarkdown(self, md):
        md.registerExtension(self)

        mathRegExps = [
            r'(?<!\\)\\\((.+?)\\\)',    # \( ... \)
            r'(?<!\\)\$\$.+?\$\$',      # $$ ... $$
            r'(?<!\\)\\\[.+?\\\]',      # \[ ... \]
            r'(?<!\\)\\begin{([a-z]+?\*?)}.+?\\end{\1}',
        ]
        if self.getConfig('enable_dollar_delimiter'):
            md.ESCAPED_CHARS.append('$')
            mathRegExps.append( r'(?<!\\|\$)\$.+?\$' ) # $ ... $
        for i, pattern in enumerate(mathRegExps):
            # we should have higher priority than 'escape' which has 180
            md.inlinePatterns.register(
                inlineMathProcessor( pattern, md ), f'math-inline-{i}', 185)

        md.uses_math = False
        self.md = md

    def reset(self):
        self.md.uses_math = False

def makeExtension(*args, **kwargs):
    return MathExtension(*args, **kwargs)
