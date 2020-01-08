#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

from ..wrappers import args_to_dtype


@args_to_dtype(pd.Series)
def sdev(src, n=2):
    'Returns the standard deviation of a `src` given `n` periods'

    _sdev = src.rolling(n).std().values
    return _sdev
