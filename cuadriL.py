import cuadri


class CuadriL(cuadri.Cuadri):
    """
    Cuadripolo de tipo L

    ■───Z1───┬────■
             Z2
             │ 
    ■────────┴────■ 
    """
    def __init__(self, z1, z2):

        self._z1 = z1
        self._z2 = z2

        c = cuadri.CuadriD(z1, z2, 0)

        super().__init__(c.A, c.B, c.C, c.D)



    @property
    def z1(self):
        return self._z1
    
    @property
    def z2(self):
        return self._z2
        

