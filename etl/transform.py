import pandas as pd
import numpy as np

from configs.config import ORIGIN_FILE, TRANSFORMED_FILE


def transform_csv(origin_file, transformed_file, rows=300, repeat=1):
    """
        Get the original csv file and make new one for dynamo db
    """

    with open(origin_file, 'r', encoding='utf-8') as f:
        df = pd.read_csv(f)
        table_columns = df.columns.tolist()
        table_columns.insert(0, 'generated_date')

        print(f'Origin file, ROWS, COLUMNS: {df.shape}')
        print(f'AVAILABLE COLUMNS: {table_columns}')

        df1 = df.head(rows)

        for index, row in df1.iterrows():
            df1.loc[index, 'generated_date'] = generate_date()

        df_repeated = pd.concat([df1] * repeat, ignore_index=True)
        print(f'Transformed file, ROWS, COLUMNS: {df_repeated.shape}')

        try:
            df_repeated.to_csv(transformed_file, index=False)
            print('file successfully created')
        except Exception as e:
            print(f'Failed to create a file: {e}')


def generate_date():
    date = f'2019-08-{np.random.randint(1, 6)}'
    return date


if __name__ == '__main__':
    transform_csv(ORIGIN_FILE, TRANSFORMED_FILE, rows=300, repeat=10)
