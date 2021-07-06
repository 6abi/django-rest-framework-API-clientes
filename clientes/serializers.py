from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': "Número de CPF inválido"})

        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':"Não inclua números neste campo "})

        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg': "O RG deve ter 9 dígitos"})

        return data



    def validate_celular(self, celular):
        """Verifica a validação do campo celular"""
        if len(celular) < 11:
            raise serializers.ValidationError("O Celular dever ter 11 digitos")
        return celular

    