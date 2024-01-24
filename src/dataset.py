from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

def get_data():
    data = load_iris(as_frame=True)
    
    df = data['frame']
    class_map = data['target_names']
    
    train_df, val_df = train_test_split(
        df, shuffle=True, test_size=0.2, random_state=42, stratify=df['target']
        )
    
    return {
        "train": train_df,
        "val": val_df,
        "class_map": class_map
    }
