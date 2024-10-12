import cuadri


class CuadriTPuente(cuadri.Cuadri):
    """
    Cuadripolo de tipo T puenteada
  
        ┌───────Z4──────┐
        │               │
    ■───┴──Z1───┬───Z3──┴───■
                Z2
                │ 
    ■───────────┴───────────■  
    """
    def __init__(self, z1, z2, z3, z4):

        self._z1 = z1
        self._z2 = z2
        self._z3 = z3
        self._z4 = z4

        cT = cuadri.CuadriT(z1, z2, z3)
        cpi = cT.conv_pi()
        cpieq = cuadri.CuadriPi(cpi.z1, cpi.z2*z4/(cpi.z2+z4), cpi.z3)

        super().__init__(cpieq.A, cpieq.B, cpieq.C, cpieq.D)


    @property
    def z1(self):
        return self._z1
    
    @property
    def z2(self):
        return self._z2
    
    @property
    def z3(self):
        return self._z3
    
    @property
    def z4(self):
        return self._z4
    


    @staticmethod
    def adapt(zin, zout, corr=0.634):
        print("Función no disponible en tipo T Puente")
        return None
    
    @property
    def tetha(self):
        print("Atributo no disponible en tipo T Puente")
        return None

    @staticmethod
    def aten(vin, vout, zk2=1):
        print("Función no disponible en tipo T Puente")
        return None
