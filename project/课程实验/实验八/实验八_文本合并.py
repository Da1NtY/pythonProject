'''
假设有两个文本文件file1.txt和file2.txt，编写程序merge.py，
把两个文本文件中的内容合并到新文件result.txt中，
要求文件file1.txt和file2.txt中的行在result.txt中交替出现。
即result.txt中的奇数行来自file1.txt，偶数行来自file2.txt。
如果两个文件行数不一样，那么处理完行数较少的文件之后，把另一个文件中剩余的所有行直接追加到result.txt的最后。
并且读取result.txt文件中的内容，在屏幕输出显示。
测试文档
file1.txt							file2.txt
【提示】
可同时打开三个文件，通过双重循环，交替将file1.txt和file2.txt的每一行写入result.txt中（在内循环中，每写入一行后，可用break语句退出内循环，可实现交替写入）。
循环结束后，再读出内循环中的文件对象其余的内容，写入result.txt中。

'''
import os

def merge_files(file1, file2, output_file):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as out:
            file1_lines = f1.readlines()
            file2_lines = f2.readlines()

            while file1_lines and file2_lines:
                line1 = file1_lines.pop(0)
                line2 = file2_lines.pop(0)
                out.write(line1)
                out.write(line2)

            remaining_lines = file1_lines + file2_lines
            out.writelines(remaining_lines)

        print(f"文件 {file1} 和 {file2} 已成功合并为 {output_file}")

    except FileNotFoundError:
        print("一个或多个输入文件不存在。请检查文件路径是否正确。")
    except IOError:
        print("读写文件时发生错误。请检查文件权限。")
    except Exception as e:
        print(f"发生未知错误: {e}")

if __name__ == "__main__":
    file1 = "file1.txt"
    file2 = "file2.txt"
    output_file = "result.txt"

    if os.path.exists(file1) and os.path.exists(file2):
        merge_files(file1, file2, output_file)
    else:
        print("一个或多个输入文件不存在。请检查文件路径是否正确。")