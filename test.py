import dns.resolver  # Importar la biblioteca para realizar consultas DNS

# Función para verificar si un dominio tiene un registro MX válido
def has_mx_record(domain):
    try:
        answers = dns.resolver.resolve(domain, 'MX')  # Consultar registros MX
        return len(answers) > 0  # Retorna True si hay registros MX
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.Timeout):
        return False  # Retorna False si no hay registros MX o el dominio no existe

# Dirección de correo a verificar
email = "example@example.com"

# Extraer el dominio del correo
parts = email.split("@")
if len(parts) == 2:
    domain = parts[1]
    if has_mx_record(domain):
        print("✅ El dominio tiene un registro MX válido.")
    else:
        print("❌ El dominio NO tiene un registro MX válido.")
else:
    print("⚠️ Dirección de correo inválida.")
