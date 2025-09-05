#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
测试使用示例
展示如何使用tests目录中的工具
"""


def demonstrate_test_usage():
    """演示测试使用方法"""
    print("=" * 60)
    print("X2Case 测试目录使用示例")
    print("=" * 60)
    
    print("\\n📁 tests/ 目录包含以下文件:")
    files = [
        ("test_runner.py", "统一测试运行器"),
        ("test_csv_conversion.py", "CSV转换功能测试"),
        ("test_func_fix.py", "func.py修复验证"),
        ("debug_tools.py", "调试工具集"),
        ("README.md", "详细使用说明")
    ]
    
    for filename, description in files:
        print(f"  • {filename:<25} - {description}")
    
    print("\\n🚀 运行方式:")
    print("1. 运行所有测试:")
    print("   python tests/test_runner.py")
    
    print("\\n2. 只运行测试（不包括调试工具）:")
    print("   python tests/test_runner.py --tests-only")
    
    print("\\n3. 只运行调试工具:")
    print("   python tests/test_runner.py --debug-only")
    
    print("\\n4. 运行指定测试:")
    print("   python tests/test_runner.py --test test_csv_conversion.py")
    
    print("\\n5. 直接运行单个文件:")
    print("   python tests/test_csv_conversion.py")
    print("   python tests/debug_tools.py")
    
    print("\\n✅ 预期结果:")
    print("  • 所有测试应该通过 (PASS)")
    print("  • 验证func.py的None值修复成功")
    print("  • 确认CSV转换功能正常")
    print("  • 字段映射和数据完整性验证通过")
    
    print("\\n📋 测试覆盖范围:")
    coverage_areas = [
        "XMind文件解析功能",
        "CSV文件生成和格式验证", 
        "字段映射正确性",
        "优先级和类型转换",
        "None值处理修复",
        "边界情况处理",
        "数据结构完整性",
        "向后兼容性"
    ]
    
    for area in coverage_areas:
        print(f"  ✓ {area}")
    
    print("\\n🔧 故障排除:")
    print("  • 如果测试失败，查看详细错误输出")
    print("  • 运行调试工具进行问题诊断")
    print("  • 检查Python环境和依赖库")
    print("  • 参考tests/README.md获取更多信息")
    
    print("\\n" + "=" * 60)


if __name__ == '__main__':
    demonstrate_test_usage()