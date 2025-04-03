from django.shortcuts import render
from .models import Pessoa
from rest_framework.response import Response
from .serializers import PessoaSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status, viewsets
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_pessoas(request):
    pessoas = Pessoa.objects.all()
    serializer = PessoaSerializer(pessoas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_pessoa(request, pk):
    try:
        pessoa = Pessoa.objects.get(pk=pk)
    except Pessoa.DoesNotExist:
        return Response({"Erro: ": "Essa pessoa não existe!"}, status=status.HTTP_404_NOT_FOUND)
    serializer = PessoaSerializer(pessoa)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def registrar(request):
    nome = request.data.get('username')
    senha = request.data.get('senha')
    email = request.data.get('email')
    biografia = request.data.get('biografia')
    idade = request.data.get('idade')
    telefone = request.data.get('telefone')
    endereco = request.data.get('endereco')
    escolaridade = request.data.get('escolaridade')
    qte_animais = request.data.get('qte_animais') 

    if not nome or not senha or not email:
        return Response({"Erro: ": "O campo de nome, email e senha são obrigatórios!"}, status=status.HTTP_400_BAD_REQUEST)

    usuario = Pessoa.objects.create_user(
        username=nome,
        password=senha,
        email=email,
        biografia=biografia,
        idade=idade,
        telefone=telefone,
        endereco=endereco,
        escolaridade=escolaridade,
        qte_animais=qte_animais
    )

    return Response({"Mensagem: ": "O usuário foi cadastrado com sucesso!"}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def logar(request):
    nome = request.data.get('username')
    senha = request.data.get('senha')

    user = authenticate(username=nome, password=senha)

    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            'acesso': str(refresh.access_token),
            'refresh': str(refresh)
        }, status=status.HTTP_200_OK)
    else:
        return Response({"Erro: ": "Digite o usuário ou senha corretos!"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_pessoa(request, pk):
    try:
        pessoa = Pessoa.objects.get(pk=pk)
    except Pessoa.DoesNotExist:
        return Response({'Erro': 'Essa pessoa não existe!'}, status=status.HTTP_404_NOT_FOUND)

    # Se password for enviado na requisição, atualiza corretamente
    senha = request.data.get("password", None)
    if senha:
        pessoa.set_password(senha)  # Garante que a senha seja criptografada

    # Atualiza os outros campos sem exigir todos os dados
    serializer = PessoaSerializer(pessoa, data=request.data, partial=True)  
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_pessoa(request, pk):
    try:
        pessoa = Pessoa.objects.get(pk=pk)
    except Pessoa.DoesNotExist:
        return Response({"Erro: ": "Essa pessoa não existe!"}, status=status.HTTP_404_NOT_FOUND)

    pessoa.delete()
    return Response({"Mensagem: ": "Pessoa deletada com sucesso!"}, status=status.HTTP_204_NO_CONTENT)