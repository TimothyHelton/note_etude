#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module will create musical note images.

.. moduleauthor:: Timothy Helton <timothy.j.helton@gmail.com>
"""

import os
import os.path as osp
import subprocess


__version__ = '1.0.0'


class Instrument:
    """Instrument Base Class

    :param str clef: clef for instrument music
    :param str pitch_low: lowest possible pitch in Lilypond format
    :param str pitch_high: highest possible pitch in Lilypond format
    """
    def __init__(self, clef, pitch_low, pitch_high):
        self.scale = ('c', 'd', 'e', 'f', 'g', 'a', 'b')
        self.notes = ([x + '4' for x in self.scale] +
                      [x + "'4" for x in self.scale] +
                      [x + "''4" for x in self.scale] +
                      [x + "'''4" for x in self.scale])
        self.clef = clef
        self.pitch_low = pitch_low
        self.pitch_high = pitch_high
        self.pitch_range = None

    def calc_range(self):
        """All instrument notes for instrument range in Lilypond format."""
        self.pitch_range = self.notes[self.notes.index(self.pitch_low):
                                      self.notes.index(self.pitch_high)]

    def note_images(self):
        """Create note image using Lilypond."""
        for note in self.pitch_range:
            lilypond_input = '''\\version "2.18.2"
            \\header {{
                tagline = ""
            }}
            \\absolute {{
                \\language "english"
                \\override Staff.TimeSignature #'stencil = ##f
                \\clef "{}"
                {}
            }}'''.format(self.clef, note)

            # TODO call subprocess.Popen to run Lilypond and create note images

    def crop_images(self):
        """Crop the Lilypond images uniformly."""
        pass


if __name__ == '__main__':
    violin = Instrument('treble', 'g4', "a'''4")
    viola = Instrument('alto', 'c4', "g'''4")
    cello = Instrument('bass', 'c4', "c'''4")
    bass = Instrument('bass', 'e4', "c''4")
