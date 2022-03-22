from django.urls import path
from news.api import (
    NewsListCreate,
    NewsUpdateDelete
)


urlpatterns = [
    path("api/news/", NewsListCreate.as_view()),
    path("api/news/<int:news_pk>/", NewsUpdateDelete.as_view()),
]
