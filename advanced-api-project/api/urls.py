from django.urls import path, include
from django.contrib import admin
from .views import BookListCreateAPIView, BookRetrieveUpdateDstroyAPIView

urlpatterns = [
    path('books/',
        BookListCreateAPIView.as_view(),
        name='book-list-create'),

    path('books/<int:pk>/',
        BookRetrieveUpdateDstroyAPIView.as_view(),
        name='book-detail-rub'),

    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls', namespace=rest_framework)),
]