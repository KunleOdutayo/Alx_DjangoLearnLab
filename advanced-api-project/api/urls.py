from django.urls import path, include
from django.contrib import admin
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView
BookListCreateAPIView, BookRetrieveUpdateDstroyAPIView

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

    path('books/', 
        BookListView.as_view(),
        name='book-list'),

    path('book/create/',
        BookCreateView.as_view(),
        name='book-create'),
    
    path('book/<int:pk>/update/',
        BookUpdateView.as_view(),
        name='book-update'),
         
    path('books/<int:pk>/delete/',
        BookDeleteView.as_view(),
        name='book-delete'),
]