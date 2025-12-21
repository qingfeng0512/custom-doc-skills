#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI意图分析器
使用AI模型分析业务描述，提取意图和关键参数
"""

import json
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
import openai
from config_manager import config


@dataclass
class IntentAnalysis:
    """意图分析结果"""
    business_type: str
    business_subtype: str
    participants: List[str]
    flow_steps: List[str]
    key_parameters: Dict[str, str]
    success_criteria: List[str]
    risk_points: List[str]


class AIIntentAnalyzer:
    """AI意图分析器"""

    def __init__(self, api_key: str, api_base: str, model: str = "MiniMaxAI/MiniMax-M2", **kwargs):
        """
        初始化AI分析器

        Args:
            api_key: API密钥
            api_base: API基础URL
            model: 使用的模型名称
            **kwargs: 额外的参数（如temperature, max_tokens等）
        """
        self.client = openai.OpenAI(
            api_key=api_key,
            base_url=api_base
        )
        self.model = model
        # 保存额外参数
        self.extra_params = kwargs

    def analyze_business_intent(self, case_id: str, description: str) -> IntentAnalysis:
        """
        分析业务意图

        Args:
            case_id: 案例编号
            description: 业务描述

        Returns:
            IntentAnalysis: 意图分析结果
        """
        prompt = self._build_analysis_prompt(case_id, description)

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "你是一个专业的业务分析师，专门分析E2E测试意图和案例关键测试点。"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1,
            response_format={"type": "json_object"}
        )

        result = json.loads(response.choices[0].message.content)
        return IntentAnalysis(**result)

    def _build_analysis_prompt(self, case_id: str, description: str) -> str:
        """构建分析提示"""
        return f"""
请分析以下E2E测试业务案例，提取关键信息：

案例编号: {case_id}
业务描述: {description}

请按照以下JSON格式返回分析结果：

{{
    "business_type": "主业务类型（如：支付、转账、查询等）",
    "business_subtype": "业务子类型（如：快捷支付、代扣等）",
    "participants": ["参与者列表，如：支付机构、银行、用户等"],
    "flow_steps": ["业务流程步骤，如：发起、受理、处理、返回等"],
    "key_parameters": {{
        "参数名": "参数值"
    }},
    "success_criteria": ["成功判断标准"],
    "risk_points": ["风险点或关注点"]
}}

请确保返回的是有效的JSON格式。
"""


if __name__ == '__main__':
    # 从配置文件加载API配置
    API_CONFIG = config.get_ai_config()

    # 测试示例
    analyzer = AIIntentAnalyzer(**API_CONFIG)

    test_case_id = "epcc_201_0110_Z_AI_001"
    test_description = "支付机构发起快捷支付，网联平台受理后转发给银行处理，银行返回账户被冻结支付失败，平台接收后响应支付机构业务处理失败。"

    try:
        result = analyzer.analyze_business_intent(test_case_id, test_description)
        print("分析结果:")
        print("-" * 20)
        print(f"案例编号: {test_case_id}")
        print(f"业务类型: {result.business_type}")
        print(f"业务子类型: {result.business_subtype}")
        print(f"参与者: {result.participants}")
        print(f"流程步骤: {result.flow_steps}")
        print(f"关键参数: {result.key_parameters}")
        print(f"成功标准: {result.success_criteria}")
        print(f"风险点: {result.risk_points}")
    except Exception as e:
        print(f"分析失败: {e}")
        print("请确保API配置正确且网络连接正常")