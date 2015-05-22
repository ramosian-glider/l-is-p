
class SExpr(object):
  def __init__(self, *args):
    self.expr = []
    for arg in args:
      self.args
    self.expr = args
    self.builtins = {
      'car': self.builtin_car,
    }
  def evaluate(self):
    if len(self.expr) == 0:
      return NIL
  def __str__(self):
    strs = []
    for elem in self.expr:
      strs.append(elem.evaluate())
    return '(%s)' % ', '.join(strs)
  def builtin_car(self):
    #TODO
    return NIL
    

class NilExpr(SExpr):
  def __init__(self):
    super(NilExpr, self).__init__([])
  def evaluate(self):
    return NIL
  def __str__(self):
    return '()'

NIL = NilExpr()

print SExpr(Atom
