def plots(train_data,corr):
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    ## Heatmap
    plt.figure(figsize=(16,16))
    sns.heatmap(corr, cmap='coolwarm')
    plt.title("Correlation Heatmap")

    plt.show()

    ##Barplot
    
    top_corr = corr['SalePrice'].sort_values(ascending=False).head(10)

    plt.figure(figsize=(10,6))
    sns.barplot(x=top_corr.values, y=top_corr.index)
    plt.title("Top Features affecting Price")
    plt.show()

    ## Target Distribution
    sns.histplot(train_data['SalePrice'], kde=True)
    plt.title("SalePrice Distribution")

    plt.show()

    ##scattering distribution
    sns.scatterplot(x=train_data['OverallQual'], y=train_data['SalePrice'])
    plt.title("OverallQual vs SalePrice")
    plt.show()

    ## Box plot
    sns.boxplot(x=train_data['SalePrice'])
    plt.title("SalePrice Boxplot")

    plt.show()

    

    