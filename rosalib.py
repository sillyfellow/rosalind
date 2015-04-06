
def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def hyopotenuse(a, b):
    return (a * a) + (b * b)


def get_input_integers(count):
    numbers = raw_input().split()
    if len(numbers) != count or (not reduce(lambda x, y: is_integer(x) and y, numbers, True)):
        raise "Input must be %d integers" % count
    return [int(x) for x in numbers]


def print_dict(d):
    for key, value in d.iteritems():
        print key, value


def base_complement(c):
    d = { 'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'a': 't', 'c': 'g', 'g': 'c', 't': 'a' }
    return d[c]


