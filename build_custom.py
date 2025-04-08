import argparse
import os
import sys

def generate_custom_graph(n, edges):
    """
    生成一个自定义图
    n: 节点数
    edges: 边的列表，每个元素是一个元组(u,v)表示一条边
    """
    # 创建结果目录
    result_dir = "custom-result"
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)
    
    # 生成文件名
    filename = os.path.join(result_dir, f"custom_graph_n{n}.in")
    
    with open(filename, 'w') as f:
        # 写入图的数量（1）
        f.write("1\n")
        
        # 写入节点数
        f.write(f"{n}\n")
        
        # 写入边
        for u, v in edges:
            f.write(f"{u} {v}\n")
    
    print(f"已生成自定义图文件：{filename}")
    return True

def main():
    parser = argparse.ArgumentParser(description='生成自定义图')
    parser.add_argument('--n', type=int, required=True, help='节点数')
    parser.add_argument('--edges', type=str, required=True, help='边的列表，格式为"u1,v1;u2,v2;..."')
    
    args = parser.parse_args()
    
    # 验证参数
    if args.n < 1:
        print("错误：节点数必须大于0", file=sys.stderr)
        sys.exit(1)
    
    # 解析边的列表
    try:
        edges = []
        edge_pairs = args.edges.strip('"').split(';')  # 移除可能存在的引号
        for pair in edge_pairs:
            if pair.strip():  # 忽略空字符串
                # 移除所有空格并分割
                u, v = map(int, pair.replace(' ', '').split(','))
                if u < 1 or v < 1 or u > args.n or v > args.n:
                    print(f"错误：边的节点编号必须在1到{args.n}之间", file=sys.stderr)
                    sys.exit(1)
                edges.append((u, v))
        
        if not edges:
            print("错误：至少需要一条边", file=sys.stderr)
            sys.exit(1)
            
        if not generate_custom_graph(args.n, edges):
            print("错误：生成图失败", file=sys.stderr)
            sys.exit(1)
            
    except ValueError as e:
        print(f"错误：边的格式不正确，应为'u1,v1;u2,v2;...'", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main() 