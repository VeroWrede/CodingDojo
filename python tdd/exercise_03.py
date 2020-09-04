    ## Adding to the AlbumTest class we were working in already
    def test_view_edit(self):
        ## For this one, we have given you a good jumping off point, but it's still
        ## up to you to create the url and the view function to make this test pass
        c = Client()
        post_data = {
            "title": "A Test Edit",
            "artist" : "Test Artist Edit",
            "year": 3099
        }
        # This should edit the single album that is created by our setUp method
        response = c.post('/album/1/edit', post_data)
        # Let's make sure the view function eventually redirects
        self.assertEqual(response.status_code, 302)
        # Let's test to make sure the edit worked
        edited = Album.objects.get(id = 1)
        self.assertEqual(edited.title, post_data['title'])
        self.assertEqual(edited.artist, post_data['artist'])
        self.assertEqual(edited.year, post_data['year'])
    def test_view_delete(self):
        # Test to make sure a view function can retrieve an album based on an id being sent in the url
        # Test to make sure that this specific album gets deleted
    
    def test_view_read(self):
        # Test to make sure a view function can retrieve an album based on an id being sent in the url
        # Make sure this single record is getting passed via context
        