from django.shortcuts import render

from django.http import JsonResponse

# third party imports
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins

from .serializers import PostSerializer
from .models import Post

# example level 1
def test_view(request):
    data = {
        'name': 'john',
        'age': 23
    }
    return JsonResponse(data)


# example level 2
class TestView(APIView):
    # def get(self, request, *args, **kwargs):
        # data = {
        #     'name': 'john',
        #     'age': 23
        # }
        # return Response(data)

    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        qs = Post.objects.all()
        # serializer = PostSerializer(qs, many=True)
        post = qs.first()
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


# example level 3
class PostView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# example level 4
class PostCreateView(mixins.ListModelMixin,
                     generics.CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

# example level 5
class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
