from rest_framework import serializers
from .models import Author, Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        current_year = date.today().year

        if value > current_year:
            raise serializers.ValidationError(
                f"Publicatio year cannot be in the future. Max allowed year is {current_year}."
            )
        return value
    
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']