# 代码生成时间: 2025-09-19 08:34:10
import pandas as pd
from sqlalchemy import create_engine, text

# 函数：连接数据库
def connect_to_database(username, password, host, database):
    try:
        engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}/{database}")
        connection = engine.connect()
        print("Database connection established successfully")
        return connection
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# 函数：执行安全的SQL查询
def execute_safe_query(connection, query, params):
    """
    执行安全的SQL查询，防止SQL注入。
    
    参数:
    connection: 数据库连接对象
    query: SQL查询字符串
    params: 查询参数字典
    
    返回:
    pandas DataFrame对象，包含查询结果
    """
    try:
        result = pd.read_sql_query(query, connection, params=params)
        print("Query executed successfully")
        return result
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# 主函数：演示防止SQL注入的程序
def main():
    # 数据库配置
    username = "your_username"
    password = "your_password"
    host = "localhost"
    database = "your_database"

    # 连接数据库
    connection = connect_to_database(username, password, host, database)
    if connection is None:
        return

    # 安全的SQL查询
    query = "SELECT * FROM users WHERE username = :username AND password = :password"
    params = {"username": "example_user", "password": "example_pass"}
    result = execute_safe_query(connection, query, params)

    if result is not None:
        print(result)

if __name__ == "__main__":
    main()