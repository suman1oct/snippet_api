# python imports

#django imports

# third party imports
from rest_framework import serializers

#local imports
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES



class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')