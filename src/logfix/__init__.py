#!/usr/bin/env python3

import os
import re
import loggz
import uuid

JAVA_STACKTRACE_PATTERN = '^.*[\r\n]+.*?Exception.*(?:[\r\n]+^\s*at .*)+'
JAVA_STACKTRACE_REGEX = re.compile(JAVA_STACKTRACE_PATTERN, re.MULTILINE)

MAIN_LOG = loggz.factory('log-repair')
""" The main logger. 
"""


def _replace(string, substitutions):
    """ Replace multiple strings from a dictionary.

    :ref: https://gist.github.com/carlsmith/b2e6ba538ca6f58689b4c18f46fef11c
    """
    MAIN_LOG.debug('replace()')
    substrings = sorted(substitutions, key=len, reverse=True)
    regex = re.compile('|'.join(map(re.escape, substrings)))
    return regex.sub(lambda match: substitutions[match.group(0)], string)


def repair(filename, tmp_file: str):
    """ Repair a log file.
    """
    MAIN_LOG.debug('repair_log_file()')
    stacks = {}
    if tmp_file is None:
        tmp_file = os.path.join(os.path.dirname(filename), uuid.uuid4())
    rx_blanks = re.compile(r'\W+')  # to remove blanks and newlines
    file_source = open(filename, 'r')
    lines = '\n'.join(file_source.readlines())
    for match in JAVA_STACKTRACE_REGEX.finditer(lines):
        stacks[match.group(0)] = match.group(0).replace('\n', '\\n').replace('\t', ' ')

    s = _replace(lines, stacks)
    dst = open(tmp_file, 'w')
    dst.write(s)
    dst.close()
