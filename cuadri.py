
import numpy as np
import math

class Cuadri():

    def __init__(self, A, B, C, D):

        self._mdir = np.array([[A,B],[C,D]])



    @property
    def A(self):
        return self._mdir[0][0]
    
    @property
    def B(self):
        return self._mdir[0][1]
    
    @property
    def C(self):
        return self._mdir[1][0]
    
    @property
    def D(self):
        return self._mdir[1][1]
    


    
    @property
    def matriz_dir(self):
        return self._mdir
    
    @property
    def matriz_inv(self):
        return np.linalg.inv(self._mdir)
    
    @property
    def matriz_z(self):
        z11 = self.A/self.C
        z12 = np.linalg.det(self._mdir)/self.C
        z21 = 1/self.C
        z22 = self.D/self.C
        return np.array([[z11, z12],[z21 , z22]])
    
    @property
    def matriz_y(self):
        return np.linalg.inv(self.matriz_z)
    
    
    @property
    def matriz_h(self):
        h11 = self.B/self.D
        h12 = np.linalg.det(self._mdir)/self.D
        h21 = -1/self.D
        h22 = self.C/self.D
        return np.array([[h11, h12],[h21 , h22]])
    
    @property
    def matriz_g(self):
        return np.linalg.inv(self.matriz_h)
    




    @property
    def zim1(self):
        return ((self.A * self.B) / (self.C * self.D))**0.5

    @property
    def zim2(self):
        return ((self.B * self.D) / (self.A * self.C))**0.5
    
    @property
    def zk1(self):
        aux = (self.A - self.D)/(2*self.C)
        return -1*aux + (aux**2 + self.B/self.C)**0.5

    @property
    def zk2(self):
        aux = (self.D - self.A)/(2*self.C)
        return -1*aux + (aux**2 + self.B/self.C)**0.5
    





    def ftransfv(self, zout):
        return 1/self.fpropv(zout)
    
    def ftransfi(self, zout):
        return 1/self.fpropi(zout)

    def fpropv(self, zout):
        return self.A + self.B/zout
    
    def fpropi(self, zout):
        return self.C*zout + self.D
    
    def alphav(self, zout):
        return math.log(self.fpropv(zout))
    
    def alphai(self, zout):
        return math.log(self.fpropi(zout))
    
    def betav(self, zout):
        fpropv = self.fpropv(zout)
        return math.atan(fpropv.imag/fpropv.real)
    
    def betai(self, zout):
        fpropi = self.fpropi(zout)
        return math.atan(fpropi.imag/fpropi.real)
    




    def casc(self, other):
        [[A, B], [C, D]] = np.matmul(self._mdir, other._mdir)
        return Cuadri(A, B, C, D)
    
    def serie(self, other):
        [[z11, z12], [z21, z22]] = np.add(self.matriz_z, other.matriz_z)
        return Cuadri.por_z(z11, z12, z21, z22)
    
    def paralelo(self, other):
        [[y11, y12], [y21, y22]] = np.add(self.matriz_y, other.matriz_y)
        return Cuadri.por_y(y11, y12, y21, y22)
    
    def serie_paralelo(self, other):
        [[h11, h12], [h21, h22]] = np.add(self.matriz_h, other.matriz_h)
        return Cuadri.por_h(h11, h12, h21, h22)
    
    def paralelo_serie(self, other):
        [[g11, g12], [g21, g22]] = np.add(self.matriz_g, other.matriz_g)
        return Cuadri.por_g(g11, g12, g21, g22)
    






    @staticmethod
    def por_z(z11, z12, z21, z22):
        A = z11/z21
        B = (z11*z22-z12*z21)/z21
        C = 1/z21
        D = z22/z21
        return Cuadri(A, B, C, D)
    
    @staticmethod
    def por_y(y11, y12, y21, y22):
        A = -y22/y21
        B = -1/y21
        C = -1*(y11*y22-y12*y21)/y21
        D = -y11/y21
        return Cuadri(A, B, C, D)
    
    @staticmethod
    def por_h(h11, h12, h21, h22):
        A = -1*(h11*h22-h12*h21)/h21
        B = -h11/h21
        C = -h22/h21
        D = -1/h21
        return Cuadri(A, B, C, D)
    
    @staticmethod
    def por_g(g11, g12, g21, g22):
        A = 1/g21
        B = g22/g21
        C = g11/g21
        D = (g11*g22-g12*g21)/g21
        return Cuadri(A, B, C, D)
        
    @staticmethod
    def por_inv(E, F, G, H):
        [[A, B], [C, D]] = np.linalg.inv([[E,F],[G,H]])
        return Cuadri(A, B, C, D)
