import random
import argparse
import os


def generate_star_graph(n, m):
    # 创建结果文件夹
    result_dir = "star-result"
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)
    
    # 以写入模式打开文件
    filename = os.path.join(result_dir, f"star_{n}_{m}.in")
    with open(filename, 'w') as f:
        # 先写入图的总数
        f.write(f"{m}\n")
        
        # 生成m个星图
        for _ in range(m):
            # 写入节点数
            f.write(f"{n}\n")
            # 写入边（中心节点为1，其他节点从2到n）
            for i in range(2, n + 1):
                f.write(f"1 {i}\n")
    
    print(f"成功生成文件：{filename}")
    return True


def main():
    parser = argparse.ArgumentParser(description='生成星图')
    parser.add_argument('--n', type=int, default=5, help='节点数')
    parser.add_argument('--m', type=int, default=10, help='要生成的图的数量')
    
    args = parser.parse_args()
    
    # 参数验证
    if args.n < 2:
        print("错误：节点数必须大于1")
        return
    if args.m <= 0:
        print("错误：图的数量必须是正数")
        return
    
    try:
        generate_star_graph(args.n, args.m)
        print("成功生成星图")
    except Exception as e:
        print(f"生成图时出错：{str(e)}")


if __name__ == "__main__":
    main()
