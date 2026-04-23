import pandas as pd
def submission_res(test_data,pred):
    submission = pd.DataFrame({
        'Id':test_data.index,
        'prediction':pred
    })
    
    submission.to_csv('Outputs/submission.csv', index=False)
    return submission