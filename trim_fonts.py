#!/usr/bin/env nix-shell
#!nix-shell -p fontforge -i fontforge
import codecs
import glob
import os
import os.path

import fontforge

def all_files_of(root):
    for (dirpath, dirnames, filenames) in os.walk(root):
        for filename in filenames:
            yield os.path.join(dirpath, filename)

def all_files():
    yield from all_files_of("content")
    yield from all_files_of("i18n")
    yield from all_files_of("layouts")
    yield from all_files_of("themes/m14n/layouts")

glyphs = set()
for content_file in all_files():
    if os.path.isfile(content_file):
        print(content_file)
        try:
            with codecs.open(content_file, encoding='utf-8', errors='strict') as f:
                glyphs |= set(f.read())
        except UnicodeDecodeError:
            pass

for font_path in glob.glob("themes/m14n/assets/fonts/literata/variable/*.ttf"):
    font = fontforge.open(font_path)
    for glyph in glyphs:
        font.selection[ord(glyph)] = True
    font.selection.invert()
    for glyph in font.selection.byGlyphs:
        font.removeGlyph(glyph)
    font.generate(font_path + '.trimmed.ttf')

