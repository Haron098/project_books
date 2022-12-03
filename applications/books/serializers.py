from rest_framework import serializers

from applications.books.models import Books


class BooksSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)

    class Meta:
        model = Books
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user

        books = Books.objects.create(owner=user, **validated_data)
        return books