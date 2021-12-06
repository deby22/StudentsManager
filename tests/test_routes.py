
def test_empty_db(client):
    """Start with a blank database."""

    response = client.get('/students')
    assert [] == response.json
