from typing import TypeVar, Union

import numpy as np
import pandas
import pandas as pd
from pandas.core.arrays import ExtensionArray

T = TypeVar('T')


def read_data() -> dict[T, np.ndarray]:
    pass


def __read_data() -> dict[T, np.ndarray]:
    pass


def read_test_tsv() -> tuple[Union[ExtensionArray, np.ndarray], Union[ExtensionArray, np.ndarray]]:
    df = __read_test_tsv()
    ndarrays = [df[col].values for col in df.columns]
    # print(ndarrays[1])
    # print(ndarrays[2])

    return ndarrays[1], ndarrays[2]


def __read_test_tsv() -> pd.DataFrame:
    df = pd.read_csv("./data/test.tsv", sep='\t', header=None)
    # print(df)

    return df


def write_test_to_excel():
    df = pd.read_csv("../data/test.tsv", sep='\t', header=None)
    ndarrays = [df[col].values for col in df.columns]
    data_list = ndarrays[1].tolist()
    data = {'content': data_list}
    a = pandas.DataFrame(data)
    a.to_excel('../data/test_data.xlsx', sheet_name='Sheet1', index=False)


def read_train_tsv() -> tuple[Union[ExtensionArray, np.ndarray], Union[ExtensionArray, np.ndarray]]:
    df = __read_test_tsv()
    ndarrays = [df[col].values for col in df.columns]
    # print(ndarrays[1])
    # print(ndarrays[2])

    return ndarrays[1], ndarrays[2]


def __read_train_tsv() -> pd.DataFrame:
    df = pd.read_csv("../data/train.tsv", sep='\t', header=None)
    # print(df)

    return df


def read_dev_tsv() -> tuple[Union[ExtensionArray, np.ndarray], Union[ExtensionArray, np.ndarray]]:
    df = __read_test_tsv()
    ndarrays = [df[col].values for col in df.columns]
    # print(ndarrays[1])
    # print(ndarrays[2])

    return ndarrays[1], ndarrays[2]


def __read_dev_tsv() -> pd.DataFrame:
    df = pd.read_csv("../data/dev.tsv", sep='\t', header=None)
    # print(df)

    return df


if __name__ == '__main__':
    write_test_to_excel()
