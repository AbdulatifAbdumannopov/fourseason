from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView
from rest_framework import permissions
from .permissions import *

class PostList(ListCreateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostDelete(RetrieveDestroyAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class PostUpdate(RetrieveUpdateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)

def home(request):
    return render(request, 'home.html')

def maldives(request):
    return render(request, 'maldives.html')

def residents(request):
    if request.method == 'POST':
        status = request.POST.get('status')
        first_name = request.POST.get('name')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        data = {
            'status': status,
            'name': first_name,
            'lastname': last_name,
            'email': email
        }
        print(data)
    return render(request, 'residents.html')

def dining(request):
    return render(request, 'dinning.html')
