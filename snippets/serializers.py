from django.contrib.auth.models import User

from rest_framework import serializers

from snippets.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')


class UserSerializer(serializers.ModelSerializer):
    # snippet 에서 user 정보를 가지고 있으므로 ModelSerializer 가 기본적으로 snippet 들을 찾을 수 없어
    # 명시적으로 필드를 포함해줘야함
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')
