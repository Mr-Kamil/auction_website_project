from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password
from rest_framework import status
from .serializers import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.


class Conditions(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        conditions = Condition.objects.all()
        serializer = ConditionsSerializer(conditions, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class Items(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        conditions = Item.objects.all()
        serializer = ItemsSerializer(conditions, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class Categories(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategoriesSerializer(categories, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ItemsNewest(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        items = list(reversed(Item.objects.order_by('-created_data')))[:5]
        serializer = ItemsSerializer(items, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class SingleCategoryItems(APIView):
    permission_classes = [AllowAny]

    def get(self, request, category_name):
        items = Item.objects.filter(category__category=category_name)
        serializer = ItemsSerializer(items, many=True)

        return Response(serializer.data)


class UserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)

        if serializer.is_valid():
            password = serializer.validated_data.get('password')
            repeated_password = serializer.validated_data.pop('repeated_password')

            if password != repeated_password:
                return Response({"error_message": "Passwords do not match"}, status=status.HTTP_400_BAD_REQUEST)

            user = serializer.save(password=make_password(password))

            return Response({"user_id": user.id}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return Response(status=status.HTTP_200_OK)

        return Response({'detail': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)


class UserLoggedIn(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_serializer = UserSerializer(request.user)
        return Response(user_serializer.data)


class UserDelete(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        password = request.data.get('password')

        if authenticate(username=user.username, password=password):
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        else:
            message = 'Wrong password.'
            return Response({'message': message}, status=status.HTTP_400_BAD_REQUEST)


class UserLogout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({'detail': 'Logout successful.'})


class UserAvatar(APIView):
    permission_classes = [IsAuthenticated]
    # parser_classes = [MultiPartParser, FormParser]
    print('oleoleole')
    def post(self, request):
        print('test0')
        serializer = AvatarSerializer(data=request.data)
        print('test')
        if serializer.is_valid():
            user = request.user
            print('test2', user.username)
            user.avatar = serializer.validated_data['avatar']
            user.save()
            return Response({'detail': 'Avatar uploaded successfully'})

        return Response(serializer.errors, status=400)

    def delete(self, request):
        user = request.user

        if user.avatar:
            user.avatar.delete()
            user.avatar = None
            user.save()

        return Response({'detail': 'Avatar deleted successfully'})