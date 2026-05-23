import pyodbc
import os
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


CONEXION_STRING = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=localhost;"
    "Database=sistema_pagos;"
    "Trusted_Connection=yes;"
)

CORREO_REMITENTE = "katherinecalderoncordova@gmail.com"
CORREO_PASSWORD = "rzkw warp ahun hjfv"
CORREO_DESTINATARIO = "katherinecalderoncordova@gmail.com"

def conectar_db():
    return pyodbc.connect(CONEXION_STRING)

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def generar_archivo_recibo(id_transaccion, cliente, servicio, monto):
    carpeta = "recibos"
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    nombre_archivo = f"{carpeta}/recibo_{id_transaccion}.txt"
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("          RECIBO DE PAGO DIGITAL        \n")
        archivo.write("========================================\n")
        archivo.write(f"ID Transacción: {id_transaccion}\n")
        archivo.write(f"Cliente:        {cliente}\n")
        archivo.write(f"Servicio:       {servicio}\n")
        archivo.write(f"Total Pagado:   ${monto:.2f}\n")
        archivo.write("========================================\n")
        archivo.write("      ¡Gracias por su preferencia!      \n")
    print(f"-> [OS] Recibo físico generado automáticamente en: {nombre_archivo}")

def enviar_notificacion_gmail(cliente, servicio, monto):
    mensaje = MIMEMultipart()
    mensaje['From'] = CORREO_REMITENTE
    mensaje['To'] = CORREO_DESTINATARIO
    mensaje['Subject'] = f"🚨 Alerta de Pago Recibido: {cliente}"
    cuerpo_correo = f"Hola Administrador,\nSe ha registrado un pago:\n• Cliente: {cliente}\n• Servicio: {servicio}\n• Monto: ${monto:.2f}"
    mensaje.attach(MIMEText(cuerpo_correo, 'plain'))
    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(CORREO_REMITENTE, CORREO_PASSWORD)
        servidor.sendmail(CORREO_REMITENTE, CORREO_DESTINATARIO, mensaje.as_string())
        servidor.quit()
        print("-> [Gmail] Notificación de correo enviada exitosamente. 📧")
    except Exception as error:
        print(f"❌ No se pudo mandar el correo. Detalles: {error}")

def registrar_pago():
    limpiar_pantalla()
    print("=== REGISTRAR NUEVO PAGO ===")
    cliente = input("Nombre del cliente: ")
    servicio = input("Servicio prestado: ")
    try:
        monto = float(input("Monto a pagar ($): "))
    except ValueError:
        print("❌ Error: El monto debe ser un número válido.")
        time.sleep(2)
        return
    try:
        db = conectar_db()
        cursor = db.cursor()
        sql = "INSERT INTO transacciones (cliente, servicio, monto) VALUES (?, ?, ?)"
        valores = (cliente, servicio, monto)
        cursor.execute(sql, valores)
        cursor.execute("SELECT @@IDENTITY")
        id_insertado = int(cursor.fetchone()[0])
        db.commit()
        print(f"\n✔ ¡Éxito! Datos guardados en la base de datos (ID: {id_insertado})")
        print("Ejecutando procesos automáticos en segundo plano...")
        generar_archivo_recibo(id_insertado, cliente, servicio, monto)
        enviar_notificacion_gmail(cliente, servicio, monto)
        cursor.close()
        db.close()
    except Exception as err:
        print(f"❌ Error de conexión o base de datos: {err}")
    input("\nPresiona Enter para continuar...")

def ver_historial():
    limpiar_pantalla()
    print("=== HISTORIAL DE PAGOS REGISTRADOS ===\n")
    try:
        db = conectar_db()
        cursor = db.cursor()
        cursor.execute("SELECT id, cliente, servicio, monto, fecha FROM transacciones")
        resultados = cursor.fetchall()
        if not resultados:
            print("No hay ningún pago registrado todavía en la base de datos.")
        else:
            for fila in resultados:
                print(f"ID: {fila[0]} | Cliente: {fila[1]} | Servicio: {fila[2]} | Total: ${fila[3]} | Fecha: {fila[4]}")
        cursor.close()
        db.close()
    except Exception as err:
        print(f"❌ Error al leer los datos de SQL Server: {err}")
    input("\nPresiona Enter para volver al menú...")

def mostrar_cierre_caja_db():
    limpiar_pantalla()
    print("      CIERRE DE CAJA DIRECTO DESDE LA BASE       ")
    try:
        db = conectar_db()
        cursor = db.cursor()
        query_analitica = "SELECT SUM(monto), COUNT(id), MAX(monto), MIN(monto) FROM transacciones;"
        cursor.execute(query_analitica)
        resultado = cursor.fetchone()
        if resultado[1] == 0 or resultado[0] is None:
            print("⚠ La base de datos no tiene transacciones.")
        else:
            print(f"Total Dinero Recaudado : ${resultado[0]:,.2f}")
            print(f"Cantidad de Servicios  : {resultado[1]} atendidos")
            print(f"Servicio Más Costoso   : ${resultado[2]:,.2f}")
            print(f"Servicio Más Económico : ${resultado[3]:,.2f}")
        cursor.close()
        db.close()
    except Exception as err:
        print(f"Error al calcular en SQL Server: {err}")
    input("\nPresiona Enter para regresar al menú principal...")

def menu_principal():
    while True:
        limpiar_pantalla()
        print("    SISTEMA DE GESTIÓN DE PAGOS     ")
        print("1. Registrar un nuevo pago")
        print("2. Ver historial de pagos (SQL Server)")
        print("3. Calcular Cierre de Caja (Desde la BD)")
        print("4. Salir del sistema")
        opcion = input("\nSelecciona una opción (1-4): ")
        if opcion == "1":
            registrar_pago()
        elif opcion == "2":
            ver_historial()
        elif opcion == "3":
            mostrar_cierre_caja_db()
        elif opcion == "4":
            print("\n¡Gracias por utilizar el sistema automatizado!")
            break
        else:
            print("\nOpción no válida. Intenta de nuevo.")
            time.sleep(1.5)

if __name__ == "__main__":
    menu_principal()