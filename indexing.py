#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import re

TOKENIZING_REGEX = "[A-Z]{2,}(?![a-z])|[A-Z][a-z]+(?=[A-Z])|[\'\w\-]+"
def tokenize_file(file_path, encoding='utf-8'):
        with codecs.open(file_path, 'r', encoding=encoding) as fileobj:
            for line in fileobj:
                line = line.lower().replace('#', ' ')
                for token in re.findall(TOKENIZING_REGEX, line):
                    token = token.strip()
                    if not token:
                        continue
                    yield token