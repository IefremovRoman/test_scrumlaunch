from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


from .models import NewsTable
from .serializers import NewsSerializer


class NewsListCreate(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = NewsSerializer
    queryset = NewsTable.objects.all()


class NewsUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = NewsSerializer
    queryset = NewsTable.objects.all()
    lookup_url_kwarg = "news_pk"
