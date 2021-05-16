#!/usr/bin/env python3

import logging
import os
import re
from pathlib import Path

from logfix.logfix import StacktraceFinder

JAVA_STACKTRACE_PATTERN = '(^\d+\) .+)|(^.+Exception: .+)|(^\s+at .+)|(^\s+... \d+ more)|(^\s*Caused by:.+)'
JAVA_STACKTRACE_REGEX = re.compile(JAVA_STACKTRACE_PATTERN, re.MULTILINE)

LOG = logging.getLogger('logfix')
""" The main logger. 
"""


def _find_exception_pattern(lines):
    LOG.debug('_find_exception_pattern()')
    if type(lines) == str:
        return JAVA_STACKTRACE_REGEX.finditer(lines)
    elif type(lines) == list:
        return JAVA_STACKTRACE_REGEX.finditer('\n'.join(lines))
    raise TypeError(f'lines must be of type: (list|str)')


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

    lines = open(src, 'r').readlines()
    stf = StacktraceFinder(lines)
    stf.run()

    fixed = open(dst, 'w')

    if stf.positions and len(stf.positions) > 0:
        current_stacktrace_index = 0

    stacktrack_as_list = []
    for i, line in enumerate(lines):
        if current_stacktrace_index < len(stf.positions):
            current_stacktrace = stf.positions[current_stacktrace_index]
        else:
            current_stacktrace = None
        if current_stacktrace and current_stacktrace[0] <= i <= current_stacktrace[1]:
            stacktrack_as_list.append(line)
        elif current_stacktrace and i > current_stacktrace[1]:
            # fixed.write('||'.join(stacktrack_as_list))
            stacktrack_as_list = []  # Reinit stacktrace as list
            current_stacktrace_index += 1  # Go to next identified stacktrace
        else:
            fixed.write(line)
    fixed.close()
    return str(dst)


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
    for file in p.glob(file_pattern):
        LOG.debug(str(file))
        fixed_filename = file_fix(file)
        fixed_files.append(fixed_filename)
    return fixed_files
