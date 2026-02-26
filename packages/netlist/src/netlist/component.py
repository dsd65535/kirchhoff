"""This module contains the base definition for a component"""

from abc import ABC
from dataclasses import dataclass
from dataclasses import field
from typing import Any

Node = str


@dataclass
class ComponentParams:
    """Component Parameters"""

    refdes: str | None = None
    terminals: dict[str, Node | None] | None = field(default_factory=dict)
    config: dict[str, Any] | None = field(default_factory=dict)
    placement: tuple[float | None, float | None, float | None] = (None, None, None)


class Component(ABC):
    """The ABC for any Component"""

    def __init__(self, params: ComponentParams) -> None:
        """Initialize"""

        self._refdes = params.refdes
        self._terminals = {} if params.terminals is None else params.terminals
        self._config = {} if params.config is None else params.config
        self._placement = params.placement

    @property
    def refdes(self) -> str | None:
        """Reference Designator"""

        return self._refdes

    @property
    def terminals(self) -> dict[str, Node | None]:
        """Mapping of Terminals to Nodes"""

        return self._terminals

    @property
    def config(self) -> dict[str, Any]:
        """Device-specific Configuration"""

        return self._config

    @property
    def placement(self) -> tuple[float | None, float | None, float | None]:
        """Placement (x, y, rotation in degrees)"""

        return self._placement
