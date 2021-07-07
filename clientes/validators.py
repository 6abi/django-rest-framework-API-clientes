import re
from validate_docbr import CPF

def cpf_valido(numero_do_cpf):
    """Verifica se o CPF tem 11 digitos """
    cpf = CPF()
    return cpf.validate(numero_do_cpf)  # True

def nome_valido(nome):
    """Verifica se o campo nome é válido"""
    return nome.isalpha()

def rg_valido(rg):
    """Verifica se o RG tem 9 caracteres """
    return len(rg)

def celular_valido(numero_celular):
    """Verifica se o celular é válido (11 91234-1234)"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, numero_celular)
    return  resposta

