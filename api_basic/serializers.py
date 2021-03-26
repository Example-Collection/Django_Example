from abc import ABC

from rest_framework import serializers
from .models import Article


class ArticleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'author', 'email']

    # def create(self, validated_data):
    #     return Article.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.email = validated_data.get('email', instance.email)
        # save() : Saves instance to database.
        instance.save()
        return instance

    # How to use Serializer

    # 1. create new Article
    # article = Article(title = "sample title", author = "sample author", email = "sample@email.com")

    # 2. save new Article instance
    # article.save()

    # 3. Create new ArticleSerializer instance.
    # serializer = new ArticleSerializer(article)

    # 4. Read data as JSON format using `serializer.data` .
    # Output : {'title': 'sample title', 'author': 'sample author', email: 'sample@email.com'}

    # 5. Render data as JSON format.
    # content = JSONRenderer().render(serializer.data);
    # JSONRenderer above is imported from `rest_framework.renderers`.

    # 6. To render more than 1 objects
    # Use the code below.
    # serializer = ArticleSerializer(Article.objects.all(), many=True)
