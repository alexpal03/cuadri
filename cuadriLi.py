import cuadri
import math


class CuadriLi(cuadri.Cuadri):
    """
    Cuadripolo de tipo Li

    ■────┬───Z2───■
         Z1
         │ 
    ■────┴────────■ 
    """
    def __init__(self, z1, z2):

        self._z1 = z1
        self._z2 = z2

        etapa1 = cuadri.CuadriL(0, z1)
        etapa2 = cuadri.CuadriL(z2, float('inf'))

        etotal = etapa1.casc(etapa2)

        super().__init__(etotal.A, etotal.B, etotal.C, etotal.D)



    @property
    def z1(self):
        return self._z1
    
    @property
    def z2(self):
        return self._z2


    @staticmethod
    def adapt(zin, zout):

        # Error, no se podrá lograr con esta configuración Li
        if zin > zout:
            print("No se permite Zin > Zout... probar configuración L")
            return None

        ratioz = zout/zin
        tetha = math.acosh(ratioz**0.5)
        sinht = math.sinh(tetha)
        sqmulz = (zin*zout)**0.5
        z1 = sqmulz / sinht
        z2 = sqmulz * sinht
        return CuadriLi(z1, z2)
    
    @property
    def tetha(self):
        return math.acosh((self.zim2/self.zim1)**0.5)
    


    @staticmethod
    def aten(vin, vout, zk2=1):
        ratiov = vin/vout
        z2 = zk2*(ratiov - 1)
        z1 = (z2 + zk2)/(ratiov -1)
        return CuadriLi(z1, z2)

