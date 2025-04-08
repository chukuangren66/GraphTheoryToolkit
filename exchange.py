def convert_graph_to_g_mark(edges, n):
    print("***")
    print(n)
    # g 数组：保存每个节点的相邻节点
    g = []

    # mark 数组：保存每个节点相邻节点在 g 数组中的起始位置
    mark = [0] * (n)  # mark[0] 和 mark[n] 用作辅助

    # 存储每个节点的相邻节点列表
    adjacency_list = {i: [] for i in range(1, n + 1)}

    print(adjacency_list)
    # 构建邻接表
    for edge in edges:
        print(edge)
        u, v = edge
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)

    # 填充 g 和 mark
    idx = 0  # 用于遍历 g 数组
    for i in range(1, n + 1):
        mark[i - 1] = idx + 1  # mark[i] 表示节点 i 在 g 中的起始位置
        g.extend(adjacency_list[i])  # 将节点 i 的所有相邻节点加入 g
        idx += len(adjacency_list[i])  # 更新 idx



    return g, mark

