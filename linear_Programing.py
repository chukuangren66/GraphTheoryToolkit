import cplex
import csv
import time

# 批处理函数
def solve_ilp_for_graph(n, g, mark):
    print("this")
    # 创建Cplex模型
    prob = cplex.Cplex()
    prob.set_problem_name("Italian Control Problem")
    prob.objective.set_sense(prob.objective.sense.minimize)

    # 添加变量（vx和vy均为二进制变量）
    vx_vars = list(range(n))  # vx变量索引：0,1,2,3
    vy_vars = [i + n for i in range(n)]  # vy变量索引：4,5,6,7
    prob.variables.add(names=[f"vx_{i}" for i in range(n)], types="B" * n)
    prob.variables.add(names=[f"vy_{i}" for i in range(n)], types="B" * n)

    # 设置目标函数：最小化 sum(vx[i] + 2*vy[i])
    objective = [(i, 1.0) for i in vx_vars] + [(i, 2.0) for i in vy_vars]
    prob.objective.set_linear(objective)

    # 添加约束1：每个节点只能选择0、1或2（vx + vy <= 1）
    for i in range(n):
        prob.linear_constraints.add(
            lin_expr=[[[vx_vars[i], vy_vars[i]], [1.0, 1.0]]],
            senses=["L"],
            rhs=[1.0]
        )

    # 添加约束2：意大利控制条件
    for i in range(n):
        print(i)
        # 计算当前节点的邻接节点在g中的索引范围

        start = mark[i] - 1  # 转换为0-based
        end = mark[i + 1] - 2  # mark数组在Python中是0-based
        print(start, end)
        adj_indices = list(range(start, end + 1))

        # 获取邻接节点的Python索引（原题中的节点编号转换为0-based）
        adj_nodes = [g[j] - 1 for j in adj_indices]
        print(adj_nodes)

        # 构建约束表达式
        variables = []
        coefficients = []
        # 添加当前节点的vx和vy
        variables.extend([vx_vars[i], vy_vars[i]])
        coefficients.extend([1.0, 1.0])
        # 添加邻接节点的vx和vy的贡献
        for j in adj_nodes:
            variables.append(vx_vars[j])  # vx[j]的系数为0.5
            coefficients.append(0.5)
            variables.append(vy_vars[j])  # vy[j]的系数为1.0
            coefficients.append(1.0)

        # 添加约束到模型
        prob.linear_constraints.add(
            lin_expr=[[variables, coefficients]],
            senses=["G"],
            rhs=[1.0]
        )

    # 求解并输出结果
    prob.solve()

    # 获取解
    solution_status = prob.solution.get_status_string()
    objective_value = prob.solution.get_objective_value()

    return solution_status, objective_value

# 生成统计表格
def process_multiple_graphs(graphs_data):
    # 统计表头
    result = [["Graph Index","num_of_node", "Solution Status", "Objective Value", "Solving Time"]]

    # 遍历每个图
    for idx, graph_data in enumerate(graphs_data):
        start_time = time.time()
        g = graph_data[0]
        graph_data[1].append(len(g) + 1)
        mark = graph_data[1];
        print(mark)
        n = len(mark) - 1
        print(n)
        solution_status, objective_value = solve_ilp_for_graph(n, g, mark)
        solving_time = time.time() - start_time
        num_of_node = n
        result.append([idx + 1,num_of_node, solution_status, objective_value, solving_time])

    # 输出为 CSV 文件
    with open(f"results_of_hypercube.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(result)

    print("Results have been saved to results.csv")

"""# 定义多个图的数据（n, m, g, mark）
graphs_data = [
    ([2, 3, 1, 4, 1, 4, 2, 3], [1, 3, 5, 7]),  # 图1
([2, 3, 1, 4, 1, 4, 2, 3], [1, 3, 5, 7]),
([2, 3, 1, 4, 1, 4, 2, 3], [1, 3, 5, 7])

]

# 处理多个图并生成统计表
process_multiple_graphs(graphs_data)"""
