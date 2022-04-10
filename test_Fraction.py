from app.fraction import Fraction

def test_str():
g = Fraction(1, 2)
assert str(g) == '1/2'

def  test_reduce():
    f =  Fraction(4,2)
    f.reduce()
    assert f == Fraction(2,1)
  
def test_inner(moker):
    moker.patch('builtins.input' , side_effect=['5', '10'])
    f = IrreduceableFraction()
    f.inner()
    assert f == IrreduceableFraction(1, 2)
      
