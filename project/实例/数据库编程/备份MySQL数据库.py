import os
import time
import pymysql

# 生成一个备份文件名，名字由日期时间组成，便于通过文件名知道备份时间
def create_filename(db_name):
    file_name = db_name+'backup'+time.strftime('%Y%m%d-%H%M%S')+'.sql'
    return file_name

# 对数据库进行备份的函数
# host指定数据库服务的IP地址
def db_backup(host,db_name,user,passwd):
    print('开始备份'+db_name+'数据库')
    # 调用一个函数生成一个备份文件的名字
    filename = create_filename(db_name)
    # 指定备份文件的路径和名字
    path_name = './'+filename
    # 生成备份命令
    backupcmd = "mysqldump -h" + host + " -u" + user + " -p" + passwd + " " + db_name + " " + path_name
    # 执行备份命令
    os.system(backupcmd)
    print("备份完成！")

# 恢复数据的函数
def db_restore(host,db_name,user,passwd,filename):
    print('开始恢复' + db_name + '数据库')
    # 指定备份文件的路径和名字
    path_name = './'+filename
    # 生成数据恢复的命令
    recovercmd = "mysqldump -h" + host + "-u" + user + " -p" + passwd + " " + db_name + " < " + path_name
    # 执行恢复命令
    os.system(recovercmd)
    print('完成数据恢复！')

# 生成数据库的函数
def create_db(host,db_name,user,passwd):
    # 建立数据库连接
    conn = pymysql.connect(host=host, port=3306, user=user, passwd=passwd)
    # 建立一个游标
    cur = conn.cursor()
    # 建立一个空数据库
    cur.execute('create database '+db_name)
    # 关闭游标
    cur.close()
    # 断开连接
    conn.close()

# 删除数据库的函数
def delete_db(host,db_name,user,passwd):
    conn = pymysql.connect(host=host, port=3306, user=user, passwd=passwd)
    cur = conn.cursor()
    # 删除数据库，慎用
    cur.execute('drop database '+db_name)
    cur.close()
    conn.close()

# 主函数
if __name__ == '__main__':
    # 初始化各变量
    host = 'localhost'
    user = 'root'
    passwd = '123456'
    db_name = 'mytest'
    # 调用函数进行备份
    db_backup(host,db_name,user,passwd)
    # 为测试，调用删除数据库
    delete_db(host,db_name,user,passwd)
    # 由于恢复数据库数据时，MySQL要求该数据库必须先存在才能恢复数据，因此先生成一个空的数据库用于恢复
    create_db(host,db_name,user,passwd)
    # 选一个备份文件，从中恢复数据
    filename = 'mytestbackup20240323-130518.sql'
    # 进行数据恢复
    db_restore(host,db_name,user,passwd,filename)
