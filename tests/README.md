# Tests 目录

本目录包含 X2Case 项目的所有测试和调试工具。

## 目录结构

```
tests/
├── __init__.py              # 测试模块初始化
├── README.md               # 本文件
├── test_runner.py          # 测试运行器（统一管理）
├── test_csv_conversion.py  # CSV转换功能测试
├── test_func_fix.py        # func.py修复验证测试
└── debug_tools.py          # 调试工具集
```

## 测试文件说明

### 1. test_csv_conversion.py
**CSV转换功能完整测试套件**
- 测试CSV文件生成功能
- 验证字段映射正确性
- 测试边界情况处理
- 验证JIRA格式兼容性

### 2. test_func_fix.py
**func.py修复后功能验证**
- 验证None值处理修复
- 测试数据结构完整性
- 验证转换功能兼容性
- 确保修复后功能正常

### 3. debug_tools.py
**项目调试工具集**
- CSV字段映射调试
- 数据结构调试
- 优先级问题调试
- samples.py兼容性检查

### 4. test_runner.py
**统一测试运行器**
- 管理所有测试的执行
- 生成测试报告
- 支持单独运行指定测试
- 提供调试工具运行

## 使用方法

### 运行所有测试
```bash
cd /Users/zeno/ai/XMind2TestCase/x2case
python tests/test_runner.py
```

### 只运行测试（不包括调试工具）
```bash
python tests/test_runner.py --tests-only
```

### 只运行调试工具
```bash
python tests/test_runner.py --debug-only
```

### 运行指定测试
```bash
python tests/test_runner.py --test test_csv_conversion.py
```

### 直接运行单个测试文件
```bash
python tests/test_csv_conversion.py
python tests/test_func_fix.py
python tests/debug_tools.py
```

## 测试覆盖的功能

### ✅ 核心功能测试
- [x] XMind文件解析
- [x] CSV文件生成
- [x] 字段映射验证
- [x] 数据结构转换
- [x] 优先级和类型映射

### ✅ 修复验证
- [x] None值迭代错误修复
- [x] 边界情况处理
- [x] 向后兼容性保证
- [x] 数据完整性验证

### ✅ 调试支持
- [x] 字段映射调试
- [x] 数据结构分析
- [x] 优先级问题诊断
- [x] 兼容性检查

## 测试数据

测试使用模拟数据，包括：
- 多种优先级的测试用例（High/Medium/Low）
- 不同类型的测试（Manual/Automation）
- 多模块测试套件（登录、商品管理等）
- 边界情况数据（空值、超出范围值）

## 预期结果

所有测试应该通过，表明：
1. func.py中的None值迭代错误已修复
2. CSV转换功能完全正常
3. 所有字段映射正确
4. 数据结构完整性得到保证
5. 项目功能健壮稳定

## 故障排除

如果测试失败，请：
1. 查看详细的错误输出
2. 运行调试工具进行诊断
3. 检查相关代码修改
4. 验证依赖库版本

## 维护说明

当添加新功能或修复bug时，请：
1. 相应地更新或添加测试用例
2. 确保所有现有测试仍能通过
3. 更新本README文档
4. 考虑添加新的调试工具