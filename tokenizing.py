#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import re

TOKENIZING_REGEX = "[A-Z]{2,}(?![a-z])|[A-Z][a-z]+(?=[A-Z])|[\'\w\-]+"

def tokenize_sentence(line):
    line = line.lower().replace('#', ' ').strip()
    return re.findall(TOKENIZING_REGEX, line)

def tokenize_file(file_path, encoding='utf-8'):
        with codecs.open(file_path, 'r', encoding=encoding) as fileobj:
            for line in fileobj:
                for token in tokenize_sentence(line):
                    yield token