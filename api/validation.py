import pandas as pd


def validate_data(df: pd.DataFrame) -> bool:
    if df.empty:
        print("No articles downloaded. FInishing execution")
        return False

    if pd.Series(df['id']).is_unique:
        pass
    else:
        raise Exception("Duplicate articles found!")
    
    
    if df.isnull().values.any():
        raise Exception("Null values found!")
    return True