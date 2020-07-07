from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import *
from rest_framework.parsers import FileUploadParser
from rest_framework import status


class Articles(APIView):
    permission_classes = [permissions.IsAdminUser]
    parser_class = (FileUploadParser,)

    def get(self, request, id=None):
        if id:
            obj = Article.objects.get(id=id)
            serializer = ArticleSerializer(obj, many=False)
            return Response(serializer.data)
        else:
            objs = Article.objects.all()
            serializer = ArticleSerializer(objs, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                'message': 'Article created',
            },
            status=status.HTTP_201_CREATED,
        )

    def put(self, request, id=None):
        if Article.objects.filter(id=id).exists():
            article = Article.objects.get(id=id)
            serializer = ArticleSerializer(article, data=request.data, many=False)
            serializer.is_valid(raise_exception=True)
            serializer.update(article, request.data)
            return Response(
                {
                    'message': 'Article updated'
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    'message': 'Article not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, id=None):
        if Article.objects.filter(id=id).exists():
            Article.objects.get(id=id).delete()
            return Response(
                {
                    'message': 'Article deleted'
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    'message': 'Article not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )


class ArticlesClient(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, id=None):
        if id:
            obj = Article.objects.get(id=id)
            serializer = ArticleSerializer(obj, many=False)
            return Response(serializer.data)
        else:
            objs = Article.objects.all().order_by('-date')
            serializer = ArticleSerializer(objs, many=True)
            return Response(serializer.data)