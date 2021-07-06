from rest_framework import serializers
from clientes.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate_cpf(self, cpf):
        """Verifica se o CPF tem 11 digitos """
        if len(cpf) != 11:
            raise serializers.ValidationError("O CPF dever ter 11 digitos ")
        return cpf

    def validate_nome(self, nome):
        """Verifica se o campo nome é válido"""
        if not nome.isalpha():
            raise serializers.ValidationError("Não inclua números neste campo ")
        return nome

    def validate_rg(self, rg):
        """Verifica se o RG tem 9 caracteres """
        if len(rg) != 9:
            raise serializers.ValidationError("O RG deve ter 9 dígitos")
        return rg

    def validate_celular(self, celular):
        """Verifica a validação do campo celular"""
        if len(celular) < 11:
            raise serializers.ValidationError("O Celular dever ter 11 digitos")
        return celular

    