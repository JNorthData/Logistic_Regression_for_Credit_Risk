import pandas as pd

def examine(df):

    inf = df.dtypes
    ct = df.count()
    unique_values = df.nunique()
    missing_values = df.isnull().sum()
    mem = df.memory_usage(deep=True)
    formatted_mem = (mem / (1024 * 1024)).apply(lambda x: "{:,.1f}".format(x))

    summary_df = pd.DataFrame({
        'Type': inf,
        'Entries': ct,
        'Unique Values': unique_values,
        'Null/Missing Values': missing_values,
        'Memory Usage MB': formatted_mem
    }).fillna('0')

    summary_df[['Unique Values', 'Null/Missing Values', 'Entries']] = summary_df[['Unique Values', 'Null/Missing Values', 'Entries']].astype(int)

    summary_df.index.name = f'Row: {df.shape[0]} Col: {df.shape[1]}'

    summary_df = summary_df.iloc[1:]

    return summary_df