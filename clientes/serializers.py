from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    # // Validações feitas a partir de todos os campos de um POST (no campo 'data')
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            # // precisamos informar o campo relacionado ao erro ('cpf')
            raise serializers.ValidationError({ 'cpf': "CPF inválido" })
        
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({ 'nome': "Não inclua números neste campo" })
        
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({ 'rg': "O rg deve ter 9 dígitos" })
        
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({ 'celular': "O celular deve seguir este modelo: 'xx xxxxx-xxxx'" })

        return data
