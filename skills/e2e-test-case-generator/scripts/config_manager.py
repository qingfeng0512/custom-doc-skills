#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
配置管理器
负责读取和管理config.yaml配置文件
"""

import os
import yaml
from typing import Dict, Any, Optional
from pathlib import Path


class ConfigManager:
    """配置管理器单例"""

    _instance = None
    _config = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if self._config is None:
            self._load_config()

    def _load_config(self):
        """加载配置文件"""
        # 获取配置文件的路径（相对于当前文件的位置）
        current_dir = Path(__file__).parent.parent
        config_file = current_dir / "config.yaml"

        if not config_file.exists():
            raise FileNotFoundError(f"配置文件不存在: {config_file}")

        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                self._config = yaml.safe_load(f)
        except yaml.YAMLError as e:
            raise ValueError(f"配置文件格式错误: {e}")

    def get(self, key_path: str, default: Any = None) -> Any:
        """
        获取配置值

        Args:
            key_path: 配置键路径，使用'.'分隔，例如 'ai_config.api_key'
            default: 默认值

        Returns:
            配置值
        """
        keys = key_path.split('.')
        value = self._config

        try:
            for key in keys:
                value = value[key]
            return value
        except (KeyError, TypeError):
            return default

    def get_ai_config(self) -> Dict[str, Any]:
        """获取AI配置"""
        return {
            "api_key": self.get("ai_config.api_key"),
            "api_base": self.get("ai_config.api_base"),
            "model": self.get("ai_config.model"),
            "temperature": self.get("ai_config.temperature", 0.1),
            "max_tokens": self.get("ai_config.max_tokens", 2000)
        }

    def get_mcp_config(self) -> Dict[str, Any]:
        """获取MCP配置"""
        return {
            "base_url": self.get("mcp_config.base_url"),
            "auth_token": self.get("mcp_config.auth_token")
        }

    def get_template_config(self) -> Dict[str, Any]:
        """获取模板配置"""
        return {
            "templates_dir": self.get("template_config.templates_dir"),
            "match_weights": self.get("template_config.match_weights")
        }

    def get_output_config(self) -> Dict[str, Any]:
        """获取输出配置"""
        return {
            "output_dir": self.get("output_config.output_dir"),
            "execute_immediately": self.get("output_config.execute_immediately", False)
        }

    def get_logging_config(self) -> Dict[str, Any]:
        """获取日志配置"""
        return {
            "level": self.get("logging_config.level", "INFO"),
            "format": self.get("logging_config.format")
        }

    def reload(self):
        """重新加载配置文件"""
        self._load_config()

    @classmethod
    def get_instance(cls) -> 'ConfigManager':
        """获取配置管理器实例"""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance


# 创建全局配置管理器实例
config = ConfigManager.get_instance()