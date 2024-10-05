import cuadri


class CuadriT(cuadri.Cuadri):
    """
    Cuadripolo de tipo T

    ■───Z1───┬───Z3───■
             Z2
             │ 
    ■────────┴────────■  
    """
    def __init__(self, z1, z2, z3):

        self._z1 = z1
        self._z2 = z2
        self._z3 = z3

        etapa1 = cuadri.CuadriL(z1, z2)
        etapa2 = cuadri.CuadriL(z3, float('Inf'))

        etotal = etapa1.casc(etapa2)

        super().__init__(etotal.A, etotal.B, etotal.C, etotal.D)


    @property
    def z1(self):
        return self._z1
    
    @property
    def z2(self):
        return self._z2
    
    @property
    def z3(self):
        return self._z3



    def conv_pi(self):
        num = self.z1*self.z2 + self.z1*self.z3 + self.z2*self.z3
        za = num/self.z3
        zb = num/self.z2
        zc = num/self.z1
        return cuadri.CuadriPi(za,zb,zc)