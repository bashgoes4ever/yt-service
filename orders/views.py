from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import *
from rest_framework import status
from utilities.permissions import IsOwner
from accounts.backends import JWTAuthentication


class Orders(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, id=None):
        if id:
            obj = Order.objects.get(id=id)
            serializer = OrderSerializer(obj, many=False)
            return Response(serializer.data)
        else:
            objs = Order.objects.all()
            serializer = OrderSerializer(objs, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = OrderCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )

    def put(self, request, id=None):
        if Order.objects.filter(id=id).exists():
            order = Order.objects.get(id=id)
            serializer = OrderCreateSerializer(order, data=request.data, many=False)
            serializer.is_valid(raise_exception=True)
            serializer.update(order, request.data)
            return Response(
                {
                    'message': 'order updated'
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    'message': 'order not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )


class Statuses(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        objs = OrderStatus.objects.all()
        serializer = OrderStatusSerializer(objs, many=True)
        return Response(serializer.data)


class OrdersClient(APIView):
    permission_classes = [IsOwner]
    authentication_classes = (JWTAuthentication,)

    def get(self, request):
        objs = Order.objects.filter(user=request.user).order_by('-date')
        serializer = ClientOrderSerializer(objs, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.user)
        request.data['user'] = request.user.id
        serializer = ClientOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )


class CalculatePrice(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (JWTAuthentication,)

    def get(self, request):
        plan = Plan.objects.get(id=request.GET.get('plan'))
        total_price = int(plan.price) * int(request.GET.get('amount'))
        price = plan.price
        if request.user.customplanprices_set.exists():
            for range in request.user.customplanprices_set.filter(plan=plan):
                if range.min_amount <= int(request.GET.get('amount')) <= range.max_amount:
                    price = range.price
                    total_price = price * int(request.GET.get('amount'))
                    break
        return Response({
            'amount': request.GET.get('amount'),
            'price': price,
            'total_price': total_price
        })
