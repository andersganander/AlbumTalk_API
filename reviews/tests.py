
from django.contrib.auth.models import User
from .models import Review
from .models import Album

from rest_framework import status
from rest_framework.test import APITestCase


class ReviewListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='db', password='heroes')
        Album.objects.create(title='heroes', artist='David Bowie', release_year=1977, audiodb_idAlbum=1, audiodb_idArtist=1)
        Album.objects.create(title='Low', artist='David Bowie', release_year=1977, audiodb_idAlbum=2, audiodb_idArtist=2)
        Album.objects.create(title='Lodger', artist='David Bowie', release_year=1979, audiodb_idAlbum=3, audiodb_idArtist=3)

    def test_can_list_reviews(self):
        db = User.objects.get(username='db')
        album = Album.objects.get(title='heroes')
        Review.objects.create(owner=db, album=album, rating=3, content='testing')
        album = Album.objects.get(title='Low')
        Review.objects.create(owner=db, album=album, rating=4, content='testing 2')
        album = Album.objects.get(title='Lodger')
        Review.objects.create(owner=db, album=album, rating=5, content='testing 3')
        response = self.client.get('/reviews/')
        count = Review.objects.count()
        self.assertEqual(count, 3)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_review(self):
        self.client.login(username='db', password='heroes')
        album = Album.objects.get(title='heroes')
        response = self.client.post('/reviews/', {'album':album.pk, 'rating':5, 'content':'test2'})
        count = Review.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print(response.data)

    def test_user_not_logged_in_cant_create_review(self):
        album = Album.objects.get(title='heroes')
        response = self.client.post('/reviews/', {'album':album.pk, 'rating':5, 'content':'test2'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class ReviewDetailViewTests(APITestCase):
    def setUp(self):
        user1 = User.objects.create_user(username='user1', password='pass')
        user2 = User.objects.create_user(username='user2', password='pass')
        Album.objects.create(title='heroes', artist='David Bowie', release_year=1977, audiodb_idAlbum=1, audiodb_idArtist=1)
        Album.objects.create(title='Low', artist='David Bowie', release_year=1977, audiodb_idAlbum=2, audiodb_idArtist=2)
        
        album = Album.objects.get(title='heroes')
        Review.objects.create(owner=user1, album=album, rating=3, content='user1 review')
        Review.objects.create(owner=user2, album=album, rating=4, content='user2 review')
        
    def test_can_retrieve_review_using_valid_id(self):
        response = self.client.get('/reviews/1/')
        self.assertEqual(response.data['content'], 'user1 review')
        response = self.client.get('/reviews/2/')
        self.assertEqual(response.data['content'], 'user2 review')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_review_using_invalid_id(self):
        response = self.client.get('/reviews/666/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_review(self):
        self.client.login(username='user1', password='pass')
        album = Album.objects.get(title='heroes')
        response = self.client.put('/reviews/1/', {'album':album.pk, 'rating':5, 'content':'updated review'})
        #response = self.client.put('/reviews/1/', {'content': 'a new review user1'})
        review = Review.objects.filter(pk=1).first()
        self.assertEqual(review.content, 'updated review')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_post(self):
        self.client.login(username='user1', password='pass')
        album = Album.objects.get(title='heroes')
        response = self.client.put('/reviews/2/', {'album':album.pk, 'rating':5, 'content':'updated review'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        

    def test_user_can_delete_own_post(self):
        self.client.login(username='user1', password='pass')
        
        response = self.client.get('/reviews/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.delete('/reviews/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get('/reviews/1/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_not_delete_another_post(self):
        self.client.login(username='user1', password='pass')
        response = self.client.delete('/reviews/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_not_review_same_album(self):
        self.client.login(username='user1', password='pass')
        album = Album.objects.get(title='heroes')
        response = self.client.post('/reviews/', {'album':album.pk, 'rating':5, 'content':'reviewing same album'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        print(response.data)


