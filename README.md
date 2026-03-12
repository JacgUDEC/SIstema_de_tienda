# 🏪 Sistema de Tienda en Python

Este proyecto consiste en un sistema de tienda hecho en Python utilizando la **Programación Orientada a Objetos (POO)**.  
El programa permite gestionar un inventario de productos y simular compras mediante un carro.

---

# 📌 Descripción del sistema

El sistema simula el funcionamiento de una tienda.  
Permite agregar productos al inventario, visualizar los productos disponibles y añadirlos a un carrito de compras.

El programa utiliza tres clases:

- **Producto** → Representa los productos disponibles en la tienda.
- **Tienda** → Administra el inventario de productos.
- **Carro** → Gestiona los productos agregados al carrito de compras.

Cuando un producto se agrega al carrito, el sistema reduce automáticamente el **stock disponible**, evitando que se compren más unidades de las existentes.

Las principales funcionalidades del sistema son:

- Agregar productos al inventario.
- Ver el inventario de la tienda.
- Agregar productos al carrito.
- Ver los productos del carrito.
- Calcular el total de la compra.

---

# 📂 Estructura del proyecto

El proyecto tiene una estructura simple:

### Tienda.py
Contiene todo el código del sistema, incluyendo:

- las clases:
  - `Producto`
  - `Tienda`
  - `Carro`
- Menú interactivo para el usuario.
- Funciones para agregar productos al inventario.

### README.md
Este mismo documento donde se explica el funcionamiento del codigo su estructura y como ejecutarlo.

---

# ▶️ Cómo ejecutar el programa

Para ejecutar el programa se necesita tener instalado **Python 3**.

### 1️⃣ Descargar o clonar el proyecto

Si usas Git:

```bash
git clone https://github.com/JacgUDEC/SIstema_de_tienda.git

o se descarga el archivo Tienda.py