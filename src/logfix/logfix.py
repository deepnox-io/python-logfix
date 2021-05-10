def previous_space_pos(s, pos):
    if not pos:
        return
    while s[pos] not in ' \t\r\n' and pos > 0:
        pos -= 1
    return pos


def check_substring(s, sub, pos):
    if pos >= len(sub) and s[pos - len(sub):pos] == sub:
        return pos - len(sub)


class StacktraceFinder(object):

    def __init__(self, s):
        self.s = s
        self.positions = []

    def run(self):
        start, end = None, None
        pos = 0
        into_exception = False
        for line in self.s:
            if not into_exception:
                i = line.find('Exception')
                if i >= 0:
                    into_exception = True
                    start = pos - 1
            else:
                if line.find('at ') <= -1 and line.find(' more') <= -1 and line.find('Caused by') <= -1:
                    into_exception = False
                    end = pos - 1
                    self.positions.append((start, end))
            pos += 1
