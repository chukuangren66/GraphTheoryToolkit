import argparse
import os

def generate_k_regular_graph(n, k):
    """
    生成一个确定的k正则图
    n: 节点数
    k: 节点度数（每个顶点恰好与k个其他顶点相连）
    """
    # 检查参数是否满足k正则图的条件
    if n <= k:
        print("错误：节点数必须大于节点度数")
        return False
    
    if n * k % 2 != 0:
        print("错误：n*k必须是偶数")
        return False
    
    # 创建结果目录
    result_dir = "k-result"
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)
    
    # 生成文件名
    filename = os.path.join(result_dir, f"k_regular_n{n}_k{k}.in")
    
    with open(filename, 'w') as f:
        # 写入图的数量（1）
        f.write("1\n")
        
        # 写入节点数
        f.write(f"{n}\n")
        
        # 生成边
        edges = set()
        for i in range(n):
            # 连接到后面的k/2个节点
            for j in range(1, k//2 + 1):
                target = (i + j) % n
                edges.add((min(i+1, target+1), max(i+1, target+1)))
            
            # 连接到前面的k/2个节点
            for j in range(1, k//2 + 1):
                target = (i - j) % n
                edges.add((min(i+1, target+1), max(i+1, target+1)))
            
            # 如果k是奇数，额外连接到对面的节点
            if k % 2 == 1:
                target = (i + n//2) % n
                edges.add((min(i+1, target+1), max(i+1, target+1)))
        
        # 写入所有边
        for edge in edges:
            f.write(f"{edge[0]} {edge[1]}\n")
    
    print(f"已生成K正则图文件：{filename}")
    return True

def main():
    parser = argparse.ArgumentParser(description='生成K正则图')
    parser.add_argument('--n', type=int, required=True, help='节点数')
    parser.add_argument('--k', type=int, required=True, help='节点度数')
    
    args = parser.parse_args()
    
    # 验证参数
    if args.n <= args.k:
        print("错误：节点数必须大于节点度数")
        return
    
    if args.n * args.k % 2 != 0:
        print("错误：n*k必须是偶数")
        return
    
    generate_k_regular_graph(args.n, args.k)

if __name__ == "__main__":
    main()