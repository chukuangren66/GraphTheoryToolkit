import argparse
import os


def generate_hypercube(n):
    # 验证输入是否为非负整数
    if n < 0:
        print("输入的维度必须是非负整数。")
        return False

    # 创建结果文件夹
    result_dir = "q-result"
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)

    # 计算节点数，即2的n次方
    m = 1 << n
    edges = []
    # 遍历所有节点
    for i in range(m):
        # 遍历每个节点的每一位
        for k in range(n):
            # 翻转第k位得到相邻节点
            j = i ^ (1 << k)
            # 确保每条边只记录一次
            if j > i:
                edges.append((i, j))

    # 构建文件名
    filename = os.path.join(result_dir, f"Q{n}.in")
    # 打开文件以写入模式
    with open(filename, 'w') as file:
        # 写入图的数量（超立方体图只生成一个）
        file.write("1\n")
        # 写入节点数
        file.write(str(m) + '\n')
        # 写入每条边的两个端点
        for a, b in edges:
            file.write(f"{a + 1} {b + 1}\n")

    print(f"成功生成文件：{filename}")
    return True


def main():
    parser = argparse.ArgumentParser(description='生成超立方体图')
    parser.add_argument('--n', type=int, default=3, help='超立方体图的维度')
    
    args = parser.parse_args()
    
    # 参数验证
    if args.n < 0:
        print("错误：维度必须是非负整数")
        return
    
    try:
        generate_hypercube(args.n)
        print("成功生成超立方体图")
    except Exception as e:
        print(f"生成图时出错：{str(e)}")


if __name__ == "__main__":
    main()