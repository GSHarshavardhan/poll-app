from .models import Poll, Choice
from rest_framework import serializers


class ChoiceSerializer(serializers.ModelSerializer):
    choice_id = serializers.IntegerField(source='id', read_only= True)

    class Meta:
        model = Choice
        fields = ['choice_id','choice_text']
        read_only_fields = ['choice_id']

class ChoiceWithVoteSerializer(ChoiceSerializer):
    class Meta(ChoiceSerializer.Meta):
        fields = ChoiceSerializer.Meta.fields + ['vote_count']
        read_only_fields = ChoiceSerializer.Meta.read_only_fields + ['vote_count']

class PollSerializer(serializers.ModelSerializer):
    poll_id = serializers.IntegerField(source= 'id', read_only= True)
    choices = ChoiceSerializer(many= True)

    class Meta:
        model= Poll
        fields = ['poll_id', 'question_text', 'choices']
        read_only_fields= ['poll_id']
    
    def create(self, validated_data):
        choices_data = validated_data.pop('choices')
        poll = Poll.objects.create(**validated_data)
        for choice_data in choices_data:
            Choice.objects.create(poll= poll, **choice_data)
        return poll

class PollWithVoteSerializer(PollSerializer):
    choices = ChoiceWithVoteSerializer(many= True)

class VoteSerializer(serializers.Serializer):
    poll_id = serializers.IntegerField()
    choice_id = serializers.IntegerField()
