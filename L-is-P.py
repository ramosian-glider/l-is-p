NIL = '()'
T = 'T'

def is_atom(expr):
  return isinstance(expr, str)

def string(expr):
  if is_atom(expr):
    return expr
  strs = []
  for i in expr:
    strs.append(string(i))
  return '(%s)' % ', '.join(strs)

def head(expr):
  if is_atom(expr):
    return expr
  else:
    return expr[0]

def tail(expr):
  if is_atom(expr):
    return ()
  else:
    return expr[1:]


def QUOTE(expr):
  return expr

def CAR(expr):
  print 'car: ', expr
  return head(expr)


BUILTINS = {
  'quote': QUOTE,
  'car': CAR,
}

def evaluate(expr):
  print 'evaluating', expr
  if is_atom(expr):
    return expr
  elif len(expr) == 0:
    return NIL
  elif len(expr) > 0:
    if head(expr) == QUOTE:
      return tail(expr)[0]
    elif head(expr) in BUILTINS:
      return BUILTINS[head(expr)](evaluate(tail(expr)[0]))

def test(expr):
  print string(evaluate(expr))

test('T')
test(())
test('zzz')
test(('car', ('quote', ('a', 'b', 'c'))))
