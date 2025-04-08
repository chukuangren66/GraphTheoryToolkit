import exchange

def read_graph_from_file(file_name):
    with open(file_name, 'r') as file:
        num_graphs = int(file.readline())  # 读取图的数量
        graphs = []
        line = ""

        for _ in range(num_graphs):
            if line == "":
                n = int(file.readline())  # 读取当前图的节点数
            else:n = int(line)
            edges = []

            # 读取每个图的边
            while True:
                line = file.readline().strip()
                print(line)
                if len(line.split()) <= 1:  # 如果是单正整数，表示此图的边读取完毕
                    break
                u, v = map(int, line.split())  # 读取边
                edges.append((u, v))

            # 将边和节点数传入转换函数
            g, mark = exchange.convert_graph_to_g_mark(edges, n)
            print(g)
            print(mark)
            graphs.append((g, mark))  # 保存每个图的 g 和 mark

        return graphs
