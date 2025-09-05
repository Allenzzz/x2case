#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
项目调试工具集
包含各种调试和诊断功能
"""
import json
import logging
from x2case import const
from x2case.jira import gen_case_row, gen_case_priority, gen_case_type
from x2case.com import TestSuite, TestCase, TestStep

logging.basicConfig(level=logging.DEBUG)


class ProjectDebugger:
    """项目调试器"""
    
    def debug_field_mapping(self):
        """调试CSV字段映射"""
        print("=== 调试CSV字段映射 ===")
        
        # 显示JIRA表头
        print("\\nJIRA表头字段:")
        for i, field in enumerate(const.JIRA_HEAD):
            print(f"  {i:2d}: {field}")
        
        # 测试优先级和类型函数
        print(f"\\n优先级映射测试:")
        for i in [1, 2, 3, 999]:
            priority = gen_case_priority(i)
            print(f"  importance {i} -> priority '{priority}'")
        
        print(f"\\n测试类型映射测试:")
        for i in [1, 2, 999]:
            test_type = gen_case_type(i)
            print(f"  execution_type {i} -> test_type '{test_type}'")
        
        # 创建测试数据
        test_case = {
            'case_id': 'DEBUG-TC-001',
            'name': '调试测试用例',
            'preconditions': '调试前置条件',
            'steps': [
                {
                    'step_number': 1,
                    'actions': '执行调试步骤1',
                    'expected_results': '调试预期结果1'
                }
            ],
            'importance': 1,  # High
            'execution_type': 2,  # Automation
            'product': '调试产品',
            'suite': '调试套件',
            'epic_link': 'DEBUG-EPIC-001'
        }
        
        print(f"\\n生成CSV行测试:")
        row = gen_case_row(test_case)
        
        print(f"生成的行字段数: {len(row)}")
        print(f"JIRA表头字段数: {len(const.JIRA_HEAD)}")
        
        if len(row) == len(const.JIRA_HEAD):
            print("✓ 字段数量匹配")
        else:
            print("✗ 字段数量不匹配")
        
        # 显示关键字段的值
        key_mappings = {
            'Test Case Identifier*': 0,
            'Summary*': 2,
            'Action*': 3,
            'Expected Result': 5,
            'Test Type': 7,
            'Applications': 8,
            'Priority': 11,
            'Labels': 14,
            'Pre-Condition': 22,
            'Epic Link': 27
        }
        
        print(f"\\n关键字段值检查:")
        for field_name, pos in key_mappings.items():
            if pos < len(row):
                value = row[pos]
                print(f"  {field_name} (位置{pos}): '{value}'")
            else:
                print(f"  {field_name} (位置{pos}): 超出范围")
    
    def debug_data_structure(self):
        """调试数据结构"""
        print("\\n=== 调试数据结构 ===")
        
        # 创建测试数据
        step = TestStep()
        step.step_number = 1
        step.actions = "调试动作"
        step.expected_results = "调试预期"
        
        testcase = TestCase()
        testcase.case_id = "DEBUG-TC-001"
        testcase.name = "调试用例"
        testcase.steps = [step]
        testcase.importance = 1
        testcase.execution_type = 1
        
        testsuite = TestSuite()
        testsuite.name = "调试套件"
        testsuite.testcase_list = [testcase]
        
        # 检查属性
        print("\\n测试套件属性:")
        for attr in dir(testsuite):
            if not attr.startswith('_'):
                value = getattr(testsuite, attr)
                if not callable(value):
                    print(f"  {attr}: {type(value).__name__} = {value}")
        
        # 检查sub_suites
        print(f"\\nsub_suites检查:")
        if hasattr(testsuite, 'sub_suites'):
            print(f"  sub_suites存在: {testsuite.sub_suites}")
        else:
            print(f"  sub_suites不存在")
        
        # 转换测试
        print(f"\\n转换测试:")
        try:
            suite_dict = testsuite.to_dict()
            print(f"  套件转换成功: {len(suite_dict)} 个字段")
            
            case_dict = testcase.to_dict()
            print(f"  用例转换成功: {len(case_dict)} 个字段")
            
            step_dict = step.to_dict()
            print(f"  步骤转换成功: {len(step_dict)} 个字段")
            
        except Exception as e:
            print(f"  转换失败: {e}")
    
    def debug_priority_issue(self):
        """调试优先级问题"""
        print("\\n=== 调试优先级问题 ===")
        
        # 创建测试用例
        testcase = TestCase()
        testcase.case_id = "PRIORITY-DEBUG"
        testcase.name = "优先级调试用例"
        testcase.summary = "测试优先级映射"
        testcase.preconditions = ""
        testcase.importance = 999  # 超出范围的值
        testcase.execution_type = 999  # 超出范围的值
        
        # 空步骤
        empty_step = TestStep()
        empty_step.step_number = 1
        empty_step.actions = ""
        empty_step.expected_results = ""
        testcase.steps = [empty_step]
        
        # 转换为字典
        case_data = testcase.to_dict()
        case_data['product'] = "调试产品"
        case_data['suite'] = "调试套件"
        case_data['epic_link'] = ""
        
        print(f"测试用例字典数据:")
        print(f"  importance: {case_data.get('importance', 'N/A')} (类型: {type(case_data.get('importance'))})")
        print(f"  execution_type: {case_data.get('execution_type', 'N/A')} (类型: {type(case_data.get('execution_type'))})")
        
        # 测试优先级生成函数
        importance_value = case_data.get('importance')
        priority = gen_case_priority(importance_value)
        print(f"  gen_case_priority({importance_value}) = '{priority}'")
        
        # 生成CSV行
        row = gen_case_row(case_data)
        priority_in_row = row[11]  # Priority在位置11
        print(f"  CSV行中的优先级 (位置11): '{priority_in_row}'")
        
        # 测试正常情况
        print(f"\\n正常情况测试:")
        for test_importance in [1, 2, 3]:
            case_data['importance'] = test_importance
            priority_normal = gen_case_priority(case_data['importance'])
            print(f"  gen_case_priority({test_importance}) = '{priority_normal}'")
            
            row_normal = gen_case_row(case_data)
            priority_normal_in_row = row_normal[11]
            print(f"  CSV行中的优先级: '{priority_normal_in_row}'")
    
    def debug_samples_compatibility(self):
        """调试samples.py兼容性"""
        print("\\n=== 调试samples.py兼容性 ===")
        
        # 检查samples.py中使用的功能
        print("检查samples.py中使用的主要功能:")
        
        try:
            from x2case.func import XmindZenParser
            print("  ✓ XmindZenParser 导入成功")
            
            from x2case.jira import xmind_to_jira_csv_file
            print("  ✓ xmind_to_jira_csv_file 导入成功")
            
            # 模拟创建parser
            fake_xmind_file = 'test.xmind'
            parser = XmindZenParser(fake_xmind_file)
            print("  ✓ XmindZenParser 实例化成功")
            
            # 检查方法是否存在
            methods_to_check = [
                'get_suite_json',
                'get_xmind_testsuite_list', 
                'get_xmind_testcase_list',
                'xmind_2_suite_json_file',
                'xmind_2_case_json_file'
            ]
            
            for method_name in methods_to_check:
                if hasattr(parser, method_name):
                    print(f"  ✓ 方法 {method_name} 存在")
                else:
                    print(f"  ✗ 方法 {method_name} 不存在")
            
        except Exception as e:
            print(f"  ✗ 导入或实例化失败: {e}")
    
    def run_all_debug(self):
        """运行所有调试功能"""
        print("=" * 60)
        print("项目调试工具集")
        print("=" * 60)
        
        self.debug_field_mapping()
        self.debug_data_structure()
        self.debug_priority_issue()
        self.debug_samples_compatibility()
        
        print("\\n" + "=" * 60)
        print("调试完成")
        print("=" * 60)


def main():
    """主函数"""
    debugger = ProjectDebugger()
    debugger.run_all_debug()


if __name__ == '__main__':
    main()