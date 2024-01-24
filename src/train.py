import joblib

import config
import dataset
import model_dispatcher

def main():
    data = dataset.get_data()
    X_train, y_train = data['train'].drop(['target'], axis=1).values, data['train']['target'].values
    X_val, y_val = data['val'].drop(['target'], axis=1).values, data['val']['target'].values
    
    selected_model = 'lr'
    model = model_dispatcher.model[selected_model]
    
    model.fit(X_train, y_train)
    
    train_score = model.score(X_train, y_train)
    val_score = model.score(X_val, y_val)
    print(f"Validation score: {val_score:.3}, Train score: {train_score:.3}")
    
    joblib.dump(model, config.MODEL_PATH.format(model_name=selected_model, score=val_score))
    print("model saved")
    
if __name__ == "__main__":
    main()
