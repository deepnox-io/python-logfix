#!/usr/bin/env python3
import os
import re

JAVA_STACKTRACE_PATTERN = '^.*[\r\n]+.*?Exception.*(?:[\r\n]+^\s*at .*)+'
JAVA_STACKTRACE_REGEX = re.compile(JAVA_STACKTRACE_PATTERN, re.MULTILINE)

FILENAME = os.path.join(os.path.dirname(__name__), '..', 'test_resources', 'one-exception.log')

rx_blanks = re.compile(r"\W+")  # to remove blanks and newlines
for match in JAVA_STACKTRACE_REGEX.finditer(open(FILENAME).read()):
    stacktrace = match.group(0).replace('\n', '\\n')
    print(stacktrace)
