def predict(model,scalar,is_scaled,test_df,train_cols):
    from preprocessing import clean_data
    from Feature_Engineering import create_features
    import pandas as pd
    test_df = clean_data(test_df)
    test_df = create_features(test_df)
    test_df = pd.get_dummies(test_df,drop_first = True)
    test_df = test_df.reindex(columns=train_cols,fill_value=0)
    if is_scaled:
        test_df = scalar.transform(test_df)
    pred = model.predict(test_df)
    return pred