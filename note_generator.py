#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module will create musical note images.

.. moduleauthor:: Timothy Helton <timothy.j.helton@gmail.com>
"""

import itertools
import os
import os.path as osp
import subprocess


__version__ = '1.0.0'


class Instrument:
    """Instrument Base Class

    :param str clef: clef for instrument music
    :param str pitch_low: lowest possible pitch in scientific designation
    :param str pitch_high: highest possible pitch in scientific designation
    """
    def __init__(self, clef, pitch_low, pitch_high):
        self.scale = ('c', 'd', 'e', 'f', 'g', 'a', 'b')
        self.octave = (",,,", ",,", ",", "", "'", "''", "'''", "''''",
                       "'''''", "''''''")
        self.notes_lilypond = [''.join(x) for x in
                               list(itertools.product(self.scale, self.octave))]
        self.notes = None
        self.clef = clef
        self.pitch_low = pitch_low
        self.pitch_high = pitch_high
        self.pitch_range = None

    def calc_range(self):
        """All instrument notes for instrument range in Lilypond format."""
        self.pitch_range = self.notes[self.notes.index(self.pitch_low):
                                      self.notes.index(self.pitch_high)]

    def convert_octave(self):
        """Convert Lilypond octave notation to scientific designation."""
        note = self.notes_lilypond
        note = [x.replace(",,,", '0') for x in note]
        note = [x.replace(",,", '1') for x in note]
        note = [x.replace(",", '2') for x in note]
        note = [x.replace("''''''", '9') for x in note]
        note = [x.replace("'''''", '8') for x in note]
        note = [x.replace("''''", '7') for x in note]
        note = [x.replace("'''", '6') for x in note]
        note = [x.replace("''", '5') for x in note]
        note = [x.replace("'", '4') for x in note]
        note = [x + '3' if x.isalpha() else x for x in note]

        self.notes = {x: y for (x, y) in zip(self.notes_lilypond, note)}

    def create_images(self):
        """Create note images using Lilypond."""
        os.makedirs(self.clef, exist_ok=True)
        for pitch in self.pitch_range:
            file_name = osp.join(self.clef, '{}.ly'.format(pitch))

            with open(file_name, 'w') as f:
                f.write(self.lilypond_input(pitch))

    def lilypond_input(self, note):
        """Generate Lilypond input file to create note image.

        :param str note: musical note in Lilypond format
        :returns: Lilypond commands to create a note image
        :rtype: str
        """
        return '''\\version "2.18.2"
                  \\header {{
                      tagline = ""
                  }}
                  \\absolute {{
                      \\language "english"
                      \\override Staff.TimeSignature #'stencil = ##f
                      \\clef "{}"
                      {}
                  }}'''.format(self.clef, note)

    def crop_images(self):
        """Crop the Lilypond images uniformly."""
        pass


if __name__ == '__main__':
    violin = Instrument('treble', 'g3', "a6")
    viola = Instrument('alto', 'c3', "d6")
    cello = Instrument('bass', 'c2', "c6")
    bass = Instrument('bass', 'e1', "c5")
