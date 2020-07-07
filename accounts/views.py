from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import *
from orders.serializers import OrderSerializer
from rest_framework import status
from accounts.backends import JWTAuthentication


class Users(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, id=None):
        if id:
            obj = CustomUser.objects.get(id=id)
            serializer = UserSerializer(obj, many=False)
            return Response(serializer.data)
        else:
            objs = CustomUser.objects.all()
            serializer = UserSerializer(objs, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                'message': 'User created',
            },
            status=status.HTTP_201_CREATED,
        )

    def put(self, request, id=None):
        if CustomUser.objects.filter(id=id).exists():
            user = CustomUser.objects.get(id=id)
            serializer = UserSerializer(user, data=request.data, many=False)
            serializer.is_valid(raise_exception=True)
            serializer.update(user, request.data)
            return Response(
                {
                    'message': 'User updated'
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    'message': 'User not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )





class UserLogin(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class Sites(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        objs = CustomUserSite.objects.all()
        serializer = UserSiteSerializer(objs, many=True)
        return Response(serializer.data)


class ChangeAccountAmount(APIView):
    permission_classes = [permissions.IsAdminUser]

    def post(self, request, id):
        if CustomUser.objects.filter(id=id).exists():
            user = CustomUser.objects.get(id=id)
            user.add_amount(request.data.get('amount', 0))
            user.save()
            return Response(
                {
                    'amount': user.amount
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    'message': 'User not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )


class AccountOrders(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, id=None):
        objs = CustomUser.objects.get(id=id).order_set.all()
        serializer = OrderSerializer(objs, many=True)
        return Response(serializer.data)


class UserAmount(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (JWTAuthentication,)

    def get(self, request):
        amount = request.user.amount
        return Response(amount)