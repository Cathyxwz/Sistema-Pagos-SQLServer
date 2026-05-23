# 📊 Sistema de Gestión de Pagos Automatizado (Python + SQL Server)

Un sistema de consola dinámico diseñado para la administración de transacciones financieras en tiempo real. Este proyecto integra el poder de **SQL Server** para el almacenamiento seguro de datos con automatizaciones de **Python** para optimizar tareas administrativas cotidianas.

---

## 🚀 ¿Cómo Funciona el Sistema?

El flujo del software está diseñado para ejecutarse en cadena de la siguiente manera:

1. **Captura de Datos**: El usuario registra un nuevo pago desde un menú interactivo en la consola de comandos.
2. **Persistencia en SQL**: Python se conecta a SQL Server y guarda de forma permanente el cliente, el servicio y el monto, generando un ID numérico único y automático.
3. **Automatización de Archivos (Módulo OS)**: El sistema detecta el registro y genera de inmediato un recibo físico en formato `.txt` dentro de una carpeta local.
4. **Notificación en Redes (Módulo SMTP)**: Al mismo tiempo, Python se conecta de forma segura a los servidores de Google y envía una alerta por correo electrónico (Gmail) informando al administrador sobre el recaudo.
5. **Análisis de Datos (Cierre de Caja)**: El motor de SQL Server procesa internamente todas las transacciones para calcular totales, promedios y balances financieros al instante sin saturar la memoria de Python.

---

## 🛠️ Tecnologías y Módulos Utilizados

* **SQL Server**: Motor de base de datos relacional para el almacenamiento persistente de transacciones.
* **pyodbc**: Conector oficial que permite a Python comunicarse y ejecutar sentencias SQL.
* **smtplib & email**: Librerías nativas de Python para gestionar conexiones cifradas y envíos de correo mediante el protocolo SMTP.
* **os**: Módulo para la manipulación y creación automática de directorios y archivos físicos en el sistema operativo.

---

## 🗄️ Inicialización de la Base de Datos

Ejecuta este script dentro de tu **SQL Server Management Studio (SSMS)** para crear la estructura necesaria:

```sql
CREATE DATABASE sistema_pagos;
GO
USE sistema_pagos;
GO
CREATE TABLE transacciones (
    id INT IDENTITY(1,1) PRIMARY KEY,
    cliente VARCHAR(100) NOT NULL,
    servicio VARCHAR(100) NOT NULL,
    monto DECIMAL(10, 2) NOT NULL,
    fecha DATETIME DEFAULT GETDATE()
);
GO