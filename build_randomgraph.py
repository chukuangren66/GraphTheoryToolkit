import random
import argparse
import os


def generate_random_graph(n, p=0.5):
    """
    生成一个随机图
    n: 节点数
    p: 每条边存在的概率（默认0.5）
    """
    # 创建结果目录
    result_dir = "random-result"
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)
    
    # 生成文件名
    filename = os.path.join(result_dir, f"random_graph_n{n}.in")
    
    with open(filename, 'w') as f:
        # 写入图的数量（1）
        f.write("1\n")
        
        # 写入节点数
        f.write(f"{n}\n")
        
        # 生成随机边
        edges = []
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                # 以概率p添加边
                if random.random() < p:
                    edges.append((i, j))
        
        # 写入所有边
        for edge in edges:
            f.write(f"{edge[0]} {edge[1]}\n")
    
    print(f"已生成随机图文件：{filename}")
    return True


def main():
    parser = argparse.ArgumentParser(description='生成随机图')
    parser.add_argument('--n', type=int, required=True, help='节点数')
    parser.add_argument('--p', type=float, default=0.5, help='边的生成概率（默认0.5）')
    
    args = parser.parse_args()
    
    # 验证参数
    if args.n < 1:
        print("错误：节点数必须大于0")
        return
    
    if args.p < 0 or args.p > 1:
        print("错误：概率p必须在0到1之间")
        return
    
    generate_random_graph(args.n, args.p)


if __name__ == "__main__":
    main()
