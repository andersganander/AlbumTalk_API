from django.http import Http404
from rest_framework import generics, status, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Review
from .serializers import ReviewSerializer
from AlbumTalk_API.permissions import IsOwnerOrReadOnly


class ReviewList(generics.ListCreateAPIView):

    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # Not totally sure aabout this one...
    queryset = Review.objects.all()
    # Filters
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['album', 'owner__profile']

    # def get(self, request):
    #     reviews = Review.objects.all()
    #     serializer = ReviewSerializer(
    #         reviews, many = True, context = {'request': request}
    #     )
    #     print('GET')
    #     return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # def post(self, request):
    #         serializer = ReviewSerializer(
    #             data=request.data, context ={'request': request}
    #         )
    #         if serializer.is_valid():
    #             serializer.save(owner=request.user)
    #             return Response(
    #                 serializer.data, status=status.HTTP_201_CREATED
    #             )

    #         return Response(
    #             serializer.errors, status=status.HTTP_400_BAD_REQUEST
    #         )

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a review and edit or delete it if you own it.
    """
    serializer_class = ReviewSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Review.objects.all()

    # queryset = Review.objects.annotate(
    #     likes_count=Count('likes', distinct=True),
    #     comments_count=Count('comment', distinct=True)
    # ).order_by('-created_at')
    #queryset = Review.objects().order_by('-created_at')

    # def get_object(self, pk):
    #     try:
    #         review = Review.objects.get(pk=pk)
    #         self.check_object_permissions(self.request, review)
    #         return review
    #     # TODO Check this exception !!!
    #     except Review.DoesNotExist:
    #         raise Http404

    # def get(self, request, pk):
    #     review = self.get_object(pk)
    #     serializer = ReviewSerializer(
    #         review, context={'request': request}
    #     )
    #     return Response(serializer.data)

    # def put(self, request, pk):
    #     review = self.get_object(pk)
    #     serializer = ReviewSerializer(
    #         review, data=request.data, context={'request': request}
    #     )
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(
    #         serializer.errors, status=status.HTTP_400_BAD_REQUEST
    #     )

    # def delete(self, request, pk):
    #     review = self.get_object(pk)
    #     review.delete()
    #     return Response(
    #         status=status.HTTP_204_NO_CONTENT
    #     )

