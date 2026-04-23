from sklearn.linear_model import LinearRegression,Ridge
from sklearn.model_selection import train_test_split,cross_val_score,GridSearchCV
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
import numpy as np

## full training pipeline
def full_training_pipeline(df):
    X = df.drop('SalePrice',axis =1) ## independent variable
    y = df['SalePrice']  ## dependent variable
    
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42) ## splitting the dataset into train and test

    scaler = StandardScaler()                                                         ## scaling the features for better learning 
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    linear_model = LinearRegression()                                                ## training using linear regression
    linear_model.fit(X_train,y_train)
    linear_pred = linear_model.predict(X_test)
    linear_rmse = np.sqrt(mean_squared_error(linear_pred,y_test))

    ridge_model = Ridge()
    params = {'alpha': np.logspace(-3, 3, 50)}
    grid = GridSearchCV(ridge_model,params,scoring='neg_mean_squared_error',cv=10)
    grid.fit(X_train_scaled,y_train)
    best_ridge = grid.best_estimator_
    ridge_pred = best_ridge.predict(X_test_scaled)
    ridge_rmse = np.sqrt(mean_squared_error(ridge_pred,y_test))

    if ridge_rmse < linear_rmse :
        best_model = best_ridge
        is_scaled = True
    else:
        best_model = linear_model
        is_scaled = False
    return best_model,scaler,is_scaled,X.columns


    
    




    
    
    