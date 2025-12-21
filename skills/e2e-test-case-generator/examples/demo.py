#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
E2E测试案例生成器 - 使用示例
演示如何使用技能生成测试案例
"""

import json
import sys
from pathlib import Path

# 添加scripts目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from test_skill import SimpleIntentAnalyzer


def demo_single_case():
    """演示单个案例生成"""
    print("="*60)
    print("演示：单个测试案例生成")
    print("="*60)

    # 初始化分析器
    analyzer = SimpleIntentAnalyzer()

    # 业务描述
    case_id = "epcc_201_0110_Z_AI_001"
    description = "支付机构发起快捷支付，网联平台受理后转发给银行处理，银行返回处理并支付成功，平台接收后响应支付机构业务处理成功。"

    print(f"\n📝 案例编号: {case_id}")
    print(f"📝 业务描述: {description}")

    # 分析意图
    print("\n🔍 正在进行意图分析...")
    intent = analyzer.analyze_business_intent(case_id, description)

    print(f"\n✅ 分析结果:")
    print(f"   业务类型: {intent.business_type}")
    print(f"   业务子类型: {intent.business_subtype}")
    print(f"   参与者: {', '.join(intent.participants)}")
    print(f"   流程步骤: {', '.join(intent.flow_steps)}")
    print(f"   关键参数: {intent.key_parameters}")
    print(f"   成功标准: {', '.join(intent.success_criteria)}")

    # 生成案例信息
    print("\n📋 正在生成案例信息...")
    case_info = {
        "caseId": case_id,
        "caseSummary": f"{'、'.join(intent.participants)}执行{intent.business_type}业务，流程：{' → '.join(intent.flow_steps)}",
        "caseData": {
            "transType": intent.business_subtype.lower(),
            "amount": intent.key_parameters.get("amount", "100.00"),
            "orderId": f"ORDER_{1640995200000}",
            "participants": intent.participants,
            "flowSteps": intent.flow_steps
        },
        "mockRtn": {
            "responseCode": "00",
            "responseMsg": "交易成功",
            "transId": f"TXN_{1640995200000}",
            "status": "SUCCESS"
        }
    }

    print(f"   ✅ 案例ID: {case_info['caseId']}")
    print(f"   ✅ 案例摘要: {case_info['caseSummary']}")

    # 生成断言信息
    print("\n🔍 正在生成断言信息...")
    assertions = [
        {
            "assertType": "MSG",
            "assertKey": "responseCode",
            "assertValue": "00",
            "assertRule": "REQUIRED",
            "createBy": "AI",
            "description": "验证交易响应码为成功"
        },
        {
            "assertType": "BUSINESS",
            "assertKey": "payment_status",
            "assertValue": "SUCCESS",
            "assertRule": "REQUIRED",
            "createBy": "AI",
            "description": "验证支付状态为成功"
        },
        {
            "assertType": "TIMING",
            "assertKey": "response_time",
            "assertValue": "<5000",
            "assertRule": "REQUIRED",
            "createBy": "AI",
            "description": "验证响应时间在5秒内"
        }
    ]

    print(f"   ✅ 生成断言数量: {len(assertions)}")
    for i, assertion in enumerate(assertions, 1):
        print(f"      {i}. {assertion['description']}")

    # 输出JSON格式结果
    print("\n📄 生成的标准JSON格式:")
    print("-"*60)
    result = {
        "case_info": case_info,
        "assertions": assertions,
        "intent_analysis": {
            "business_type": intent.business_type,
            "business_subtype": intent.business_subtype,
            "participants": intent.participants,
            "flow_steps": intent.flow_steps,
            "key_parameters": intent.key_parameters,
            "success_criteria": intent.success_criteria
        }
    }

    print(json.dumps(result, ensure_ascii=False, indent=2))
    print("-"*60)

    return result


def demo_batch_cases():
    """演示批量案例生成"""
    print("\n\n" + "="*60)
    print("演示：批量测试案例生成")
    print("="*60)

    # 业务描述列表
    business_descriptions = [
        {
            "case_id": "epcc_201_0110_Z_AI_001",
            "description": "支付机构发起快捷支付，网联平台受理后转发给银行处理，银行返回处理并支付成功，平台接收后响应支付机构业务处理成功。"
        },
        {
            "case_id": "epcc_201_0120_Z_AI_002",
            "description": "用户发起转账汇款请求，银行系统受理后处理转账业务，收款方账户收到转账资金，转账状态更新为成功。"
        },
        {
            "case_id": "epcc_201_0130_Z_AI_003",
            "description": "用户发起余额查询请求，系统受理查询请求后查询账户余额，成功返回余额信息。"
        }
    ]

    analyzer = SimpleIntentAnalyzer()
    results = []

    print(f"\n📊 批量处理 {len(business_descriptions)} 个案例:")

    for i, item in enumerate(business_descriptions, 1):
        print(f"\n{i}. 处理案例: {item['case_id']}")

        intent = analyzer.analyze_business_intent(
            item['case_id'],
            item['description']
        )

        result = {
            "case_id": item['case_id'],
            "business_type": intent.business_type,
            "participants": intent.participants,
            "flow_steps": intent.flow_steps
        }
        results.append(result)

        print(f"   业务类型: {intent.business_type}")
        print(f"   参与者: {', '.join(intent.participants)}")

    # 汇总结果
    print("\n📈 批量生成汇总:")
    print("-"*60)
    business_types = {}
    for result in results:
        bt = result['business_type']
        business_types[bt] = business_types.get(bt, 0) + 1

    for bt, count in business_types.items():
        print(f"   {bt}: {count} 个案例")

    print(f"\n总计: {len(results)} 个案例")
    print("-"*60)

    return results


def demo_mcp_integration():
    """演示MCP集成流程"""
    print("\n\n" + "="*60)
    print("演示：MCP服务集成流程")
    print("="*60)

    # 模拟MCP集成流程
    print("\n🔗 模拟MCP服务集成流程:")
    print("   1️⃣  创建案例...")
    print("       POST /api/cases")
    print("       ✅ 案例创建成功，案例ID: epcc_201_0110_Z_AI_001")

    print("\n   2️⃣  添加断言...")
    print("       POST /api/cases/epcc_201_0110_Z_AI_001/assertions")
    print("       ✅ 断言添加成功，共添加 3 个断言")

    print("\n   3️⃣  执行案例...")
    print("       POST /api/cases/epcc_201_0110_Z_AI_001/execute")
    print("       ✅ 案例执行成功，执行ID: EXEC_1640995200001")

    print("\n   4️⃣  获取执行结果...")
    print("       GET /api/executions/EXEC_1640995200001/result")
    print("       ✅ 执行完成，状态: SUCCESS")

    # 显示执行结果
    execution_result = {
        "execution_id": "EXEC_1640995200001",
        "case_id": "epcc_201_0110_Z_AI_001",
        "status": "SUCCESS",
        "start_time": "2025-01-20 10:00:00",
        "end_time": "2025-01-20 10:00:03",
        "duration": "3s",
        "assertions": [
            {
                "assertKey": "responseCode",
                "status": "PASS",
                "message": "验证交易响应码为成功"
            },
            {
                "assertKey": "payment_status",
                "status": "PASS",
                "message": "验证支付状态为成功"
            },
            {
                "assertKey": "response_time",
                "status": "PASS",
                "message": "验证响应时间在5秒内"
            }
        ]
    }

    print("\n📊 执行结果详情:")
    print("-"*60)
    print(json.dumps(execution_result, ensure_ascii=False, indent=2))
    print("-"*60)

    print("\n🎉 完整流程执行成功！")


def main():
    """主函数"""
    print("🚀 E2E测试案例生成器 - 功能演示")
    print("="*60)
    print("本演示展示了如何使用技能生成E2E测试案例")
    print("="*60)

    try:
        # 演示1: 单个案例生成
        demo_single_case()

        # 演示2: 批量案例生成
        demo_batch_cases()

        # 演示3: MCP集成流程
        demo_mcp_integration()

        print("\n\n" + "="*60)
        print("✨ 演示完成！")
        print("="*60)
        print("\n📚 使用说明:")
        print("   - 查看 SKILL.md 了解详细使用说明")
        print("   - 查看 scripts/ 目录下的脚本文件")
        print("   - 查看 assets/templates/ 目录下的模板文件")
        print("\n🔧 下一步:")
        print("   1. 配置AI分析器的API密钥")
        print("   2. 配置MCP服务地址")
        print("   3. 根据需要添加更多业务模板")
        print("   4. 运行 python3 scripts/test_skill.py 进行测试")

    except Exception as e:
        print(f"\n❌ 演示过程中发生错误: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()