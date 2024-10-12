
# cuadri

- [Importar módulo](##Importar-módulo)
- [Tipos de cuadripolos](##Tipos-de-cuadripolos)
- [Parámetros](##Parámetros)
- [Impedancias imagenes](#Impedancias-imagenes)
- [Impedancias iterativas](#Impedancias-iterativas)
- [Funciones](#Funciones)
   - [Propagación](##Propagación)
   - [Transferencia](##Transferencia)
   - [Alpha y Beta](##Alpha-y-Beta)
- [Asociaciones](#Asociaciones)
- [Cuadripolo por parámetros directos](#Cuadripolo-por-parámetros-directos)
- [Cuadripolo a partir de otros parámetros](#Cuadripolo-a-partir-de-otros-parámetros)
- [Adaptadores](#Adaptadores)
  - [Tipo L](##Tipo-L)
  - [Tipo Li](##Tipo-Li)
  - [Tipo T](##Tipo-T)
- [Atenuadores](#Atenuadores)
  - [Tipo L](##Tipo-L)
  - [Tipo Li](##Tipo-Li)
  - [Tipo T](##Tipo-T)
  - [Tipo Pi](##Tipo-Pi)

# Importar módulo
```python
from cuadri import *
```

# Tipos de cuadripolos

Los parámetros `zx` pueden ser valores reales o complejos.

* Cuadripolo tipo D

  ```python
  c = CuadriD(z1, z2, z3)
  ```

  ![cuadri D](https://github.com/user-attachments/assets/f1131083-3cf0-4114-8c13-e7c8f98b96d7)

* Cuadripolo tipo L

  ```python
  c = CuadriL(z1, z2)
  ```
  
  ![cuadri L](https://github.com/user-attachments/assets/9bb2e596-4af2-4e19-9bc0-7ecff6ac7494)


* Cuadripolo tipo L inverso (Li)

  ```python
  c = CuadriLi(z1, z2)
  ```
  ![cuadri Li](https://github.com/user-attachments/assets/3712ad49-4024-4a42-93ef-cc7c77d0d92b)

  
* Cuadripolo tipo pi

  ```python
  c = CuadriPi(z1, z2, z3)
  ```
  
  ![cuadri pi](https://github.com/user-attachments/assets/6b389430-52b8-411c-b9ae-a44a350b5ee9)

* Cuadripolo tipo T

  ```python
  c = CuadriT(z1, z2, z3)
  ```
  
  ![cuadri T](https://github.com/user-attachments/assets/70bd730c-f748-4cf4-a730-2dc4c868b0fd)

* Cuadripolo tipo T puente

  ```python
  c = CuadriTPuente(z1, z2, z3, z4)
  ```
  
  ![cuadri T puenteada](https://github.com/user-attachments/assets/e6db0efd-d29a-45e8-9c9d-5cb586bb3639)



# Parámetros

Retorna un arreglo de numpy 2x2 con los parámetros correspondientes

* Directos: `c.matriz_dir`  
* Inversos: `c.matriz_inv`  
* Z: `c.matriz_z`
* Y: `c.matriz_y`
* H: `c.matriz_h`
* G: `c.matriz_g`

# Impedancias imagenes

Atributos que retornan las impedancias imagenes del cuadripolo

* Imagen 1: `c.zim1`
* Imagen 2: `c.zim2`

# Impedancias iterativas

Atributos que retornan las impedancias iterativas del cuadripolo

* Iterativa 1: `c.zk1`
* Iterativa 2: `c.zk2`


# Funciones

Las siguientes funciones necesitan un parámetro `zout` que identifica la carga del cuadripolo. La carga puede ser real o compleja:

## Transferencia

* Transferencia de tensiones: `c.ftransfv(zout)`
* Transferencia de corrientes: `c.ftransfi(zout)`

## Propagación
  
* Propagación de tensiones: `c.fpropv(zout)`
* Propagación de corrientes: `c.fpropi(zout)`

## Alpha y Beta

* Alpha de tensiones: `c.alphav(zout)`
* Alpha de corrientes: `c.alphai(zout)`
* Beta de tensiones: `c.betav(zout)`
* Beta de corrientes: `c.betai(zout)`

* Ejemplo 1:

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

---

* Ejemplo 2 (clase práctica 27/09):

   ![ej 2](https://github.com/user-attachments/assets/7212e6e5-6aea-4681-b271-74bdb09068c0)
   
   Resolución:
   
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


# Asociaciones

Se pasa como parámetros una instancia `cuadri` del cuadripolo que se quiere asociar.
Retorna un nuevo cuadripolo que representa la asociación.

* Cascada: `c1.casc(c2)`
* Serie: `c1.serie(c2)`
* Paralelo: `c1.paralelo(c2)`
* Serie paralelo: `c1.serie_paralelo(c2)`
* Paralelo serie: `c1.paralelo_serie(c2)`

# Cuadripolo por parámetros directos

Se puede crear una instancia de cuadripolo directamente a partir de sus parámetros directos ABCD. Esta instancia de cuadripolo no tiene ninguna forma o configuración. Es un cuadripolo general.

```python
c = Cuadri(a, b, c, d)
```


# Cuadripolo a partir de otros parámetros


Se puede crear una instancia de cuadripolo directamente a partir de otros parámetros utilizando las funciones estáticas listadas debajo. Esta instancia de cuadripolo no tiene ninguna forma o configuración. Es un cuadripolo general.


* Parámetros z `Cuadri.por_z(z11, z12, z21, z22)`
* Parámetros y `Cuadri.por_y(y11, y12, y21, y22)`
* Parámetros h `Cuadri.por_h(h11, h12, h21, h22)`
* Parámetros g `Cuadri.por_g(g11, g12, g21, g22)`
* Parámetros inversos `Cuadri.por_inv(e, f, g, h)`


# Adaptadores

Creación de una instancia de cuadripolo que funcione como un adaptador. Los valores de impedancias de entrada y de salida deben ser puramente *reales*. Valores complejos no son admitidos. Las configuraciones que cuentan con esta función son:

## Tipo L

Se pasa como parámetros los valores de impedancias de entrada `zin` y salida `zout` que se desea tenga el adaptador:

* Ejemplo

  ![ej adapt L](https://github.com/user-attachments/assets/c1bf2a68-d5c0-4b8e-b417-024e1f987fb6)

  Resolución:

  ```python

  from cuadri import *
  
  zin = 300
  zout = 75
  c = CuadriL.adapt(zin, zout)
  
  print("z1:", c.z1)
  print("z2:", c.z2)
  print("zim1:", c.zim1)
  print("zim2:", c.zim2)
  print("tetha:", c.tetha)
  ```

  ![ej adapt L res](https://github.com/user-attachments/assets/fa354659-ee04-4e0b-b57b-039d187084ac)


## Tipo Li

Se pasa como parámetros los valores de impedancias de entrada `zin` y salida `zout` que se desea tenga el adaptador:

* Ejemplo

  ![ej adapt Li](https://github.com/user-attachments/assets/71f0f818-df58-4d10-b3af-b5b77d2f19cf)

  Resolución:

  ```python

  from cuadri import *
  
  zin = 50
  zout = 300
  c = CuadriLi.adapt(zin, zout)

  print("z1:", c.z1)
  print("z2:", c.z2)
  print("zim1:", c.zim1)
  print("zim2:", c.zim2)
  print("tetha:", c.tetha)
  ```

  ![ej adapt Li res](https://github.com/user-attachments/assets/39bdd78d-c608-45c4-8484-38a1e342880f)


  
## Tipo T

Se pasa como parámetros los valores de impedancias de entrada `zin` y salida `zout` que se desea tenga el adaptador. Posee un tercer parámetro que corresponde al valor de corrección que se debe sumar a la relación Ein/Eout. Este parámetro es opcional y tiene un valor de 0.634, a menos que es especifique otro valor. Con el valor por defecto funciona bien.

* Ejemplo

  ![ej adapt T](https://github.com/user-attachments/assets/ba9a5fdb-6e80-4d0e-b04d-b17e137c08b1)

  Resolución:
  
  ```python

  from cuadri import *
  
  zin = 75
  zout = 300
  c = CuadriT.adapt(zin, zout)
  
  print("z1:", c.z1)
  print("z2:", c.z2)
  print("z3:", c.z3)
  print("zim1:", c.zim1)
  print("zim2:", c.zim2)
  print("tetha:", c.tetha)

  ```
  ![ej adapt T res](https://github.com/user-attachments/assets/f6de414c-a68b-4c62-8399-d9d574966891)



# Atenuadores

Creación de una instancia de cuadripolo que funcione como un atenuador. El valor de la impedancia iterativa Zk2 debe ser puramente *real*. Valores complejos no son admitidos. Las configuraciones que cuentan con esta función son:

## Tipo L

Se pasa como parámetro la tensión de entrada `vin`, la tensión de salida deseada `vout`, y la impedancia iterativa `zk2`

* Ejemplo

   ![ej aten L](https://github.com/user-attachments/assets/aed6ff85-f488-4f36-87f8-7ce21b3b9e9f)
   
   Resolución:
   
   ```python
   from cuadri import *
   
   vin = 40
   vout = 8
   zk2 = 300
   c = CuadriL.aten(vin, vout, zk2)
   
   print("z1:", c.z1)
   print("z2:", c.z2)
   print("zk2:", c.zk2)
   print("fprop v:", c.fpropv(zk2))
   ```
   
   ![ej aten L res](https://github.com/user-attachments/assets/00628105-1821-4de0-aed1-b1121e779f6e)

## Tipo Li

Se pasa como parámetro la tensión de entrada `vin`, la tensión de salida deseada `vout`, y la impedancia iterativa `zk2`

* Ejemplo
     
   ![ej aten Li](https://github.com/user-attachments/assets/6bf5fff4-889f-4b31-8b88-172e87817bf6)
   
   
   Resolución:
   
   ```python
   from cuadri import *
   
   vin = 40
   vout = 8
   zk2 = 300
   c = CuadriLi.aten(vin, vout, zk2)
   
   print("z1:", c.z1)
   print("z2:", c.z2)
   print("zk2:", c.zk2)
   print("fprop v:", c.fpropv(zk2))
   ```
   ![ej aten Li res](https://github.com/user-attachments/assets/a1fc678d-92c9-4d7b-8b43-61efa7ff8940)

## Tipo T

Se pasa como parámetro la tensión de entrada `vin`, la tensión de salida deseada `vout`, y la impedancia iterativa `zk2`

* Ejemplo

   ![ej aten T](https://github.com/user-attachments/assets/aa91a615-b311-4458-ac28-ac03083e39e6)

   Resolución:
   
   ```python
   vin = 40
   vout = 16
   zk2 = 8
   c = CuadriT.aten(vin, vout, zk2)
   
   print("z1:", c.z1)
   print("z2:", c.z2)
   print("z3:", c.z3)
   print("zk2:", c.zk2)
   print("fprop v:", c.fpropv(zk2))
   ```
   ![ej aten T res](https://github.com/user-attachments/assets/b6aa48d8-418d-476a-9016-576c2ab45008)

## Tipo Pi

Se pasa como parámetro la tensión de entrada `vin`, la tensión de salida deseada `vout`, y la impedancia iterativa `zk2`

* Ejemplo

   ![ej aten Pi](https://github.com/user-attachments/assets/aacf2f7e-da4c-44bd-8be8-d4800917d2cf)
   
   Resolución:
   
   ```python
   vin = 40
   vout = 16
   zk2 = 8
   c = CuadriPi.aten(vin, vout, zk2)
   
   print("z1:", c.z1)
   print("z2:", c.z2)
   print("z3:", c.z3)
   print("zk2:", c.zk2)
   print("fprop v:", c.fpropv(zk2))
   ```
   
   ![ej aten Pi res](https://github.com/user-attachments/assets/1dbf492f-bd39-45ba-9fad-42dfe2ac87db)



