import pytest
from artwork.models import Artwork

@pytest.mark.django_db
def test_create_artwork():
    artwork = Artwork.objects.create(title="Mona Lisa", status="In Exhibition", storage_location="Louvre Museum")
    assert artwork.title == "Mona Lisa"
    assert artwork.status == "In Exhibition"
    assert artwork.storage_location == "Louvre Museum"