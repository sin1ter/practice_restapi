from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from accounts.api.serializers import RegistrationSerializer, UserUpdateSerializer, ChangePasswordSerializer
# from accounts.models import *

# @api_view(['POST',])
# def logout_view(request):

#     if request.method == 'POST':
#         request.user.auth_token.delete()

#         return Response(status=status.HTTP_200_OK)



@api_view(['POST',])
@permission_classes([AllowAny])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()

            data['response'] = "Registration Succesfull"
            data['username'] = account.username
            data['email'] = account.email
            
            # token = Token.objects.get(user=account).key
            # data['token'] = token

            refresh = RefreshToken.for_user(account)

            data['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }


        else:
            data = serializer.errors

        return Response(data, status=status.HTTP_201_CREATED)
    
class LogoutView(APIView):
    
    def post(self, request):
        try: 
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class User_info(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserUpdateSerializer
    
    def get_object(self):
        return self.request.user
    
class Update_password(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer
    
    def get_object(self):
        return self.request.user