import cuadri
import math

class CuadriPi(cuadri.Cuadri):
    """
    Cuadripolo de tipo Pi

    ■────┬───Z2───┬────■
         Z1       Z3
         │        │ 
    ■────┴────────┴────■ 
    """
    def __init__(self, z1, z2, z3):

        self._z1 = z1
        self._z2 = z2
        self._z3 = z3

        etapa1 = cuadri.CuadriL(0, z1)
        etapa2 = cuadri.CuadriL(z2, z3)

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



    def conv_T(self):
        den = self.z1 + self.z2 + self.z3
        za = self.z1*self.z2/den
        zb = self.z1*self.z3/den
        zc = self.z2*self.z3/den
        return cuadri.CuadriT(za,zb,zc)


    
    @staticmethod
    def adapt(vin, vout, zk2=1):
        print("Función no disponible en tipo Pi")
        return None


    @staticmethod
    def aten(vin, vout, zk2=1):
        ratiov = vin/vout
        alpha = math.log(ratiov)
        z1 = z3 = zk2/math.tanh(alpha/2)
        z2 = zk2*math.sinh(alpha)
        return CuadriPi(z1, z2, z3)
