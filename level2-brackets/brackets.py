SIGNATURES = ['()', '{}', '[]']


def drop_irrelevant_chars(s, chars):
    return ''.join(list(filter(lambda x: x in chars, s)))


def rec(expression):
    if not expression:
        return True
    for signature in SIGNATURES:
        idx = expression.find(signature)
        if idx != -1:
            return rec(expression[0:idx] + expression[idx+2:])
    return False


def brackets(expression):
    expression = drop_irrelevant_chars(expression, ''.join(SIGNATURES))
    return rec(expression)
