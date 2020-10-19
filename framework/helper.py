from mimesis import Text


def broken_data():
    text = Text('en')
    data = {
        'title': text.text(quantity=2),
        'body': text.text(quantity=1400),
        'userId': 1
    }
    return data
