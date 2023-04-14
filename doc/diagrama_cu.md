<div align="justify">

# Banana Shopping:

<div align="center">
  <img src="../img/diagrama.png"/>
</div>

Nuestro sistema se basa en una tienda de compras online, donde los clientes podrán pedir productos con envios casi inmediatos entre las Islas Canarias


|  Actor | Cliente no registrado |
|---|---|
| Descripción  | Cliente que entra a la aplicación a ojear los productos y ofertas.  |
| Características  |  |
| Relaciones | No tiene relaciones con otros actores  |
| Referencias | |   
|  Notas |   |
| Autores  | __Marlon Farizo Hergueta y Ayoze Hernández Díaz__ |
|Fecha | _31/03/2023_ |

|  Actor | Cliente registrado |
|---|---|
| Descripción  | Cliente que ya está registrado en la aplicación  |
| Características  |  |
| Relaciones | cliente no registrado  |
| Referencias | |   
|  Notas |   |
| Autores  | __Marlon Farizo Hergueta y Ayoze Hernández Díaz__ |
|Fecha | _31/03/2023_ |


|  Actor | Administrador |
|---|---|
| Descripción  | Administrador que se encarga de gestionar la aplicación  |
| Características  |  |
| Relaciones |   |
| Referencias | |   
|  Notas |   |
| Autores  | __Marlon Farizo Hergueta y Ayoze Hernández Díaz__ |
|Fecha | _31/03/2023_ |


| CU1 | CU1 Registrarse |
|---|---|
| Fuentes  | Este documento  |
| Actor  | Cliente registrado, cliente no registrado  |
| Descripción |  Método que permite a un cliente registrarse en el sistema |
| Flujo básico | El cliente entra al sistema y se registra |
| Pre-condiciones |  |  
| Post-condiciones  |   |  
|  Requerimientos |   |
|  Notas |   |
| Autores  | __Marlon Farizo Hergueta y Ayoze Hernández Díaz__ |
|Fecha | _31/03/2023_ |


| CU2 | CU2 Asociar tarjeta|
|---|---|
| Fuentes  | Este documento  |
| Actor  | Cliente registrado, cliente no registrado  |
| Descripción | Método que permite a un cliente asociar una tarjeta al registrarse  |
| Flujo básico | El cliente al registrarse asocia la tarjeta |
| Pre-condiciones |  |  
| Post-condiciones  |   |  
|  Requerimientos |   |
|  Notas |   |
| Autores  | __Marlon Farizo Hergueta y Ayoze Hernández Díaz__ |
|Fecha | _31/03/2023_ |


| CU3 | CU3 Realizar Pedido |
|---|---|
| Fuentes  | Este documento |
| Actor  |  Cliente registrado |
| Descripción |  Método que permite al cliente elegir un producto para comprarlo |
| Flujo básico | El cliente realiza un pedido |
| Pre-condiciones |  |  
| Post-condiciones  | |  
| Requerimientos |   |
| Notas |   |
| Autores  | __Marlon Farizo Hergueta y Ayoze Hernández Díaz__ |
|Fecha | _31/03/2023_ |


| CU4 | CU4 Mostrar producto |
|---|---|
| Fuentes  | Este documento  |
| Actor  |  Cliente registrado |
| Descripción |  Método que permite mostrar los productos |
| Flujo básico | El cliente realiza un pedido y se autentica |
| Pre-condiciones | Interactuar con el CU3 |  
| Post-condiciones  |   |  
|  Requerimientos | Estar autenticado  |
|  Notas |   |
| Autores  | __Marlon Farizo Hergueta y Ayoze Hernández Díaz__ |
|Fecha | _31/03/2023_ |


| CU5 | CU5 Seleccionar producto |
|---|---|
| Fuentes  | Este documento  |
| Actor  | Cliente registrado  |
| Descripción | Método que permite seleccionar productos para comprar   |
| Flujo básico | El cliente realiza un pedido y selecciona los productos que quiere |
| Pre-condiciones | Interactuar con el CU3 |  
| Post-condiciones  |   |  
|  Requerimientos | Estar autenticado  |
|  Notas |   |
| Autores  | __Marlon Farizo Hergueta y Ayoze Hernández Díaz__ |
|Fecha | _31/03/2023_ |


| CU6 | CU6 Comprar producto |
|---|---|
| Fuentes  | Este documento  |
| Actor  | Cliente registrado  |
| Descripción |  Método que permite comprar los productos |
| Flujo básico | El cliente realiza un pedido, selecciona un producto y decide comprarlo |
| Pre-condiciones | Interactuar con el CU3 |  
| Post-condiciones  |   |  
|  Requerimientos | Estar autenticado  |
|  Notas |   |
| Autores  | __Marlon Farizo Hergueta y Ayoze Hernández Díaz__ |
|Fecha | _31/03/2023_ |


| CU7 | CU7 Rechazar compra |
|---|---|
| Fuentes  | Este documento  |
| Actor  | Cliente registrado  |
| Descripción |  Método que permite denegar una compra debido a saldo insuficiente |
| Flujo básico | El cliente realiza una compra, y esta es denegada |
| Pre-condiciones | Interactuar con el CU3 |  
| Post-condiciones  |   |  
| Requerimientos | Estar autenticado |
| Notas |   |
| Autores  | __Marlon Farizo Hergueta y Ayoze Hernández Díaz__ |
|Fecha | _31/03/2023_ |


