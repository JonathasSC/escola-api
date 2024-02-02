from rest_framework import serializers
from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'avaliacao',
            'comentario',
            'criacao',
            'ativo'
        )

    def to_representation(self, instance):
        request = self.context.get('request')

        if request and request.user.is_authenticated:
            return super().to_representation(instance)
        else:
            data = super().to_representation(instance)
            data.pop('email', None)
            return data


class CursoSerializer(serializers.ModelSerializer):
    # Primary Key Related Field
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes',
        )
