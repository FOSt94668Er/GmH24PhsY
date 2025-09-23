# 代码生成时间: 2025-09-23 13:49:52
import pandas as pd

"""
排序算法实现模块，使用Pandas框架。
提供对DataFrame进行排序的功能。
"""


def bubble_sort(df, column):
    """
    冒泡排序算法实现，对DataFrame指定列进行排序。
    
    参数：
    df (pd.DataFrame): 待排序的DataFrame
    column (str): 需要排序的列名
    
    返回值：
    pd.DataFrame: 排序后的DataFrame
    
    异常：
    ValueError: 如果指定的列名不存在
    """
    if column not in df.columns:
        raise ValueError(f"列名 '{column}' 不存在于DataFrame中")
    
    length = len(df)
    for i in range(length):
        for j in range(0, length - i - 1):
            if df[column].iloc[j] > df[column].iloc[j + 1]:
                df = df.swap(df.index[j], df.index[j + 1])
    return df


def selection_sort(df, column):
    """
    选择排序算法实现，对DataFrame指定列进行排序。
    
    参数：
    df (pd.DataFrame): 待排序的DataFrame
    column (str): 需要排序的列名
    
    返回值：
    pd.DataFrame: 排序后的DataFrame
    
    异常：
    ValueError: 如果指定的列名不存在
    """
    if column not in df.columns:
        raise ValueError(f"列名 '{column}' 不存在于DataFrame中")
    
    length = len(df)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if df[column].iloc[j] < df[column].iloc[min_index]:
                min_index = j
        df = df.swap(df.index[i], df.index[min_index])
    return df


def insertion_sort(df, column):
    """
    插入排序算法实现，对DataFrame指定列进行排序。
    
    参数：
    df (pd.DataFrame): 待排序的DataFrame
    column (str): 需要排序的列名
    
    返回值：
    pd.DataFrame: 排序后的DataFrame
    
    异常：
    ValueError: 如果指定的列名不存在
    """
    if column not in df.columns:
        raise ValueError(f"列名 '{column}' 不存在于DataFrame中")
    
    length = len(df)
    for i in range(1, length):
        key = df.loc[df.index[i], column]
        j = i - 1
        while j >= 0 and key < df.loc[df.index[j], column]:
            df = df.swap(df.index[j + 1], df.index[j])
            j -= 1
    return df


def main():
    """
    主函数，用于演示排序算法的实现。
    """
    # 创建示例DataFrame
    data = {'Name': ['John', 'Anna', 'Peter', 'Linda'], 'Age': [28, 24, 35, 32]}
    df = pd.DataFrame(data)
    print("原始DataFrame：")
    print(df)

    # 排序示例
    sorted_df_bubble = bubble_sort(df.copy(), 'Age')
    print("冒泡排序后的DataFrame：")
    print(sorted_df_bubble)

    sorted_df_selection = selection_sort(df.copy(), 'Age')
    print("选择排序后的DataFrame：")
    print(sorted_df_selection)

    sorted_df_insertion = insertion_sort(df.copy(), 'Age')
    print("插入排序后的DataFrame：")
    print(sorted_df_insertion)

if __name__ == '__main__':
    main()