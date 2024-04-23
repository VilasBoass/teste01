
import re
def validar_email(email):
    # Expressão regular para validar o formato do e-mail
    regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(regex, email):
        return True
    else:
        return False

def verificar_senha(senha):
    # Verificar comprimento mínimo de 8 caracteres
    if len(senha) < 8:
        return False
    # Verificar se contém pelo menos um número
    if not any(char.isdigit() for char in senha):
        return False
    # Verificar se contém pelo menos uma letra maiúscula
    if not any(char.isupper() for char in senha):
        return False
    # Verificar se contém pelo menos um símbolo
    if not any(char in '!@#$%^&*()-_+=[]{}|;:,.<>?`~' for char in senha):
        return False
    return True

# Exemplo de uso:
email = input("Digite seu endereço de e-mail: ")
if validar_email(email):
    print("E-mail válido!")
else:
    print("E-mail inválido. Por favor, insira um endereço de e-mail válido.")

senha = input("Digite sua senha: ")
if verificar_senha(senha):
    print("Senha segura!")
else:
    print("Senha não segura. Por favor, escolha uma senha com pelo menos 8 caracteres, incluindo números, letras maiúsculas e símbolos.")