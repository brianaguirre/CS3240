__author__ = 'BrianAguirre'


def match_parenthesis(expr):
    left_count = 0
    right_count = 0
    for i in range (0, len(expr)):
        if expr[i] == '(':
            left_count += 1
        elif expr[i] == ')':
            right_count += 1

    if left_count == right_count:
        return True
    else:
        return False



#Testing:
"""
print(match_parenthesis("1+1)"))
print(match_parenthesis("(2+5)*6)"))
print(match_parenthesis("((2+4) -2 / 8)"))
print(match_parenthesis("((((2)*4)*5)*5)"))
"""
