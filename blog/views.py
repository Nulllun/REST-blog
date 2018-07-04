from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions



@api_view(['GET'])
def user_list(request):

    if request.method=='GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return  Response(serializer.data)

@api_view(['GET'])
def user_detail(request, pk):

    try:
        user = User.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)


@api_view(['GET','POST'])
def post_list(request):

    if request.method=='GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method=='POST':
        serializer = PostSerializer(data=request.data)
        if not request.user.is_authenticated:
            return  Response(status=status.HTTP_401_UNAUTHORIZED)
        elif serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST','PUT','DELETE'])
def post_detail(request, pk):

    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method=='POST':
        serializer = CommentSerializer(data=request.data)
        if not request.user.is_authenticated:
            return  Response(status=status.HTTP_401_UNAUTHORIZED)
        elif serializer.is_valid():
            serializer.save(post=post,author=request.user.username)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method=="PUT":
        serializer = PostSerializer(post, data=request.data)
        if not request.user.is_authenticated:
            return  Response(status=status.HTTP_401_UNAUTHORIZED)
        elif serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method=="DELETE":
        if not request.user.is_authenticated:
            return  Response(status=status.HTTP_401_UNAUTHORIZED)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)