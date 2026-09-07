# 📊 Sistema de Gestión de Pagos Automatizado

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/) [![SQL Server](https://img.shields.io/badge/SQL%20Server-CC2927?style=for-the-badge&logo=microsoftsqlserver&logoColor=white)](https://www.microsoft.com/sql-server) [![pyodbc](https://img.shields.io/badge/pyodbc-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://github.com/mkleehammer/pyodbc) [![SMTP](https://img.shields.io/badge/SMTP-4285F4?style=for-the-badge&logo=gmail&logoColor=white)](https://www.python.org/)

Sistema de consola dinámico diseñado para la **administración de transacciones financieras en tiempo real**.

Este proyecto integra el poder de **SQL Server** para el almacenamiento seguro de datos con automatizaciones de **Python** para optimizar tareas administrativas cotidianas.

---

## 📑 Índice

- 🚀 [¿Cómo Funciona el Sistema?](#-cómo-funciona-el-sistema)
- 🛠️ [Tecnologías y Módulos Utilizados](#️-tecnologías-y-módulos-utilizados)
- 🗄️ [Inicialización de la Base de Datos](#️-inicialización-de-la-base-de-datos)

---

## 🚀 ¿Cómo Funciona el Sistema?

El flujo del software está diseñado para ejecutarse en cadena de la siguiente manera:

### 1️⃣ Captura de Datos

El usuario registra un nuevo pago desde un **menú interactivo en la consola de comandos**.

---

### 2️⃣ Persistencia en SQL

Python se conecta a **SQL Server** y guarda de forma permanente el **cliente, el servicio y el monto**, generando un **ID numérico único y automático**.

---

### 3️⃣ Automatización de Archivos

El sistema utiliza el **Módulo OS** para detectar el registro y generar de inmediato un **recibo físico en formato `.txt`** dentro de una carpeta local.

---

### 4️⃣ Notificación en Redes

Al mismo tiempo, Python se conecta de forma segura a los **servidores de Google** y envía una alerta por correo electrónico mediante **Gmail**, informando al administrador sobre el recaudo.

---

### 5️⃣ Análisis de Datos

El motor de **SQL Server** procesa internamente todas las transacciones para calcular **totales, promedios y balances financieros** al instante sin saturar la memoria de Python.

---

## 🛠️ Tecnologías y Módulos Utilizados

| Tecnología / Módulo | Descripción |
|---|---|
| **SQL Server** | Motor de base de datos relacional para el almacenamiento persistente de transacciones. |
| **pyodbc** | Conector oficial que permite a Python comunicarse y ejecutar sentencias SQL. |
| **smtplib & email** | Librerías nativas de Python para gestionar conexiones cifradas y envíos de correo mediante el protocolo SMTP. |
| **os** | Módulo para la manipulación y creación automática de directorios y archivos físicos en el sistema operativo. |

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
```
