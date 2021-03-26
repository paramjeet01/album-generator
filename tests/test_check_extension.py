from album.album_generator import check_extension

files = ["test.png","testy.jpg","myalbum.mp4"]
def test_chek_extension():
    assert check_extension(files) == ["test.png","testy.jpg"]
