#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MCP服务集成器
集成e2e-mcp-server的API服务
"""

import json
import requests
from typing import Dict, List, Any, Optional
from dataclasses import asdict


class MCPIntegration:
    """MCP服务集成器"""

    def __init__(self, base_url: str, auth_token: str = None):
        """
        初始化MCP集成器

        Args:
            base_url: MCP服务基础URL
            auth_token: 认证令牌
        """
        self.base_url = base_url.rstrip('/')
        self.auth_token = auth_token
        self.headers = {
            'Content-Type': 'application/json'
        }
        if auth_token:
            self.headers['Authorization'] = f'Bearer {auth_token}'

    def add_case(self, case_info: Dict[str, Any]) -> Dict[str, Any]:
        """
        添加测试案例

        Args:
            case_info: 案例信息

        Returns:
            Dict: API响应
        """
        endpoint = f"{self.base_url}/api/cases"
        response = requests.post(endpoint, json=case_info, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def add_assertion(self, case_id: str, assertions: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        添加断言

        Args:
            case_id: 案例ID
            assertions: 断言信息列表

        Returns:
            Dict: API响应
        """
        endpoint = f"{self.base_url}/api/cases/{case_id}/assertions"
        response = requests.post(endpoint, json=assertions, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def execute_case(self, case_id: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        执行测试案例

        Args:
            case_id: 案例ID
            params: 执行参数

        Returns:
            Dict: API响应
        """
        endpoint = f"{self.base_url}/api/cases/{case_id}/execute"
        payload = params or {}
        response = requests.post(endpoint, json=payload, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_execution_result(self, execution_id: str) -> Dict[str, Any]:
        """
        获取执行结果

        Args:
            execution_id: 执行ID

        Returns:
            Dict: 执行结果
        """
        endpoint = f"{self.base_url}/api/executions/{execution_id}/result"
        response = requests.get(endpoint, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_case_details(self, case_id: str) -> Dict[str, Any]:
        """
        获取案例详情

        Args:
            case_id: 案例ID

        Returns:
            Dict: 案例详情
        """
        endpoint = f"{self.base_url}/api/cases/{case_id}"
        response = requests.get(endpoint, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def list_cases(self, business_type: str = None, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        列出案例

        Args:
            business_type: 业务类型过滤
            page: 页码
            page_size: 每页大小

        Returns:
            Dict: 案例列表
        """
        endpoint = f"{self.base_url}/api/cases"
        params = {
            'page': page,
            'page_size': page_size
        }
        if business_type:
            params['business_type'] = business_type

        response = requests.get(endpoint, params=params, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def validate_case(self, case_info: Dict[str, Any]) -> Dict[str, Any]:
        """
        验证案例数据

        Args:
            case_info: 案例信息

        Returns:
            Dict: 验证结果
        """
        endpoint = f"{self.base_url}/api/cases/validate"
        response = requests.post(endpoint, json=case_info, headers=self.headers)
        response.raise_for_status()
        return response.json()


class E2ETestOrchestrator:
    """E2E测试编排器"""

    def __init__(self, mcp_integration: MCPIntegration):
        """
        初始化测试编排器

        Args:
            mcp_integration: MCP集成器实例
        """
        self.mcp = mcp_integration

    def create_and_execute_case(self, case_info: Dict[str, Any],
                              assertions: List[Dict[str, Any]],
                              execute_params: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        创建并执行案例

        Args:
            case_info: 案例信息
            assertions: 断言信息
            execute_params: 执行参数

        Returns:
            Dict: 完整流程结果
        """
        result = {
            'case_creation': None,
            'assertion_addition': None,
            'execution': None,
            'validation': None
        }

        try:
            # 1. 创建案例
            print("正在创建案例...")
            case_creation = self.mcp.add_case(case_info)
            result['case_creation'] = case_creation
            case_id = case_creation.get('case_id')

            if not case_id:
                raise ValueError("案例创建失败：未获取到案例ID")

            print(f"案例创建成功，案例ID: {case_id}")

            # 2. 添加断言
            print("正在添加断言...")
            assertion_result = self.mcp.add_assertion(case_id, assertions)
            result['assertion_addition'] = assertion_result
            print("断言添加成功")

            # 3. 执行案例
            print("正在执行案例...")
            execution = self.mcp.execute_case(case_id, execute_params)
            result['execution'] = execution
            execution_id = execution.get('execution_id')

            if not execution_id:
                raise ValueError("案例执行失败：未获取到执行ID")

            print(f"案例执行成功，执行ID: {execution_id}")

            # 4. 等待并获取执行结果
            print("正在获取执行结果...")
            execution_result = self.mcp.get_execution_result(execution_id)
            result['validation'] = execution_result
            print("执行结果获取成功")

            return result

        except Exception as e:
            result['error'] = str(e)
            print(f"流程执行失败: {e}")
            return result

    def validate_case_before_save(self, case_info: Dict[str, Any]) -> bool:
        """
        保存前验证案例

        Args:
            case_info: 案例信息

        Returns:
            bool: 验证是否通过
        """
        try:
            validation_result = self.mcp.validate_case(case_info)
            return validation_result.get('valid', False)
        except Exception as e:
            print(f"验证失败: {e}")
            return False


if __name__ == '__main__':
    # 配置示例
    MCP_CONFIG = {
        "base_url": "http://localhost:8000",  # MCP服务地址
        "auth_token": None  # 如果需要认证
    }

    # 初始化集成器
    mcp_integration = MCPIntegration(**MCP_CONFIG)
    orchestrator = E2ETestOrchestrator(mcp_integration)

    # 测试案例数据
    test_case = {
        "caseId": "test_case_001",
        "caseSummary": "测试案例",
        "caseData": {},
        "mockRtn": {},
        "msgTemplate": {}
    }

    test_assertions = [
        {
            "assertType": "MSG",
            "assertKey": "status",
            "assertValue": "00",
            "assertRule": "REQUIRED",
            "createBy": "AI",
            "description": "验证状态码"
        }
    ]

    print("MCP服务集成器已就绪")
    print("使用方法:")
    print("1. 配置MCP服务地址")
    print("2. 使用E2ETestOrchestrator执行完整流程")
    print("3. 或单独调用MCPIntegration的各个方法")