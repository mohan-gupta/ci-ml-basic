from src.dataset import get_data

def test_data():
    data = get_data()
    assert isinstance(data, dict), 'Expected return value type: dict'
    assert all([key in ('train', 'val', 'class_map') for key in data.keys()]), "expected keys to be one of the following: ('train', 'val', 'class_map')"
    
if __name__ == "__main__":
    test_data()