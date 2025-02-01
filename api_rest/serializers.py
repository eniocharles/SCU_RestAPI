from rest_framework import serializers
from rest_framework.validators import UniqueValidator #Validator para garantir unicidade do Email
from .models import User


#Serializer para visualização de usuário
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nickname', 'email', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']   #Impede edição desses campos na atualização


#Serializer para registro de usuário com hashing de senha e validação de email
class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all(),message='Este e-mail já está em uso.')]
    )

    class Meta:
        model = User
        fields = ['email', 'nickname', 'password']  #Campos esperados na requisição
        extra_kwargs = {'password': {'write_only':True}}  #Garante que a senha nunca seja exposta 

    def create(self, validated_data):
        """ Sobrescreve o método create para usar a função create_user(),
        garantindo que a senha seja armazenada com hashing."""
        return User.objects.create_user(**validated_data)


#Serializer para login de usuário
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, allow_blank=False, trim_whitespace=True)
    password = serializers.CharField(write_only=True, min_length=6)
    