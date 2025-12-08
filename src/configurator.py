#configurator.py

# configurator.py

from typing import List, Dict, Any
from .core import Firewall, TerminalRule
from .decorators import LoggerDecorator, BanDecorator
from .interfaces import Rule


class FirewallConfigurator:
    """
    Charge et applique une configuration de règles au Firewall (Singleton).
    Peut être alimenté par un fichier JSON/YAML, ou une structure Python.
    """

    DECORATOR_MAP = {
        "logger": LoggerDecorator,
        "ban": BanDecorator
    }

    RULE_MAP = {
        "terminal": TerminalRule
    }

    def __init__(self):
        self.firewall = Firewall()

    def load_config(self, config: List[Dict[str, Any]]):
        """
        Recharge entièrement la configuration du firewall.
        :param config: Liste de dictionnaires décrivant des règles
        """
        self.firewall.clear_rules()

        for rule_def in config:
            rule = self._build_rule(rule_def)
            self.firewall.add_rule(rule)

    def _build_rule(self, rule_def: Dict[str, Any]) -> Rule:
        """
        Construit une règle selon une définition :
        {
            "type": "terminal",
            "action": "allow",
            "decorators": ["logger", "ban"]
        }
        """

        rule_type = rule_def.get("type")
        if rule_type not in self.RULE_MAP:
            raise ValueError(f"Unknown rule type: {rule_type}")

        # Base rule
        rule = self.RULE_MAP[rule_type](**{
            k: v for k, v in rule_def.items()
            if k not in ("type", "decorators")
        })

        # Apply decorators
        for deco_name in rule_def.get("decorators", []):
            if deco_name not in self.DECORATOR_MAP:
                raise ValueError(f"Unknown decorator: {deco_name}")

            decorator_cls = self.DECORATOR_MAP[deco_name]
            rule = decorator_cls(rule)

        return rule

    def print_config(self):
        """Debug : Affiche les règles actuelles."""
        print("=== FIREWALL CONFIG ===")
        for r in self.firewall.rules:
            print(f"- {r}")


# Exemple d'usage possible depuis main.py
if __name__ == "__main__":
    sample_config = [
        {
            "type": "terminal",
            "action": "allow",
            "decorators": ["logger"]
        },
        {
            "type": "terminal",
            "action": "deny",
            "decorators": ["ban", "logger"]
        }
    ]

    conf = FirewallConfigurator()
    conf.load_config(sample_config)
    conf.print_config()
