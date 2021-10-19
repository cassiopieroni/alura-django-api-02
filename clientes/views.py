from rest_framework import viewsets, filters
from clientes.serializers import ClienteSerializer
from clientes.models import Cliente
from django_filters.rest_framework import DjangoFilterBackend

class ClientesViewSet(viewsets.ModelViewSet):
    """Listando clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


    # // utilizamos o 'DjangoFilterBackend' para poder ver a ordenação acontecer em um GET
    # // 'filters.OrderingFilter' é responsável por essa ordenação
    # // 'filters.SearchFilter' adiciona um filtro de busca
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]

    # // ordenamos por 'nome'
    ordering_fields = ['nome']

    # // o que o filtro de busca 'filters.SearchFilter' deve filtrar
    search_fields = ['nome', 'cpf']

    # // adiciona um campo de filtro (para boleanos)
    filterser_fields = ['ativo']
