def create_features(df):
    df = df.copy()
    
    df['TotalArea'] = df['GrLivArea'] + df['TotalBsmtSF']
    df['TotalBathrooms'] = df['FullBath'] + 0.5 * df['HalfBath']
    df['HouseAge'] = 2025 - df['YearBuilt']
    
    # Drop redundant columns
    df = df.drop([
        'GrLivArea', 'TotalBsmtSF',
        'FullBath', 'HalfBath',
        'YearBuilt'
    ], axis=1)
    
    return df