#!/usr/bin/env python
#
# A simple Python script to insert whitespace between CJK (Chinese, Japanese, Korean)
# and half-width characters (alphabetical letters, numerical digits and symbols).
#
# Modified from https://github.com/vinta/pangu.py, as the original codes
# is not suitable for reStructuredText text files.
#
#
# The MIT License (MIT)
#
# Copyright (c) 2013 Vinta
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
#

import re
import sys

CJK = r"\u2e80-\u2eff\u2f00-\u2fdf\u3040-\u309f\u30a0-\u30fa\u30fc-\u30ff\u3100-\u312f\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff"

ANY_CJK = re.compile(r"[{CJK}]".format(CJK=CJK))

CJK_EN = re.compile("([{CJK}])([A-Za-z0-9])".format(CJK=CJK))
EN_CJK = re.compile("([A-Za-z0-9])([{CJK}])".format(CJK=CJK))


def spacing(text):
    if len(text) <= 1 or not ANY_CJK.search(text):
        return text

    new_text = text

    new_text = CJK_EN.sub(r"\1 \2", new_text)
    new_text = EN_CJK.sub(r"\1 \2", new_text)

    return new_text


if len(sys.argv) == 1:
    sys.exit(f"Usage: python {sys.argv[0]} files")

for infile in sys.argv[1:]:
    with open(infile, "r") as f:
        text = f.read()

    with open(infile, "w") as f:
        f.write(spacing(text))
