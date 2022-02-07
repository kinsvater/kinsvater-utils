import pandas as pd

from kinsvater_utils.tables import anti_join, semi_join


def test_anti_and_semi_join():
    df1 = pd.DataFrame({'key1': ['a', 'b', 'c', 'd'],
                        'key2': [1, 2, 3, 4],
                        'col': ['w', 'x', 'y', 'z']})

    df2 = pd.DataFrame({'key1': ['a', 'b', 'c'],
                        'key2': [1, 0, 3],
                        'other_col': [7, 8, 9]})

    df_from_anti_join = anti_join(x=df1, y=df2, on=['key1', 'key2'])
    df_expected = pd.DataFrame({'key1': ['b', 'd'],
                                'key2': [2, 4],
                                'col': ['x', 'z']})
    pd.testing.assert_frame_equal(df_from_anti_join, df_expected)

    df_from_semi_join = semi_join(x=df1, y=df2, on=['key1', 'key2'])
    df_expected = pd.DataFrame({'key1': ['a', 'c'],
                                'key2': [1, 3],
                                'col': ['w', 'y']})
    pd.testing.assert_frame_equal(df_from_semi_join, df_expected)
