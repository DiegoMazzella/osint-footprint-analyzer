"""
Módulo: inteligencia_dominios.py
Propósito: Recolectar información básica de dominios de forma ética
Autor: Tu nombre
"""

import socket
import datetime

def whois_sintetico(dominio):
    """
    Función simulada de WHOIS.
    Retorna información ficticia de manera ética.
    """
    return {
        "dominio": dominio,
        "registrante": "Empresa Ficticia S.A.",
        "fecha_registro": "2020-01-01",
        "fecha_expiracion": "2025-01-01",
        "dns": ["ns1.ficticio.com", "ns2.ficticio.com"]
    }

def obtener_ip(dominio):
    """
    Retorna la IP principal de un dominio.
    """
    try:
        ip = socket.gethostbyname(dominio)
    except Exception:
        ip = "No disponible"
    return ip

if __name__ == "__main__":
    dominio_ejemplo = "empresa-ficticia.com"
    info_whois = whois_sintetico(dominio_ejemplo)
    ip = obtener_ip(dominio_ejemplo)
    
    print("=== Información del dominio ===")
    print(f"Dominio: {info_whois['dominio']}")
    print(f"Registrante: {info_whois['registrante']}")
    print(f"Fecha registro: {info_whois['fecha_registro']}")
    print(f"Fecha expiración: {info_whois['fecha_expiracion']}")
    print(f"DNS: {', '.join(info_whois['dns'])}")
    print(f"IP principal: {ip}")
    print(f"Análisis realizado: {datetime.datetime.now()}")
