#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
E2E测试案例生成器主程序
整合所有功能模块，提供完整的E2E测试案例生成流程
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Any
from dataclasses import asdict

from ai_intent_analyzer import AIIntentAnalyzer
from case_generator import CaseGenerator
from mcp_integration import E2ETestOrchestrator, MCPIntegration
from config_manager import config


class E2EGenerator:
    """E2E测试案例生成器主类"""

    def __init__(self, templates_dir: str = None):
        """
        初始化E2E生成器

        Args:
            templates_dir: 模板文件目录，如果为None则从配置文件读取
        """
        # 从配置文件加载配置
        self.ai_config = config.get_ai_config()
        self.mcp_config = config.get_mcp_config()
        self.template_config = config.get_template_config()
        self.output_config = config.get_output_config()

        # 使用配置文件中的模板目录或传入的参数
        self.templates_dir = Path(templates_dir or self.template_config['templates_dir'])

        # 初始化组件
        self.analyzer = AIIntentAnalyzer(**self.ai_config)
        self.generator = CaseGenerator(str(self.templates_dir))
        self.mcp_integration = MCPIntegration(**self.mcp_config)
        self.orchestrator = E2ETestOrchestrator(self.mcp_integration)

    def generate_case_from_description(self, case_id: str, description: str,
                                     execute_immediately: bool = False) -> Dict[str, Any]:
        """
        从业务描述生成测试案例

        Args:
            case_id: 案例编号
            description: 业务描述
            execute_immediately: 是否立即执行

        Returns:
            Dict: 生成结果
        """
        result = {
            'case_id': case_id,
            'intent_analysis': None,
            'case_info': None,
            'assertions': None,
            'execution_result': None,
            'error': None
        }

        try:
            # 1. 意图分析
            print(f"正在分析业务意图: {case_id}")
            intent = self.analyzer.analyze_business_intent(case_id, description)
            result['intent_analysis'] = asdict(intent)
            print(f"业务类型: {intent.business_type}")
            print(f"参与者: {', '.join(intent.participants)}")

            # 2. 生成案例
            print("正在生成案例信息...")
            case_info = self.generator.generate_case(case_id, intent)
            result['case_info'] = asdict(case_info)
            print(f"案例摘要: {case_info.caseSummary}")

            # 3. 生成断言
            print("正在生成断言信息...")
            template = self.generator._select_best_template(intent)
            assertions = self.generator.generate_assertions(intent, template)
            result['assertions'] = [asdict(a) for a in assertions]
            print(f"生成断言数量: {len(assertions)}")

            # 4. 执行案例（可选）
            if execute_immediately:
                print("正在执行案例...")
                execution_result = self.orchestrator.create_and_execute_case(
                    case_info=result['case_info'],
                    assertions=result['assertions'],
                    execute_params={}
                )
                result['execution_result'] = execution_result
                print("案例执行完成")

            print("案例生成成功！")
            return result

        except Exception as e:
            result['error'] = str(e)
            print(f"案例生成失败: {e}")
            return result

    def batch_generate(self, business_descriptions: List[Dict[str, str]],
                      execute_immediately: bool = False) -> List[Dict[str, Any]]:
        """
        批量生成测试案例

        Args:
            business_descriptions: 业务描述列表
            execute_immediately: 是否立即执行

        Returns:
            List: 生成结果列表
        """
        results = []

        for item in business_descriptions:
            print(f"\n{'='*60}")
            print(f"处理案例: {item['case_id']}")
            print(f"{'='*60}")

            result = self.generate_case_from_description(
                case_id=item['case_id'],
                description=item['description'],
                execute_immediately=execute_immediately
            )
            results.append(result)

        return results

    def save_results(self, results: List[Dict[str, Any]], output_dir: str):
        """
        保存生成结果

        Args:
            results: 生成结果列表
            output_dir: 输出目录
        """
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)

        for result in results:
            case_id = result['case_id']
            output_file = output_path / f"{case_id}_result.json"

            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(result, f, ensure_ascii=False, indent=2)

            print(f"结果已保存: {output_file}")


def main():
    """主函数"""
    print("E2E测试案例生成器")
    print("="*60)

    # 创建生成器实例
    generator = E2EGenerator()

    # 示例业务描述
    test_cases = [
        {
            "case_id": "epcc_201_0110_Z_AI_001",
            "description": "支付机构发起快捷支付，网联平台受理后转发给银行处理，银行返回处理并支付成功，平台接收后响应支付机构业务处理成功。"
        },
        {
            "case_id": "epcc_201_0120_Z_AI_002",
            "description": "用户发起转账汇款请求，银行系统受理后处理转账业务，收款方账户收到转账资金，转账状态更新为成功。"
        }
    ]

    # 生成案例
    print("开始批量生成测试案例...")
    results = generator.batch_generate(test_cases, execute_immediately=False)

    # 保存结果
    output_dir = config.get("output_config.output_dir", "output")
    print(f"\n正在保存结果到 {output_dir} 目录...")
    generator.save_results(results, output_dir)

    print("\n生成完成！")
    print("="*60)

    # 显示生成摘要
    for result in results:
        if result['error']:
            print(f"❌ {result['case_id']}: 生成失败 - {result['error']}")
        else:
            print(f"✅ {result['case_id']}: 生成成功")
            print(f"   业务类型: {result['intent_analysis']['business_type']}")
            print(f"   断言数量: {len(result['assertions'])}")


if __name__ == '__main__':
    main()