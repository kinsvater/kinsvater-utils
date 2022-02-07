from typing import Union, List

import pandas as pd


def anti_join(x: pd.DataFrame, y: pd.DataFrame, on=Union[str, List[str]]) -> pd.DataFrame:
    """Keeps rows of x which, by key, are not available in y."""
    if not isinstance(on, list):
        on = [on]
    df = pd.merge(left=x, right=y.filter(items=on).drop_duplicates(), how='left', indicator=True, on=on)
    return df.loc[df['_merge'] == 'left_only', :].drop(columns='_merge').reset_index(drop=True)


def semi_join(x: pd.DataFrame, y: pd.DataFrame, on=Union[str, List[str]]) -> pd.DataFrame:
    """Keeps rows of x which, by key, are also available in y."""
    if not isinstance(on, list):
        on = [on]
    return pd.merge(left=x, right=y.filter(items=on).drop_duplicates(), how='inner', on=on)
