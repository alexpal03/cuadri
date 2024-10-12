import cuadri
import math


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



    @staticmethod
    def adapt(zin, zout):

        # Error, no se podrá lograr con esta configuración L
        if zout > zin:
            print("No se permite Zout > Zin... probar configuración Li")
            return None

        ratioz = zin/zout
        tetha = math.acosh(ratioz**0.5)
        sinht = math.sinh(tetha)
        sqmulz = (zin*zout)**0.5
        z1 = sqmulz * sinht
        z2 = sqmulz / sinht
        return CuadriL(z1, z2)

    @property
    def tetha(self):
        return math.acosh((self.zim1/self.zim2)**0.5)



    @staticmethod
    def aten(vin, vout, zk2=1):
        ratiov = vin/vout
        z1 = zk2-zk2/ratiov
        z2 = zk2/(ratiov - 1)
        return CuadriL(z1, z2)

