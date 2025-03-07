def has_consecutive_characters(string):
    for index in range(len(string) - 1):
        if string[index] == string[index + 1]:
            return True
    return False

def find(xs, predicate):
    for x in xs:
        if predicate(x):
            return x
    return None