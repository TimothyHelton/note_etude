#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module will create musical note images.

.. moduleauthor:: Timothy Helton <timothy.j.helton@gmail.com>
"""

import itertools
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import os
import subprocess
import termcolor


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
        self.notes_lilypond = [''.join([x[1], x[0]]) for x in
                               list(itertools.product(self.octave, self.scale))]
        self.sci_notes = [''.join([x[1], str(x[0])]) for x in
                          list(itertools.product(range(10), self.scale))]
        self.notes = {x: y for (x, y) in zip(self.sci_notes,
                                             self.notes_lilypond)}
        self.clef = clef
        self.pitch_low = pitch_low
        self.pitch_high = pitch_high
        self.pitch_range = None

        self.calc_range()

    def calc_range(self):
        """All instrument notes for instrument range in Lilypond format."""
        self.pitch_range = self.sci_notes[self.sci_notes.index(self.pitch_low):
                                          self.sci_notes.index(self.pitch_high)]

    def create_images(self):
        """Create note images using Lilypond."""
        try:
            os.makedirs(self.clef, exist_ok=False)
        except FileExistsError:
            return

        os.chdir(self.clef)
        for (key, value) in sorted(self.notes.items()):
            status = termcolor.colored('Create: {}'.format(key), 'blue',
                                       attrs=['bold'])
            print(status)
            file_name = '{}.ly'.format(key)

            with open(file_name, 'w') as f:
                f.write(self.lilypond_input(value))

            subprocess.call(['lilypond', '-s', '--png', file_name])
            os.remove(file_name)

            self.format_image('{}.png'.format(key))

        os.chdir('..')

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

    @staticmethod
    def format_image(note_image):
        """Format the Lilypond images uniformly.

        :param str note_image: name of note png image to format
        """
        im = mpimg.imread(note_image)

        # find image boundaries
        im_filter = np.where(im < 1)
        x_min = np.min(im_filter[1])
        x_max = np.max(im_filter[1])
        y_clef_idx = np.median(np.where(im_filter[1] == x_min))
        y_clef = im_filter[0][int(y_clef_idx)]

        # crop image
        x_pad = 15
        vertical_total = 400
        upper_pad = int(vertical_total / 2) - y_clef
        row, col, rgb = im.shape
        im = np.insert(im, 0, np.broadcast_to(im[0], (upper_pad, col, rgb)),
                       axis=0)
        img_resize = im[:vertical_total, (x_min - x_pad):(x_max + x_pad)]

        # set transparent background
        row, col, rgb = img_resize.shape
        img_transparent = np.append(img_resize, np.zeros((row, col, 1)), axis=2)
        mask = np.where(img_resize < 1)
        img_transparent[mask[0], mask[1], -1] = 1

        # save image
        plt.imsave(note_image, img_transparent)


if __name__ == '__main__':
    violin = Instrument('treble', 'g3', 'a6')
    viola = Instrument('alto', 'c3', 'd6')
    cello = Instrument('bass', 'c2', 'c6')
    bass = Instrument('bass', 'e1', 'c5')
