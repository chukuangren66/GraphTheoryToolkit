import argparse
import os

def generate_petersen_graph(n, k):
    """
    生成一个确定的彼得森图
    n: 外环节点数
    k: 内部连接参数
    """
    # 创建结果目录
    result_dir = "peterson-result"
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)
    
    # 计算总节点数
    total_nodes = 2 * n
    
    # 生成文件名
    filename = os.path.join(result_dir, f"petersen_{total_nodes}_{k}.in")
    
    with open(filename, 'w') as f:
        # 写入图的数量（1）
        f.write("1\n")
        
        # 写入节点数
        f.write(f"{total_nodes}\n")
        
        # 生成外环边
        for i in range(n):
            f.write(f"{i+1} {(i+1)%n+1}\n")
        
        # 生成内环边
        for i in range(n):
            f.write(f"{i+1} {n+((i+k)%n)+1}\n")
        
        # 生成内环连接边
        for i in range(n):
            f.write(f"{n+i+1} {n+((i+1)%n)+1}\n")
    
    print(f"已生成彼得森图文件：{filename}")

def main():
    parser = argparse.ArgumentParser(description='生成彼得森图')
    parser.add_argument('--n', type=int, required=True, help='外环节点数')
    parser.add_argument('--k', type=int, required=True, help='内部连接参数')
    
    args = parser.parse_args()
    
    # 验证参数
    if args.n < 3:
        print("错误：外环节点数必须大于等于3")
        return
    
    if args.k < 1 or args.k >= args.n:
        print("错误：内部连接参数k必须满足1 ≤ k < n")
        return
    
    generate_petersen_graph(args.n, args.k)

if __name__ == "__main__":
    main()