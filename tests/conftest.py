import pytest
from mimesis import Text


@pytest.fixture
def some_data():
    text = Text('en')
    data = {
        'title': text.text(quantity=2),
        'body': text.text(quantity=2),
        'userId': 1
    }
    return data
