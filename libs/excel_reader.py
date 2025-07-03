import pandas as pd
import os

def read_excel_first_column(file_path):
    """
    读取Excel文件的第一列数据
    
    Args:
        file_path (str): Excel文件路径
    
    Returns:
        list: 第一列的数据列表
    """
    try:
        # 检查文件是否存在
        if not os.path.exists(file_path):
            print(f"错误: 文件不存在 - {file_path}")
            return []
        
        # 读取Excel文件
        df = pd.read_excel(file_path)
        
        # 获取第一列数据
        first_column = df.iloc[:, 0].tolist()
        
        # 过滤掉空值和NaN
        first_column = [str(item).strip() for item in first_column if pd.notna(item) and str(item).strip()]
        
        print(f"成功读取Excel文件: {file_path}")
        print(f"第一列数据数量: {len(first_column)}")
        
        return first_column
        
    except Exception as e:
        print(f"读取Excel文件时出错: {e}")
        return []

def read_excel_first_column_with_header(file_path, has_header=True):
    """
    读取Excel文件的第一列数据，可选择是否包含表头
    
    Args:
        file_path (str): Excel文件路径
        has_header (bool): 是否包含表头，默认True
    
    Returns:
        list: 第一列的数据列表
    """
    try:
        # 检查文件是否存在
        if not os.path.exists(file_path):
            print(f"错误: 文件不存在 - {file_path}")
            return []
        
        # 读取Excel文件
        if has_header:
            df = pd.read_excel(file_path)
        else:
            df = pd.read_excel(file_path, header=None)
        
        # 获取第一列数据
        first_column = df.iloc[:, 0].tolist()
        
        # 过滤掉空值和NaN
        first_column = [str(item).strip() for item in first_column if pd.notna(item) and str(item).strip()]
        
        print(f"成功读取Excel文件: {file_path}")
        print(f"第一列数据数量: {len(first_column)}")
        
        return first_column
        
    except Exception as e:
        print(f"读取Excel文件时出错: {e}")
        return [] 