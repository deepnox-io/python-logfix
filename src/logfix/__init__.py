#!/usr/bin/env python3
import glob
import logging
import os
import re

JAVA_STACKTRACE_PATTERN = '^.*[\r\n]+.*?Exception.*(?:[\r\n]+^\s*at .*)+'
JAVA_STACKTRACE_REGEX = re.compile(JAVA_STACKTRACE_PATTERN, re.MULTILINE)

MAIN_LOG = logging.getLogger('logfix')
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


def file_fix(src: str, dst: str):
    """ Repair a logfile.
    :param src: The file to fix.
    :param dst: Output file to store fixed logs.

    """
    MAIN_LOG.debug(f'file_fix(src={src},dst={dst})')
    if not src:
        raise Exception('Missing source file to fix.')
    if not dst or len(dst) == 0:
        dst = f'{dst}.fixed'
    stacks = {}
    rx_blanks = re.compile(r'\W+')  # to remove blanks and newlines
    file_source = open(src, 'r')
    lines = '\n'.join(file_source.readlines())
    for match in JAVA_STACKTRACE_REGEX.finditer(lines):
        stacks[match.group(0)] = match.group(0).replace('\n', '\\n').replace('\t', ' ')

    s = _replace(lines, stacks)
    dst = open(dst, 'w')
    dst.write(s)
    dst.close()


def directory_fix(dir: str, file_pattern: str = '*'):
    """ Fix logs files founded into the specified directory.

    :param dir: The directory containing logs files.
    """
    MAIN_LOG.debug(f'directory_fix(dir={dir}, file_pattern={file_pattern}')
    if not dir or not os.path.exists(dir):
        raise Exception(f'Path {dir} does not exist')
    for file in glob.glob(os.path.join(dir), file_pattern):
        file_fix(file)
