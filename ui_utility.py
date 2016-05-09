#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Peng Liu <liupeng@imscv.com>
#
# Distributed under terms of the GNU GPL3 license.

"""
This file defines some derived UI class to help GUI works better.
"""

import Tkinter as tk


# Seems useless
class Listbox(tk.Listbox):
    def autowidth(self,maxwidth):
        f = font.Font(font=self.cget("font"))
        pixels = 0
        for item in self.get(0, "end"):
            pixels = max(pixels, f.measure(item))
        # bump listbox size until all entries fit
        pixels = pixels + 10
        width = int(self.cget("width"))
        for w in range(0, maxwidth+1, 5):
            if self.winfo_reqwidth() >= pixels:
                break
            self.config(width=width+w)
