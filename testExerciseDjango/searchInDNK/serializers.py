from rest_framework import serializers

class SearcherDNKSerializer(serializers.Serializer):
    codon = serializers.CharField()