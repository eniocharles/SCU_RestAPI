from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.exceptions import PermissionDenied


from .models import User
from .serializers import UserSerializer, UserRegistrationSerializer, UserLoginSerializer

#View para registrar novos usuários
class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer


#View para listar usuários
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

#View para visualizar usuário
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user
        user_id = self.kwargs.get('pk')
        if user.id != user_id:
            raise PermissionDenied("Você não tem permissão para modificar este usuário.")
        return user

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#View para fazer login
class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            email = serializer.validated_data['email'],
            password = serializer.validated_data['password'])
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh':str(refresh),
                'access':str(refresh.access_token),
            })
    
        return Response({"error": "Credenciais inválidas"}, status=status.HTTP_400_BAD_REQUEST)