#!/usr/bin/env python2
# encoding: utf-8
import codecs
import glob
import os
import os.path

import fontforge

def all_files():
    for (dirpath, dirnames, filenames) in os.walk("."):
        for filename in filenames:
            yield os.path.join(dirpath, filename)

glyphs = set()
for content_file in all_files():
    if os.path.isfile(content_file):
        print(content_file)
        with codecs.open(content_file, encoding='utf-8', errors='replace') as f:
            glyphs |= set(f.read())

for font_path in glob.glob("themes/m14n/assets/fonts/literata/variable/*.ttf"):
    font = fontforge.open(font_path)
    for glyph in glyphs:
        try:
            font.selection[ord(glyph)] = True
        except ValueError:
            pass
    font.selection.invert()
    for glyph in font.selection.byGlyphs:
        font.removeGlyph(glyph)
    font.generate(font_path + '.trimmed.ttf')

