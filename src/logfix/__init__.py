#!/usr/bin/env python3
import glob
import logging
import os
import re
from pathlib import Path

JAVA_STACKTRACE_PATTERN = '^.*[\r\n]+.*?Exception.*(?:[\r\n]+^\s*at .*)+'
JAVA_STACKTRACE_REGEX = re.compile(JAVA_STACKTRACE_PATTERN, re.MULTILINE)

LOG = logging.getLogger('logfix')
""" The main logger. 
"""


def _replace(string, substitutions):
    """ Replace multiple strings from a dictionary.

    :ref: https://gist.github.com/carlsmith/b2e6ba538ca6f58689b4c18f46fef11c
    """
    LOG.debug('replace()')
    substrings = sorted(substitutions, key=len, reverse=True)
    regex = re.compile('|'.join(map(re.escape, substrings)))
    return regex.sub(lambda match: substitutions[match.group(0)], string)


def file_fix(src: str, dst: str = None):
    """ Repair a logfile.
    :param src: The file to fix.
    :param dst: Output file to store fixed logs.

    """
    LOG.debug(f'file_fix(src={src},dst={dst})')
    if not src:
        raise Exception('Missing source file to fix.')
    if not dst or len(dst) == 0:
        dst = f'{src}.fixed'
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
    return dst


def directory_fix(directory: str, file_pattern: str = '*'):
    """ Fix logs files founded into the specified directory.

    :param directory: The directory containing logs files.
    :param file_pattern: The pattern to match files.
    """
    LOG.debug(f'directory_fix(directory={directory}, file_pattern={file_pattern}')
    fixed_files = []
    if not directory or not os.path.exists(directory):
        raise Exception(f'Path {directory} does not exist')
    p = Path(directory)
    LOG.debug('files', extra={'files': [str(f) for f in p.glob('*')]})
    for file in p.glob('*'):
        LOG.debug(str(file))
        file_fix(file)
        fixed_files.append(file)
    return fixed_files
