from ProjectEuler import Euler007 as primo

def test_n_primo():
    assert primo.enesimo_primo(1) == 2
    assert primo.enesimo_primo(6) == 13
    assert primo.enesimo_primo(7) == 17
test_n_primo()