from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Poll
from .serializers import *

@api_view(['GET', 'POST'])
def polls_view(request):
    
    if request.method == 'GET':
        polls = Poll.objects.all()
        serializer = PollSerializer(polls, many= True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PollSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def vote_view(request):
    serializer = VoteSerializer(data= request.data)
    if serializer.is_valid():
        poll = get_object_or_404(Poll, pk= serializer.validated_data['poll_id'])
        choice = get_object_or_404(Choice, pk= serializer.validated_data['choice_id'], poll= poll)
        choice.vote_count += 1
        choice.save()
        return Response("Successfully voted", status= status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)



