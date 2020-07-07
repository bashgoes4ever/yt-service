from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import *
from rest_framework import status


class PlansClient(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, id=None):
        if id:
            obj = Plan.objects.get(id=id)
            serializer = PlanSerializer(obj, many=False)
            return Response(serializer.data)
        else:
            objs = Plan.objects.all()
            serializer = PlanSerializer(objs, many=True)
            return Response(serializer.data)


class Plans(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, id=None):
        if id:
            obj = Plan.objects.get(id=id)
            serializer = PlanSerializer(obj, many=False)
            return Response(serializer.data)
        else:
            objs = Plan.objects.all()
            serializer = PlanSerializer(objs, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = PlanSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                'message': 'Plan created',
            },
            status=status.HTTP_201_CREATED,
        )

    def put(self, request, id=None):
        if Plan.objects.filter(id=id).exists():
            plan = Plan.objects.get(id=id)
            serializer = PlanSerializer(plan, data=request.data, many=False)
            serializer.is_valid(raise_exception=True)
            serializer.update(plan, request.data)
            return Response(
                {
                    'message': 'Plan updated'
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    'message': 'Plan not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, id=None):
        if Plan.objects.filter(id=id).exists():
            Plan.objects.get(id=id).delete()
            return Response(
                {
                    'message': 'Plan deleted'
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    'message': 'Plan not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )


class CustomPrices(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, id=None):
        if id:
            obj = CustomPlanPrices.objects.filter(user_id=id)
            serializer = CustomPricesSerializer(obj, many=True)
            return Response(serializer.data)
        else:
            objs = CustomPlanPrices.objects.all()
            serializer = CustomPricesSerializer(objs, many=True)
            return Response(serializer.data)

    def post(self, request, id=None):
        if request.data.get('prices'):
            for item in request.data.get('prices'):
                serializer = CustomPricesSerializer(data=item)
                serializer.is_valid(raise_exception=True)
                serializer.save()
        else:
            serializer = CustomPricesSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        if id:
            obj = CustomPlanPrices.objects.filter(user_id=id)
            serializer = CustomPricesSerializer(obj, many=True)
            return Response(serializer.data)

        return Response(
            {
                'message': 'Plan created',
            },
            status=status.HTTP_201_CREATED,
        )

    def delete(self, request, id=None):
        if CustomPlanPrices.objects.filter(id=id).exists():
            CustomPlanPrices.objects.get(id=id).delete()
            return Response(
                {
                    'message': 'CustomPlanPrices deleted'
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    'message': 'CustomPlanPrices not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )
