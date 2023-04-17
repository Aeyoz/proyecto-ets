<div align="justify">

# Banana Shopping:

<div align="center">
  <a name="id0"><img src="../img/diagrama_cl.png"/></a>
</div>

# Index

+ [Persona](#id1)
+ [Cliente](#id2)
+ [Administrador](#id3)
+ [Detalle compra](#id4)
+ [Producto](#id5)
+ [Listado de productos](#id6)
+ [Componente](#id7)


En este documento se describen las clases representadas en el siguiente artículo, las cuales han sido representadas en la [imagen](#id0) situada al principio del documento

### Persona <a name="id1"></a>

La clase persona ha sido creada con el propósito de que tanto cliente como [administrador]() puedan heredar sus atributos, puesto que son comunes en ambas clases. Sus atributos son: código, dni, nombre, apellidos, dirección, teléfono, correo, fecha de nacimiento. Sus métodos son mostrar y gestionar.

### Cliente <a name="id2"></a>

La clase cliente hereda sus atributos de la clase [Persona](#id1) y tiene 2 atributos propios que son tarjeta y carrito. Tiene 2 métodos propios que son gestionar carrito y gestionar tarjeta.

### Administrador <a name="id3"></a>

La clase administrador hereda sus atributos de la clase [Persona](#id1) y tiene 1 método propio que le permite gestionar los productos.

### Detalle compra <a name="id4"></a>
### Producto <a name="id5"></a>
### Listado de productos <a name="id6"></a>
### Componente <a name="id7"></a>
