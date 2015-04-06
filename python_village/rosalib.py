
def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def hyopotenuse(a, b):
    return (a * a) + (b * b)

