from django.test import TestCase, Client
from .models import *

class AlbumTest(TestCase):

    #seeding a DB for  tests
    @classmethod
    def setUpTestData(cls):
        Album.objects.create(title = "test album", artist = "me", year = "2020")
    '''def test_index(self):
        c = Client()
        response = c.get('/')
        # 200 OK: We have a working url with a valid view function
        self.assertEqual(response.status_code, 200)
    
    def test_create_album(self):
        c = Client()
        response = c.get('/album/create')
        # 302 Redirect: We have a working url with a view function that redirects
        self.assertEqual(response.status_code, 302)'''

    def test_urls(self):
        c = Client()
        idx_response = c.get('/')
        # 200 OK: the url is working and has a valid view function
        self.assertEqual(idx_response.status_code, 200)
        create_response = c.get('/album/create' )
        # 302 Redirect: url is working and has a function that redirects
        self.assertEqual(create_response.status_code, 302)

    def test_model_creation(self):
        a = Album.objects.create(title = "test model creation", artist = "me", year = 2020)
        self.assertEqual(a.title, "test model creation")
        self.assertEqual(a.artist, "me")
        self.assertEqual(a.year, 2020)

    def test_model_get(self):
        a = Album.objects.get(id = 1)
        self.assertEqual(a.id, 1)
        self.assertIsInstance(a, Album)

    def test_model_edit(self):
        a = Album.objects.first()
        a.title = "test edited"
        a.artist = "moi"
        a.year = 202
        a.save()
        edited_a = Album.objects.first()
        self.assertEquals(edited_a.title, "test edited")
        self.assertEqual(edited_a.artist, "moi")
        self.assertEqual(edited_a.year, 202)

    def test_model_delete(self):
        # Delete will return a tuple that holds the number of entities deleted in the 0 index
        # hardcoded 1 might need to get changed if using other methods like .all() od .filter()
        num_deleted = Album.objects.get(id = 1).delete()[0]
        self.assertEqual(num_deleted, 1)

    def test_view_create(self):
        c = Client()
        post_data = {
            "title" : "view test",
            "artist" : "meme",
            "year" : 2020
        }
        response = c.post("/album/create", post_data)
        self.assertEqual(response.status_code, 302)
        # check if posted correctly
        new_album = Album.objects.last()
        self.assertEqual(new_album.title, post_data["title"])
        self.assertEqual(new_album.artist, post_data["artist"])
        self.assertEqual(new_album.year, post_data["year"])
        #print('test_view_create title: ', new_album.title)

    def test_context(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.context['answer'], 42)
    
    def test_view_edit(self):
        c = Client()
        post_data = {
            "title" : "edit test",
            "artist" : "arist edit",
            "year" : 1999
        }
        response = c.post("/album/1/edit", post_data)
        self.assertEqual(response.status_code, 302)

        edited_album = Album.objects.get(id = 1)
        self.assertEqual(edited_album.title, post_data["title"])
        
        self.assertEqual(edited_album.artist, post_data["artist"])
        self.assertEqual(edited_album.year, post_data["year"])
        #print('test_view_edit title :', edited_album.title)

    def test_view_deleted(self):
        # Test to make sure a view function can retrieve an album based on an id being sent in the url
        # Test to make sure that this specific album gets deleted
        c = Client()
        id = {"id" : 1}
        response = c.post('/album/delete', id)
        #assert (Album.objects.get(id=id["id"]), "Album of id = 1 was deleted")

    def test_view_read(self):
        # Test to make sure a view function can retrieve an album based on an id being sent in the url
        # Make sure this single record is getting passed via context
        c = Client()
        response = c.get("/album/1/read")
        a = Album.objects.get(id = 1)
        self.assertEqual(response.context["Album"], a)









