from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.http import JsonResponse
from account.models import User
from account.serializers import UserSerializer
from post.models import Post
from post.serializers import PostSerializer


@api_view(['POST'])
def search(request):
    data = request.data
    query = data['query']

    users = User.objects.filter(name__icontains=query)
    users_serializers = UserSerializer(users, many=True)

    posts = Post.objects.filter(body__icontains=query)
    posts_serializers = PostSerializer(posts, many=True)
    return JsonResponse({
        'users': users_serializers.data,
        'posts': posts_serializers.data,
    }, safe=False)
