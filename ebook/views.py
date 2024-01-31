from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from ebook.models import Ebook, Author
from ebook.serializers import EbookSerializer, AuthorSerializer


class CreateEbookView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        ebook_serializer = EbookSerializer(data=request.data)

        # validating for already existing data
        if Ebook.objects.filter(**request.data).exists():
            raise serializers.ValidationError('Ebook já cadastrado')

        if ebook_serializer.is_valid():
            ebook_serializer.save()
            return Response(ebook_serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class UpdateEbookView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        ebook = Ebook.objects.get(pk=pk)
        ebook_serializer = EbookSerializer(instance=ebook, data=request.data)

        if ebook_serializer.is_valid():
            ebook_serializer.save()
            return Response(ebook_serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class DeleteEbookView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        ebook = get_object_or_404(Ebook, pk=pk)
        ebook.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


class ListEbookView(APIView):

    def get(self, request):
        ebooks = Ebook.objects.all()
        if ebooks:
            ebook_serializer = EbookSerializer(ebooks, many=True)
            return Response(ebook_serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CreateAuthorView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        autor_serializer = AuthorSerializer(data=request.data)

        # validating for already existing data
        if Author.objects.filter(**request.data).exists():
            raise serializers.ValidationError('Autor já cadastrado')

        if autor_serializer.is_valid():
            autor_serializer.save()
            return Response(autor_serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ListAuthorView(APIView):

    def get(self, request):
        authors = Author.objects.all()
        if authors:
            author_serializer = AuthorSerializer(authors, many=True)
            return Response(author_serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


