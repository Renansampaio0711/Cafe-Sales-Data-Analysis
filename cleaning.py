def clean(df):
    import pandas as pd
    import numpy as np
    from pandas.api.types import is_string_dtype

    # remove spaces and convert to lowercase for string columns
    
    df = df.apply(
    lambda col: col.str.strip().str.lower()
    if is_string_dtype(col)
    else col
)
    # replace error values with NaN
    error = {
    'error': np.nan,
    'err': np.nan,
    'unknown': np.nan,
    'unkown': np.nan,
    'nan': np.nan
}
    df.replace(error, inplace=True)

    # convert columns to appropriate data types
    df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
    df['Price Per Unit'] = pd.to_numeric(df['Price Per Unit'], errors='coerce')
    df['Total Spent'] = pd.to_numeric(df['Total Spent'], errors='coerce')
    df["Transaction Date"] = pd.to_datetime(df["Transaction Date"])

    # drop duplicates
    df.drop_duplicates(inplace=True)

    # recalculate Total Spent
    df['Total Spent'] = df['Quantity'] * df['Price Per Unit']


    return df