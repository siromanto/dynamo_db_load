import pandas as pd
import numpy as np

def transform_csv():
    """Get the original csv file and make new one for dynamo db"""
    with open('../data/diabetic_data.csv', 'r', encoding='utf-8') as f:
        df = pd.read_csv(f)

        print('Test')
        table_columns = df.columns.tolist()
        print(len(table_columns))
        table_columns.insert(0, 'generated_date')
        print(table_columns)
        print(len(table_columns))

        df1 = df.head(300)  # TODO: There is 65k records in csv. What count will we need?

        for index, row in df1.iterrows():
            df1.loc[index, 'generated_date'] = generate_date()

        print(df1)

        df_repeated = pd.concat([df1] * 10, ignore_index=True)
        print(df_repeated)

        # df_repeated.to_csv('../data/transformed_data.csv', sep='\t', encoding='utf-8')
        df_repeated.to_csv('../data/transformed_data.csv', index=False)

def generate_date():
    date = f'2019-08-{np.random.randint(1, 6)}'
    # print(date)
    return date


if __name__ == '__main__':
    transform_csv()
