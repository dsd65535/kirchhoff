"""This module contains the base definition for a component"""

from abc import ABC
from dataclasses import dataclass
from dataclasses import field
from typing import Any

from .common import Node
from .primitives import Primitive


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
        self._placement = params.placement

    @property
    def refdes(self) -> str | None:
        """Reference Designator"""

        return self._refdes

    @property
    def terminals(self) -> dict[str, Node | None]:
        """Mapping of Terminals to Nodes"""

        raise NotImplementedError

    @property
    def config(self) -> dict[str, Any]:
        """Device-specific Configuration"""

        raise NotImplementedError

    @property
    def placement(self) -> tuple[float | None, float | None, float | None]:
        """Placement (x, y, rotation in degrees)"""

        return self._placement

    @property
    def as_primitives(self) -> list[Primitive]:
        """As a network of primitives at current operating point"""

        raise NotImplementedError
