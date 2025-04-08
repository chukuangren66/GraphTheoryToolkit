
from linear_Programing import process_multiple_graphs
from read_graph_from_file import read_graph_from_file

def main():
    file_name = ('10-k-2_10-25.in')  # 文件名，需根据实际情况修改
    graphs = read_graph_from_file(file_name)
    print(graphs)

if __name__ == '__main__':
    main()