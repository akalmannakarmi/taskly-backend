from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.generics import RetrieveAPIView
from .serializers import UserSerializer,UserSignupSerializer
from .models import CustomUser

class UserDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    
class UserSignUpView(APIView):
    permission_classes = [AllowAny]

    def post(self,request,*args,**kwargs):
        print(request.data)
        serializer = UserSignupSerializer(data=request.data)

        if serializer.is_valid():
            user = CustomUser(
                **serializer.validated_data
            )
            user.set_password(user.password)
            user.save()
            return Response({"message":f"Create user {user.username}"},HTTP_200_OK)
        
        return Response({"message":"Failed to create user.","error":f"{serializer.errors}"},HTTP_400_BAD_REQUEST)
