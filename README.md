# GraphControlNumberSolver

一个用于生成各种图结构并计算其控制数的图形化工具。

## 项目简介

GraphControlNumberSolver 是一个集成了多种图生成算法和控制数计算功能的图形化工具。它能够生成多种经典图结构，并通过CPLEX求解器计算图的最小控制数。

## 主要功能

- **多种图生成器**：
  - 随机图生成器
  - K正则图生成器
  - 轮图生成器
  - 星图生成器
  - 彼得森图生成器
  - 超立方体图生成器
  - 自定义图生成器

- **图形化界面**：
  - 直观的参数设置
  - 实时图形可视化
  - 控制数计算结果展示

- **控制数计算**：
  - 基于CPLEX的整数线性规划求解
  - 支持多种图结构的控制数计算
  - 结果验证和展示

## 系统要求

- Python 3.6+
- CPLEX 22.1+
- 以下Python包：
  - tkinter
  - networkx
  - matplotlib
  - docplex

## 安装说明

1. 克隆仓库：
```bash
git clone https://github.com/yourusername/GraphControlNumberSolver.git
cd GraphControlNumberSolver
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 确保已安装CPLEX并正确配置环境变量

## 使用方法

1. 运行主程序：
```bash
python interface/graph_generator_gui.py
```

2. 在图形界面中：
   - 选择要生成的图类型
   - 设置相应参数
   - 点击生成按钮
   - 查看生成的图和计算的控制数

## 项目结构

```
GraphControlNumberSolver/
├── interface/
│   └── graph_generator_gui.py    # 图形用户界面
├── build_*.py                    # 各种图生成器
├── linear_Programing.py          # 控制数计算核心
├── exchange.py                   # 图数据转换工具
└── read_graph_from_file.py       # 文件读取工具
```

## 示例

### 生成随机图
1. 选择"随机图"选项
2. 设置节点数和边生成概率
3. 点击生成按钮
4. 查看生成的图和计算的控制数

### 生成K正则图
1. 选择"K-图"选项
2. 设置节点数和节点度数
3. 点击生成按钮
4. 查看生成的图和计算的控制数

## 贡献指南

欢迎提交Issue和Pull Request来改进项目。在提交代码前，请确保：

1. 代码符合PEP 8规范
2. 添加必要的注释和文档
3. 通过所有测试

## 许可证

本项目采用MIT许可证。详见LICENSE文件。

## 联系方式

如有任何问题或建议，请通过以下方式联系：

- 提交Issue
- 发送邮件至：[your-email@example.com]

## 致谢

感谢所有为本项目做出贡献的开发者。 