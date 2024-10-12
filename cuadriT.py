import cuadri
import math


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
    


    @staticmethod
    def adapt(zin, zout, corr=0.634):

        ratioz = zin/zout if zin > zout else zout/zin
        sqratioz_fpropv = (zin/zout)**0.5
        tetha = math.acosh(ratioz**0.5)
        # vin/vout
        fpropv = sqratioz_fpropv * math.e**tetha
        # Corrección para que no sea tipo L, Li
        # La corrección se puede variar a gusto, pero debe ser positiva
        # Probar con corrección = 0 daría z1 = 0 o z3 = 0, resultando en configuración tipo L, Li
        fpropv_rec = fpropv + corr
        tetha_rec = math.log(fpropv_rec / sqratioz_fpropv) 

        sinht = math.sinh(tetha_rec)
        cosht = math.cosh(tetha_rec)
        sqmulz = (zin*zout)**0.5
        z1 = (zin * cosht - sqmulz) / sinht
        z2 = sqmulz / sinht
        z3 = (zout * cosht - sqmulz) / sinht
        return CuadriT(z1, z2, z3)

    @property
    def tetha(self):
        return math.asinh(((self.zim1*self.zim2)**0.5)/self.z2)


    @staticmethod
    def aten(vin, vout, zk2=1):
        fpropv = vin/vout
        alpha = math.log(fpropv)
        z1 = z3 = zk2*math.tanh(alpha/2)
        z2 = zk2/math.sinh(alpha)
        return CuadriT(z1, z2, z3)
