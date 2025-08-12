#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import json
import logging

from x2case.func import XmindZenParser
from x2case.jira import xmind_to_jira_csv_file

logging.basicConfig(level=logging.INFO)


def main():
    xmind_file = 'docs/jira_demo.xmind'
    print('Start to convert XMind file: %s' % xmind_file)

    # 1、testcases import file
    # (1) jira
    csv_file = xmind_to_jira_csv_file(xmind_file)
    print(f'Convert XMind file to zentao csv file successfully: {xmind_file}')

    # 2、 testcases json file
    parser = XmindZenParser(xmind_file)
    # (1) testsuite
    testsuite_json_file = parser.xmind_2_suite_json_file()
    print('Convert XMind file to testsuite json file successfully: %s' % testsuite_json_file)
    # (2) testcase
    testcase_json_file = parser.xmind_2_case_json_file()
    print('Convert XMind file to testcase json file successfully: %s' % testcase_json_file)

    # 3、test dict/json data
    # (1) testsuite

    test_suite = parser.get_xmind_testsuite_list()
    print('Convert XMind to test suits dict data:\n%s' %
          json.dumps(test_suite, indent=2, separators=(',', ': '), ensure_ascii=False))
    # (2) testcase
    testcases = parser.get_xmind_testcase_list()
    print('Convert Xmind to testcases dict data:\n%s' %
          json.dumps(testcases, indent=4, separators=(',', ': '), ensure_ascii=False))

    print('Finished conversion, Congratulations!')


if __name__ == '__main__':
    main()
