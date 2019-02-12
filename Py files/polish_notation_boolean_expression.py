'''
Use function parse() in main to get logical expression in prefix polish notation.
As parameters it takes string - correct boolean formula.
& = AND
| = OR
! = NOT
> = SUBSEQUENTLY
Use function evaluate() to get result from expression in polish notation and dictionary with values.
'''


# Input = string with correct boolean formula. Output = expression in polish notation.
def parse(s):
    for operator in [">", "|", "&", "!"]:
        depth = 0
        for p in range(0, len(s), 1):
            if s[p] == ')':
                depth -= 1
            if s[p] == '(':
                depth += 1
            if not depth and s[p] == operator:
                if s[p] == "!":
                    return [s[p]] + parse(s[p + 1:])
                else:
                    return [s[p]] + parse(s[:p]) + parse(s[p + 1:])
    s = s.strip()
    if s[0] == '(':
        return parse(s[1:-1])
    return [s]


# Input = expression in polish notation(array) and dictionary with variables and their values. Output = value
def evaluate(stack, d):
    for i in range(len(stack)-1, -1, -1):
        z = stack[i]
        if stack[i] == '&':
            o2 = stack.pop(i + 2)
            o1 = stack.pop(i + 1)
            stack.pop(i)
            stack.append(str(min(d[o1], d[o2])))
        if stack[i] == '|':
            o2 = stack.pop(i + 2)
            o1 = stack.pop(i + 1)
            stack.pop(i)
            stack.append(str(max(d[o1], d[o2])))
        if stack[i] == '>':
            o2 = stack.pop(i + 2)
            o1 = stack.pop(i + 1)
            stack.pop(i)
            stack.append(str(max(not d[o1], d[o2])))
        if stack[i] == '!':
            o1 = stack.pop(i + 1)
            stack.pop(i)
            stack.append(str(not d[o1]))
    return stack[0]

# example
d = {'a': True, 'b': True, 'c': True, 'd': True, 'w': True, 'True': True, 'False': False, '1': True, '0': False}
s = '!(a&b>c)|!(d&w)'

print("your expression: ", s)

polish_notation = parse(s)
print("expression in polish notation:", "".join(polish_notation))

res = evaluate(polish_notation, d)
print("Answer is", res)