| CU8 | CU8 Confirmar compra |
|---|---|
| Fuentes  | Este documento  |
| Actor  | Cliente registrado  |
| Descripción |  Método que permite aceptar una compra |
| Flujo básico | El cliente realiza una compra, y esta es aceptada |
| Pre-condiciones |  |  
| Post-condiciones  |   |  
|  Requerimientos | Estar autenticado |
|  Notas |   |
| Autores  | __Marlon Farizo Hergueta y Ayoze Hernández Díaz__ |
|Fecha | _31/03/2023_ |


| CU9 | CU9 Verificar saldo |
|---|---|
| Fuentes  | Este documento  |
| Actor  | Cliente registrado  |
| Descripción | Método que permite verificar el saldo de una cuenta |
| Flujo básico | El cliente realiza un pedido, se autentica y se verifica el saldo de la cuenta al comprar |
| Pre-condiciones |  |  
| Post-condiciones  |   | 
|  Requerimientos | Estar autenticado |
|  Notas |   |
| Autores  | __Marlon Farizo Hergueta y Ayoze Hernández Díaz__ |
|Fecha | _31/03/2023_ |


| CU10 | CU10 Verificar stock |
|---|---|
| Fuentes  | Este documento  |
| Actor  | Cliente registrado  |
| Descripción | Método que permite verificar el stock  |
| Flujo básico | El cliente realiza un pedido, se autentica y se verifica el stock de los productos  |
| Pre-condiciones |  |  
| Post-condiciones  |   |  
|  Requerimientos |   |
|  Notas |   |
| Autores  | __Marlon Farizo Hergueta y Ayoze Hernández Díaz__ |
|Fecha | _31/03/2023_ |

# CU de administrador:

| CU11 | CU11 Eliminar productos |
|---|---|
| Fuentes  | Este documento  |
| Actor  | Administrador  |
| Descripción | Método que permite eliminar productos |
| Flujo básico | El administrador se autentica y realiza esta acción |
| Pre-condiciones |  |  
| Post-condiciones  |   |  
|  Requerimientos | Haber realizado una autenticación  |
|  Notas |   |
| Autores  | __Marlon Farizo Hergueta y Ayoze Hernández Díaz__ |
|Fecha | _31/03/2023_ |


| CU12 | CU12 Añadir productos |
|---|---|
| Fuentes  | Este documento  |
| Actor  | Administrador  |
| Descripción | Método que permite añadir productos |
| Flujo básico | El administrador se autentica y realiza esta acción |
| Pre-condiciones |  |  
| Post-condiciones  |   |  
|  Requerimientos | Haber realizado una autenticación  |
|  Notas |   |
| Autores  | __Marlon Farizo Hergueta y Ayoze Hernández Díaz__ |
|Fecha | _31/03/2023_ |


| CU13 | CU13 Modificar productos |
|---|---|
| Fuentes  | Este documento  |
| Actor  |  Administrador |
| Descripción |  Método que permite añadirMétodo que permite modificar productos |
| Flujo básico | El administrador se autentica y realiza esta acción |
| Pre-condiciones |  |  
| Post-condiciones  |   |  
|  Requerimientos | Haber realizado una autenticación  |
|  Notas |   |
| Autores  | __Marlon Farizo Hergueta y Ayoze Hernández Díaz__ |
|Fecha | _31/03/2023_ |


| CU14 | CU14 Añadir usuarios |
|---|---|
| Fuentes  | Este documento  |
| Actor  |  Administrador |
| Descripción |  Método que permite añadir usuarios |
| Flujo básico | El administrador se autentica y realiza esta acción |
| Pre-condiciones |  |  
| Post-condiciones  |   |  
|  Requerimientos | Haber realizado una autenticación  |
|  Notas |   |
| Autores  | __Marlon Farizo Hergueta y Ayoze Hernández Díaz__ |
|Fecha | _31/03/2023_ |


| CU15 | CU15 Eliminar usuarios |
|---|---|
| Fuentes  | Este documento  |
| Actor  | Administrador  |
| Descripción | Método que permite eliminar usuarios  |
| Flujo básico | El administrador se autentica y realiza esta acción |
| Pre-condiciones |  |  
| Post-condiciones  |   |  
|  Requerimientos |  Haber realizado una autenticación |
|  Notas |   |
| Autores  | __Marlon Farizo Hergueta y Ayoze Hernández Díaz__ |
|Fecha | _31/03/2023_ |


| CU16 | CU16 Modificar usuarios |
|---|---|
| Fuentes  | Este documento  |
| Actor  |  Administrador |
| Descripción |  Método que permite modificar usuarios |
| Flujo básico | El administrador se autentica y realiza esta acción |
| Pre-condiciones |  |  
| Post-condiciones  |   |
|  Requerimientos |  Haber realizado una autenticación |
|  Notas |   |
| Autores  | __Marlon Farizo Hergueta y Ayoze Hernández Díaz__ |
|Fecha | _31/03/2023_ |


| Cu | CU17 Autenticarse |
|---|---|
| Fuentes  | Este documento  |
| Actores  | Cliente registrado y administrador  |
| Descripción |   |
| Flujo básico | En el caso del administrador al entrar te autenticas,  el en caso del cliente al realizar un pedido te autenticas |
| Pre-condiciones |  |
| Post-condiciones  |   |  
|  Requerimientos | Estar registrado en el sistema |
|  Notas |   |
| Autores  | __Marlon Farizo Hergueta y Ayoze Hernández Díaz__ |
|Fecha | _31/03/2023_ |


</div>