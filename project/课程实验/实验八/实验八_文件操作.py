'''
当前路径下的”./data/stock”文件夹中存储有若干用股票代码为文件名的csv文件中(如”600000.csv”、”600004.csv”等)，要求完成以下任务：
1）获取”./data/stock”路径下的所有文件名，以列表形式返回(不包含子路径中的文件名)
2）将stock文件夹中所有CSV文件中的数据合并到一个列表中。要求如下：
①读取任一文件的标题行，返回标题列表，并在标题列表最前面插入“Stock code”作为新增的标题项）
②将各文件的数据行读到一个列表中，每行数据的最前面增加一项该数据所在的文件名
③将标题列表和数据列表合并为一个列表
3）将第2）步得到的列表转为字典类型。标题为键，每只股票每天各指标的数据为值。
4）将第3）步得到的元素为字典类型的列表转为json格式写入文件，缩进4个字符，保持中文原样输出。
'''
import os
import json

def filename_list(path):  # path是形如 "./data/stock"的路径
    """接收路径字符串为参数，获取该路径下的所有文件名，以列表形式返回。
    os.listdir(path)以列表形式返回path路径下的所有文件名，不包括子路径中的文件名"""
    name_list = os.listdir(path)
    return name_list

def read_title(file):  # file是形如"./data/stock/600000.csv"的文件名
    """接收文件名为参数，读取文件第一行（标题行）为二维列表格式, 并在最前面插入'Stock code'作为新增的标题项。
    如文件第一行(标题行)为：Date,High,Low,Open,Close,Volume,Adj Close，
    返回形如[['Stock code','Date','High','Low','Open','Close','Volume','Adj Close']]的二维列表"""
    with open(file, 'r') as f:
        title_line = f.readline().strip().split(',')
        title_list = [['Stock code'] + title_line]
    return title_list

def read_file(file):  # file是形如"./data/stock/600000.csv"的文件名
    """接收文件名为参数，略过文件首行（标题行），读取文件内容为二维列表格式。
    将文件名以字符串类型加入，作为每个列表元素的第一个元素。
    如文件名为：600000.csv,
    文件的某行数据为：2010-01-04,………………,5.441317081451416
    该行数据对应的列表为：['600000','2010-01-04',………………,'5.441317081451416']"""
    data_lst = []
    with open(file, 'r') as f:
        next(f)  # 跳过标题行
        for line in f:
            data = line.strip().split(',')
            data_lst.append([os.path.basename(file).split('.')[0]] + data)
    return data_lst

def merge_data(path, name_list):  # path="./data/stock"
    """将stock下所有csv文件中的数据合并到一个列表中，列表第一个元素为：
    ['Stock code','Date','High','Low','Open','Close','Volume','Adj Close'] """
    merge_list = []
    for name in name_list:
        file = os.path.join(path, name)
        if name.endswith('.csv'):
            merge_list.extend(read_file(file))
    title_list = read_title(file)
    merge_list = title_list + merge_list
    return merge_list

def list_to_dict(merge_list):
    """接收包含数据的列表，将其转换为字典类型，列表一个子列表中的值（标题）分别作为键。"""
    keys = merge_list[0]
    merge_csv_dict = [{key: value for key, value in zip(keys, row)} for row in merge_list[1:]]
    return merge_csv_dict

def dict_to_json(merge_csv_dict, file_in_json):
    """将字典类型的数据写入json文件"""
    with open(file_in_json, 'w', encoding='utf-8') as f:
        json.dump(merge_csv_dict, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    path = "./data/stock"
    name_list = filename_list(path)
    merge_list = merge_data(path, name_list)
    merge_csv_dict = list_to_dict(merge_list)
    file_in_json = './data/stock.json'
    dict_to_json(merge_csv_dict, file_in_json)