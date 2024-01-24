from src.dataset import get_data

def test_data():
    data = get_data()
    assert isinstance(data, dict)
    assert all([key in ('train', 'val', 'class_map') for key in data.keys()])
    
if __name__ == "__main__":
    test_data()