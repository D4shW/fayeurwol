#interfaces.py

from abc import ABC, abstractmethod

class Rule(ABC):
    @abstractmethod
    def apply(self, packet: dict) -> bool:
        pass
class Decorator(ABC):
    def __init__(self, rule: Rule):
        self._rule = rule

    @abstractmethod
    def apply(self, packet: dict) -> bool:
        pass
class TerminalRule(Rule):
    def __init__(self, action: str):
        self.action = action

    def apply(self, packet: dict) -> bool:
        return self.action == "allow"
class LoggerDecorator(Decorator):
    def apply(self, packet: dict) -> bool:
        print(f"Logging packet: {packet}")
        return self._rule.apply(packet)
class BanDecorator(Decorator):
    def apply(self, packet: dict) -> bool:
        if packet.get("source_ip") in ["dangerous_ip_1", "dangerous_ip_2"]:
            print(f"Banning packet from {packet.get('source_ip')}")
            return False
        return self._rule.apply(packet)
class Firewall:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule: Rule):
        self.rules.append(rule)

    def clear_rules(self):
        self.rules = []

    def process_packet(self, packet: dict) -> bool:
        for rule in self.rules:
            if not rule.apply(packet):
                return False
        return True
from typing import List, Dict, Any
from .core import Firewall, TerminalRule
from .decorators import LoggerDecorator, BanDecorator
from .interfaces import Rule