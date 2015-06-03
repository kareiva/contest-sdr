# Copyright 2014 Clayton Smith
#
# This file is part of contest-sdr
#
# contest-sdr is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# contest-sdr is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with contest-sdr; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.

morsetab = {
        'A': [1,0,1,1,1,0,0,0],                              'a': [1,0,1,1,1,0,0,0],
        'B': [1,1,1,0,1,0,1,0,1,0,0,0],                      'b': [1,1,1,0,1,0,1,0,1,0,0,0],
        'C': [1,1,1,0,1,0,1,1,1,0,1,0,0,0],                  'c': [1,1,1,0,1,0,1,1,1,0,1,0,0,0],
        'D': [1,1,1,0,1,0,1,0,0,0],                          'd': [1,1,1,0,1,0,1,0,0,0],
        'E': [1,0,0,0],                                      'e': [1,0,0,0],
        'F': [1,0,1,0,1,1,1,0,1,0,0,0],                      'f': [1,0,1,0,1,1,1,0,1,0,0,0],
        'G': [1,1,1,0,1,1,1,0,1,0,0,0],                      'g': [1,1,1,0,1,1,1,0,1,0,0,0],
        'H': [1,0,1,0,1,0,1,0,0,0],                          'h': [1,0,1,0,1,0,1,0,0,0],
        'I': [1,0,1,0,0,0],                                  'i': [1,0,1,0,0,0],
        'J': [1,0,1,1,1,0,1,1,1,0,1,1,1,0,0,0],              'j': [1,0,1,1,1,0,1,1,1,0,1,1,1,0,0,0],
        'K': [1,1,1,0,1,0,1,1,1,0,0,0],                      'k': [1,1,1,0,1,0,1,1,1,0,0,0],
        'L': [1,0,1,1,1,0,1,0,1,0,0,0],                      'l': [1,0,1,1,1,0,1,0,1,0,0,0],
        'M': [1,1,1,0,1,1,1,0,0,0],                          'm': [1,1,1,0,1,1,1,0,0,0],
        'N': [1,1,1,0,1,0,0,0],                              'n': [1,1,1,0,1,0,0,0],
        'O': [1,1,1,0,1,1,1,0,1,1,1,0,0,0],                  'o': [1,1,1,0,1,1,1,0,1,1,1,0,0,0],
        'P': [1,0,1,1,1,0,1,1,1,0,1,0,0,0],                  'p': [1,0,1,1,1,0,1,1,1,0,1,0,0,0],
        'Q': [1,1,1,0,1,1,1,0,1,0,1,1,1,0,0,0],              'q': [1,1,1,0,1,1,1,0,1,0,1,1,1,0,0,0],
        'R': [1,0,1,1,1,0,1,0,0,0],                          'r': [1,0,1,1,1,0,1,0,0,0],
        'S': [1,0,1,0,1,0,0,0],                              's': [1,0,1,0,1,0,0,0],
        'T': [1,1,1,0,0,0],                                  't': [1,1,1,0,0,0],
        'U': [1,0,1,0,1,1,1,0,0,0],                          'u': [1,0,1,0,1,1,1,0,0,0],
        'V': [1,0,1,0,1,0,1,1,1,0,0,0],                      'v': [1,0,1,0,1,0,1,1,1,0,0,0],
        'W': [1,0,1,1,1,0,1,1,1,0,0,0],                      'w': [1,0,1,1,1,0,1,1,1,0,0,0],
        'X': [1,1,1,0,1,0,1,0,1,1,1,0,0,0],                  'x': [1,1,1,0,1,0,1,0,1,1,1,0,0,0],
        'Y': [1,1,1,0,1,0,1,1,1,0,1,1,1,0,0,0],              'y': [1,1,1,0,1,0,1,1,1,0,1,1,1,0,0,0],
        'Z': [1,1,1,0,1,1,1,0,1,0,1,0,0,0],                  'z': [1,1,1,0,1,1,1,0,1,0,1,0,0,0],
        '0': [1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,0,0],  ',': [1,1,1,0,1,1,1,0,1,0,1,0,1,1,1,0,1,1,1,0,0,0],
        '1': [1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,0,0],      '.': [1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,0,0],
        '2': [1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,0,0],          '?': [1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,0,0,0],
        '3': [1,0,1,0,1,0,1,1,1,0,1,1,1,0,0,0],              ';': [1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,0,0],
        '4': [1,0,1,0,1,0,1,0,1,1,1,0,0,0],                  ':': [1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,0,0,0],
        '5': [1,0,1,0,1,0,1,0,1,0,0,0],                      "'": [1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,0,0],
        '6': [1,1,1,0,1,0,1,0,1,0,1,0,0,0],                  '-': [1,1,1,0,1,0,1,0,1,0,1,0,1,1,1,0,0,0],
        '7': [1,1,1,0,1,1,1,0,1,0,1,0,1,0,0,0],              '/': [1,1,1,0,1,0,1,0,1,1,1,0,1,0,0,0],
        '8': [1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,0,0,0],          '(': [1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,0,0,0],
        '9': [1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,0,0],      ')': [1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,0,0,0],
        ' ': [0,0,0,0],                                      '_': [1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,0,0,0],
        '!': [1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,0,0,0],  '&': [1,0,1,1,1,0,1,0,1,0,1,0,0,0],
        '=': [1,1,1,0,1,0,1,0,1,0,1,1,1,0,0,0],              '+': [1,0,1,1,1,0,1,0,1,1,1,0,1,0,0,0],
        '"': [1,0,1,1,1,0,1,0,1,0,1,1,1,0,1,0,0,0],          '$': [1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,1,1,0,0,0],
        '@': [1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,0,0,0]
}

def morse_seq(text):
    seq = []
    for c in text:
        if c in morsetab:
            seq = seq + morsetab[c]
    return tuple(seq[0:-3])
