#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
案例生成器
基于意图分析和模板生成E2E测试案例和断言
"""

import json
from typing import Dict, List, Any
from pathlib import Path
from dataclasses import dataclass, asdict
from ai_intent_analyzer import IntentAnalysis


@dataclass
class CaseInfo:
    """案例信息"""
    caseId: str
    caseSummary: str
    caseData: Dict[str, Any]
    mockRtn: Dict[str, Any]
    msgTemplate: Dict[str, Any]
    participants: List[str]
    flowSteps: List[str]
    businessType: str


@dataclass
class AssertInfo:
    """断言信息"""
    assertType: str
    assertKey: str
    assertValue: str
    assertRule: str
    createBy: str
    description: str


class CaseGenerator:
    """案例生成器"""

    def __init__(self, templates_dir: str):
        """
        初始化案例生成器

        Args:
            templates_dir: 模板文件目录
        """
        self.templates_dir = Path(templates_dir)
        self.templates = self._load_templates()

    def _load_templates(self) -> Dict[str, Dict]:
        """加载模板文件"""
        templates = {}

        # 遍历模板目录
        for template_file in self.templates_dir.glob("*.md"):
            business_type = template_file.stem
            templates[business_type] = self._parse_template_file(template_file)

        return templates

    def _parse_template_file(self, file_path: Path) -> Dict:
        """解析模板文件"""
        content = file_path.read_text(encoding='utf-8')

        # 提取案例信息部分
        case_info_match = content.split('案例信息 CaseInfo')[1].split('断言信息')[0]
        case_info_json = case_info_match.split('{', 1)[1].rsplit('}', 1)[0]

        # 提取断言信息部分
        assert_info_match = content.split('断言信息')[1]
        assert_info_json = assert_info_match.split('[', 1)[1].rsplit(']', 1)[0]

        return {
            'case_info': json.loads('{' + case_info_json + '}'),
            'assert_info': json.loads('[' + assert_info_json + ']')
        }

    def generate_case(self, case_id: str, intent: IntentAnalysis) -> CaseInfo:
        """
        生成案例信息

        Args:
            case_id: 案例编号
            intent: 意图分析结果

        Returns:
            CaseInfo: 生成的案例信息
        """
        # 选择最匹配的模板
        template = self._select_best_template(intent)

        # 生成案例信息
        case_info = template['case_info'].copy()
        case_info['caseId'] = case_id
        case_info['caseSummary'] = self._generate_case_summary(intent)
        case_info['caseData'] = self._generate_case_data(intent, template)
        case_info['mockRtn'] = self._generate_mock_response(intent, template)
        case_info['msgTemplate'] = self._generate_message_template(intent, template)
        case_info['participants'] = intent.participants
        case_info['flowSteps'] = intent.flow_steps
        case_info['businessType'] = intent.business_type

        return CaseInfo(**case_info)

    def generate_assertions(self, intent: IntentAnalysis, template: Dict) -> List[AssertInfo]:
        """
        生成断言信息

        Args:
            intent: 意图分析结果
            template: 匹配的模板

        Returns:
            List[AssertInfo]: 断言信息列表
        """
        assertions = []

        # 基于模板生成基础断言
        for assert_template in template['assert_info']:
            assertion = AssertInfo(
                assertType=assert_template['assertType'],
                assertKey=assert_template['assertKey'],
                assertValue=self._replace_parameters(assert_template['assertValue'], intent.key_parameters),
                assertRule=assert_template['assertRule'],
                createBy='AI',
                description=self._generate_assertion_description(assert_template, intent)
            )
            assertions.append(assertion)

        # 基于意图添加动态断言
        dynamic_assertions = self._generate_dynamic_assertions(intent)
        assertions.extend(dynamic_assertions)

        return assertions

    def _select_best_template(self, intent: IntentAnalysis) -> Dict:
        """选择最匹配的模板"""
        best_match = None
        best_score = 0

        for template_name, template in self.templates.items():
            score = self._calculate_match_score(intent, template)
            if score > best_score:
                best_score = score
                best_match = template

        return best_match if best_match else list(self.templates.values())[0]

    def _calculate_match_score(self, intent: IntentAnalysis, template: Dict) -> float:
        """计算匹配分数"""
        score = 0.0

        # 业务类型匹配
        case_info = template.get('case_info', {})
        if intent.business_type in case_info.get('businessType', ''):
            score += 0.5

        # 参与者匹配
        template_participants = case_info.get('participants', [])
        for participant in intent.participants:
            if participant in template_participants:
                score += 0.1

        # 流程步骤匹配
        template_steps = case_info.get('flowSteps', [])
        for step in intent.flow_steps:
            if step in template_steps:
                score += 0.1

        return min(score, 1.0)

    def _generate_case_summary(self, intent: IntentAnalysis) -> str:
        """生成案例摘要"""
        participants = "、".join(intent.participants)
        steps = " → ".join(intent.flow_steps)
        return f"{participants}执行{intent.business_type}业务，流程：{steps}"

    def _generate_case_data(self, intent: IntentAnalysis, template: Dict) -> Dict[str, Any]:
        """生成案例数据"""
        case_data = template['case_info'].get('caseData', {}).copy()

        # 替换参数
        for key, value in case_data.items():
            if isinstance(value, str):
                case_data[key] = self._replace_parameters(value, intent.key_parameters)

        return case_data

    def _generate_mock_response(self, intent: IntentAnalysis, template: Dict) -> Dict[str, Any]:
        """生成模拟响应"""
        mock_rtn = template['case_info'].get('mockRtn', {}).copy()

        # 替换参数
        for key, value in mock_rtn.items():
            if isinstance(value, str):
                mock_rtn[key] = self._replace_parameters(value, intent.key_parameters)

        return mock_rtn

    def _generate_message_template(self, intent: IntentAnalysis, template: Dict) -> Dict[str, Any]:
        """生成消息模板"""
        msg_template = template['case_info'].get('msgTemplate', {}).copy()

        # 替换参数
        for key, value in msg_template.items():
            if isinstance(value, str):
                msg_template[key] = self._replace_parameters(value, intent.key_parameters)

        return msg_template

    def _replace_parameters(self, text: str, parameters: Dict[str, str]) -> str:
        """替换文本中的参数"""
        result = text
        for param_name, param_value in parameters.items():
            result = result.replace(f"${{{param_name}}}", param_value)

        return result

    def _generate_assertion_description(self, assert_template: Dict, intent: IntentAnalysis) -> str:
        """生成断言描述"""
        return f"验证{intent.business_type}业务中{assert_template['assertKey']}的值"

    def _generate_dynamic_assertions(self, intent: IntentAnalysis) -> List[AssertInfo]:
        """生成动态断言"""
        assertions = []

        # 基于成功标准生成断言
        for criteria in intent.success_criteria:
            if '状态' in criteria:
                assertions.append(AssertInfo(
                    assertType='MSG',
                    assertKey='status',
                    assertValue='00',
                    assertRule='REQUIRED',
                    createBy='AI',
                    description=f'验证业务状态：{criteria}'
                ))

        return assertions


if __name__ == '__main__':
    # 测试示例
    print("案例生成器已就绪")
    print("使用方法:")
    print("1. 配置模板文件目录")
    print("2. 提供意图分析结果")
    print("3. 调用generate_case()生成案例")
    print("4. 调用generate_assertions()生成断言")