
# cuadri

### Importar módulo
```python
from cuadri import *
```

### Crear cuadripolo por parámetros directos
```python
c = Cuadri(a, b, c, d)
```

### Crear cuadripolo por impedancias

Los parámetros `zx` pueden ser valores reales o complejos.

* CuadriD

  ```python
  c = CuadriD(z1, z2, z3)
  ```

  ![cuadri D](https://github.com/user-attachments/assets/f1131083-3cf0-4114-8c13-e7c8f98b96d7)

* CuadriL

  ```python
  c = CuadriL(z1, z2)
  ```
  
  ![cuadri L](https://github.com/user-attachments/assets/9bb2e596-4af2-4e19-9bc0-7ecff6ac7494)

* CuadriPi

  ```python
  c = CuadriPi(z1, z2, z3)
  ```
  
  ![cuadri pi](https://github.com/user-attachments/assets/6b389430-52b8-411c-b9ae-a44a350b5ee9)

* CuadriT

  ```python
  c = CuadriT(z1, z2, z3)
  ```
  
  ![cuadri T](https://github.com/user-attachments/assets/70bd730c-f748-4cf4-a730-2dc4c868b0fd)

* CuadriTPuente

  ```python
  c = CuadriTPuente(z1, z2, z3, z4)
  ```
  
  ![cuadri T puenteada](https://github.com/user-attachments/assets/e6db0efd-d29a-45e8-9c9d-5cb586bb3639)


### Parámetros

* Directos: `c.matriz_dir`  
* Inversos: `c.matriz_inv`  
* Z:        `c.matriz_z`
* Y:        `c.matriz_y`
* H:        `c.matriz_h`
* G:        `c.matriz_g`

### Impedancias

* `c.zim1`
* `c.zim2`
* `c.zk1`
* `c.zk2`

### Funciones

Necesitan un parámetro `zout` que identifica la carga:

* Transferencia de tensiones `c.ftransfv(zout)`
* Transferencia de corrientes `c.ftransfi(zout)`
* Propagación de tensiones `c.fpropv(zout)`
* Propagación de corrientes `c.fpropi(zout)`
* Alpha de tensiones `c.alphav(zout)`
* Alpha de corrientes `c.alphai(zout)`
* Beta de tensiones `c.betav(zout)`
* Beta de corrientes `c.betai(zout)`


### Asociaciones

Se pasa como parámetros el cuadripolo que se quiere asociar.

Retorna un nuevo cuadripolo que representa la asociación.

* Cascada `c1.casc(c2)`
* Serie `c1.serie(c2)`
* Paralelo `c1.paralelo(c2)`
* Serie paralelo `c1.serie_paralelo(c2)`
* Paralelo serie `c1.paralelo_serie(c2)`

### Instancias a partir de otros parámetros

* Parámetros z `Cuadri.por_z(z11, z12, z21, z22)`
* Parámetros y `Cuadri.por_y(y11, y12, y21, y22)`
* Parámetros h `Cuadri.por_h(h11, h12, h21, h22)`
* Parámetros g `Cuadri.por_g(g11, g12, g21, g22)`
* Parámetros inversos `Cuadri.por_inv(e, f, g, h)`



### Ejemplo 1:

![ej1](https://github.com/user-attachments/assets/815e1da4-a71c-430c-9d63-82e78aad704a)


Resolución:

```python
from cuadri import *

c = CuadriTPuente(600,450,1800,4800)

print("Matriz z: ")
print(c.matriz_z)
print("Matriz directa: ")
print(c.matriz_dir)
print("zk1:  ", c.zk1)
print("zk2:  ", c.zk2)
print("zim1: ", c.zim1)
print("zim2: ", c.zim2)

print("prop v iter:  ", c.fpropv(c.zk2))
print("prop i iter:  ", c.fpropi(c.zk2))
print("alpha v iter: ", c.alphav(c.zk2))
print("alpha i iter: ", c.alphai(c.zk2))
print("prop v imag:  ", c.fpropv(c.zim2))
print("prop i imag:  ", c.fpropi(c.zim2))
print("alpha v imag: ",c.alphav(c.zim2))
print("alpha i imag: ", c.alphai(c.zim2))
```

![ej1 res](https://github.com/user-attachments/assets/078760c7-0953-4da6-8c94-c8af4b81b334)


### Ejemplo 2 (clase práctica 27/09):

![ej 2](https://github.com/user-attachments/assets/7212e6e5-6aea-4681-b271-74bdb09068c0)

```python
from cuadri import *

c1 = CuadriT(2200,4700,1500)
c2 = CuadriT(3300,6800,1000)
c3 = CuadriT(5600,2200,1800)

ctotal = c1.casc(c2).casc(c3)

print('Matriz directa:')
print(ctotal.matriz_dir)
print('alpha v iter: ', ctotal.alphav(ctotal.zk2))
```

![ej2 res](https://github.com/user-attachments/assets/15228cc6-f34e-4566-b184-67a6ffaee818)

