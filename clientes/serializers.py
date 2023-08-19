from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validade(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"O CPF está invalido."}) 
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':"O nome deve ter caracteres alfabéticos."}) 
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':"O rg deve ter 9 digitos."}) 
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':"O número de celular deve seguir o padrão: DD-99999-9999."})
        return data

