def cpf_valido(numero_do_cpf):
    """Verifica se o CPF tem 11 digitos """
    return len(numero_do_cpf) == 11


def nome_valido(nome):
    """Verifica se o campo nome é válido"""
    return nome.isalpha()

def rg_valido(rg):
    """Verifica se o RG tem 9 caracteres """
    return len(rg)

