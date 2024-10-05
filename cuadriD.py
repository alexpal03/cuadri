import cuadri


class CuadriD(cuadri.Cuadri):
    """
    Cuadripolo de tipo D

    ■────────Z1───┬────■
                  Z2
                  │ 
    ■────────Z3───┴────■ 
    """
    def __init__(self, z1, z2, z3):

        self._z1 = z1
        self._z2 = z2
        self._z3 = z3

        # Unico caso donde hay que tomar limite si z2 es circuito abierto
        A = 1 if z2 == float('Inf') else (z1+z2+z3)/z2
        B = z1+z3
        C = 1/z2
        D = 1

        super().__init__(A,B,C,D)

        

    @property
    def z1(self):
        return self._z1
    
    @property
    def z2(self):
        return self._z2
    
    @property
    def z3(self):
        return self._z3