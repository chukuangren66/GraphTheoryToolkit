import random
import argparse
import os


def generate_wheel_graph(n, m):
    # 检查 n 是否满足轮图的定义要求
    if n < 3:
        print("输入的 n 不满足轮图的定义要求（n 需大于等于 3）。")
        return False

    # 创建结果文件夹
    result_dir = "wheel-result"
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)

    # 以写入模式打开文件
    filename = os.path.join(result_dir, f"wheel_graph_{n}_{m}.in")
    with open(filename, 'w') as file:
        file.write(f"{m}\n")
        for _ in range(m):
            edges = []

            # 生成外环边（连接外环上的节点）
            for i in range(0, n - 1):
                edges.append((i, (i + 1) % (n - 1)))  # 外环上的节点形成一个圈

            # 生成中心节点与外环节点的边
            center_node = n - 1  # 选择节点 n - 1 作为中心节点
            for i in range(0, n - 1):
                edges.append((center_node, i))

            # 将结果写入文件
            file.write(f"{n}\n")
            for edge in edges:
                file.write(f"{edge[0] + 1} {edge[1] + 1}\n")
    
    print(f"成功生成文件：{filename}")
    return True


def main():
    parser = argparse.ArgumentParser(description='生成轮图')
    parser.add_argument('--n', type=int, default=5, help='轮图的节点数（包括中心节点）')
    parser.add_argument('--m', type=int, default=10, help='要生成的图的数量')
    
    args = parser.parse_args()
    
    # 参数验证
    if args.n < 3:
        print("错误：节点数必须大于等于3")
        return
    if args.m <= 0:
        print("错误：图的数量必须是正数")
        return
    
    try:
        generate_wheel_graph(args.n, args.m)
        print("成功生成轮图")
    except Exception as e:
        print(f"生成图时出错：{str(e)}")


if __name__ == "__main__":
    main()
