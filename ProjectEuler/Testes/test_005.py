#from ProjectEuler import Euler005 as segundoteste

#def test_numero():
   # assert segundoteste.mmc(6, 8)==24
#test_numero()

from ProjectEuler import Euler005 as multiplos
def test_mmc_lista():
    lista = [6, 8, 10, 12]
    assert multiplos.mmc_lista(lista) == 120
test_mmc_lista()