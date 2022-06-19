from rest_framework import serializers

from .models import Like, Post, Comment


class FilterRewiewListSerializer(serializers.ListSerializer):
    """Фильтр комментариев, только parents"""
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializar(serializers.Serializer):
    """Рекурсивный вывод дочерник комментариев"""
    def to_representation(self, instance):
        serializers = CommentDetailSerealizers(instance, context=self.context)
        return serializers.data


class RecursiveThirdLevelSerializer(serializers.Serializer):
    """Рекурсивный вывод комментариев до 3-ого уровня вложенности"""
    def to_representation(self, instance):
        if instance.level < 3:
            return CommentViewSerealizers(instance, context=self.context).data


class CommentViewSerealizers(serializers.ModelSerializer):
    """Вывод вложенных комментариев до 3 уровня"""
    children = RecursiveThirdLevelSerializer(many=True)

    class Meta:
        list_serializer_class = FilterRewiewListSerializer
        model = Comment
        fields = ('id', 'name', 'text', 'children', 'level')


class CommentDetailSerealizers(serializers.ModelSerializer):
    """Вывод всех комментариев конкретного поста"""
    children = RecursiveSerializar(many=True)

    class Meta:
        list_serializer_class = FilterRewiewListSerializer
        model = Comment
        fields = ('id', 'name', 'text', 'children')


class CommentCreateSerializars(serializers.ModelSerializer):
    """Добавление комментария"""
    name = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        list_serializer_class = FilterRewiewListSerializer
        model = Comment
        fields = '__all__'


class LikesSerializers(serializers.ModelSerializer):
    """Вывод лайков/дизлайков"""
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Like
        fields = '__all__'
    
    def create(self, validated_data):
        return Like.objects.update_or_create(
            user=validated_data.get('user'),
            post=validated_data.get('post'),
            defaults={'like': validated_data.get('like')}
        )


class PostSerializaers(serializers.ModelSerializer):
    """Вывод списка постов"""
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    post_like = LikesSerializers(many=True)
    count_all_likes = serializers.SerializerMethodField()
    count_all_dislikes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'count_all_likes',
                  'count_all_dislikes', 'author', 'post_like')

    def get_count_all_likes(self, instans):
        return Like.objects.all().filter(post=instans).filter(like='like').count()

    def get_count_all_dislikes(self, instans):
        return Like.objects.all().filter(post=instans).filter(like='dislike').count()

    def create(self, validated_data):
        like_or_dislike = Like.objects.update_or_create(
            user=validated_data.get('user'),
            post_id=validated_data.get('post_id'),
            defaults={'like': validated_data.get('like')}
        )
        return like_or_dislike


class PostCreateSerializers(serializers.ModelSerializer):
    """Добавление постов"""
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = ('title', 'author')


class PostDetaiSerializaers(serializers.ModelSerializer):
    """Вывод детальной информации о посте"""
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    post_comment = CommentViewSerealizers(many=True)
    post_like = LikesSerializers(many=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'post_comment', 'post_like')