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

La clase persona ha sido creada con el propósito de que tanto cliente como [administrador](#id3) puedan heredar sus atributos, puesto que son comunes en ambas clases. Sus atributos son: código, dni, nombre, apellidos, dirección, teléfono, correo, fecha de nacimiento. Sus métodos son mostrar y gestionar.

### Cliente <a name="id2"></a>

La clase cliente hereda sus atributos de la clase [Persona](#id1) y tiene 2 atributos propios que son tarjeta y carrito. Tiene 2 métodos propios que son gestionar carrito y gestionar tarjeta.

### Administrador <a name="id3"></a>

La clase administrador hereda sus atributos de la clase [Persona](#id1) y tiene 1 método propio que le permite gestionar los productos.

### Detalle compra <a name="id4"></a>

La clase detalle compra tiene los atributos identificador y fecha e un único método mostrar.

### Producto <a name="id5"></a>

La clase producto tiene dos atributos, código y tipo, además de un método mostrar

### Listado de productos <a name="id6"></a>

El listado de productos esta compuesto por una sucesión de componentes que acabarán heredando las propiedades de componente, en ella podemos encontrar clases como: Ram, placa, CPU, fuente, etc.

### Componente <a name="id7"></a>

La clase de componentes tiene 3 atributos, código, precio y tipo, además de un método gestionar

