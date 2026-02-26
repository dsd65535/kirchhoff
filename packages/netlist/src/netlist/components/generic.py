"""This module containts some generic components"""

from dataclasses import asdict
from dataclasses import dataclass
from typing import Any

from ..component import Component
from ..component import ComponentParams
from ..component import Node


@dataclass
class TwoTerminalTerminals:
    """Generic Two-Terminal Device Terminals"""

    a: Node | None = None
    b: Node | None = None


@dataclass
class ResistorConfig:
    """Resistor Configuration"""

    resistance: float | str | None = None  # ohms


class Resistor(Component):
    """A Resistor"""

    def __init__(self, params: ComponentParams) -> None:
        """Initialize"""

        self._terminals = (
            TwoTerminalTerminals()
            if params.terminals is None
            else TwoTerminalTerminals(**params.terminals)
        )
        self._config = (
            ResistorConfig()
            if params.config is None
            else ResistorConfig(**params.config)
        )

        super().__init__(params)

    @property
    def terminals(self) -> dict[str, Node | None]:
        """Mapping of Terminals to Nodes"""

        return asdict(self._terminals)

    @property
    def config(self) -> dict[str, Any]:
        """Device-specific Configuration"""

        return asdict(self._config)


@dataclass
class CapacitorConfig:
    """Capacitor Configuration"""

    capacitance: float | str | None = None  # ohms


class Capacitor(Component):
    """A Capacitor"""

    def __init__(self, params: ComponentParams) -> None:
        """Initialize"""

        self._terminals = (
            TwoTerminalTerminals()
            if params.terminals is None
            else TwoTerminalTerminals(**params.terminals)
        )
        self._config = (
            CapacitorConfig()
            if params.config is None
            else CapacitorConfig(**params.config)
        )

        super().__init__(params)

    @property
    def terminals(self) -> dict[str, Node | None]:
        """Mapping of Terminals to Nodes"""

        return asdict(self._terminals)

    @property
    def config(self) -> dict[str, Any]:
        """Device-specific Configuration"""

        return asdict(self._config)


@dataclass
class InductorConfig:
    """Inductor Configuration"""

    inductance: float | str | None = None  # ohms


class Inductor(Component):
    """A Inductor"""

    def __init__(self, params: ComponentParams) -> None:
        """Initialize"""

        self._terminals = (
            TwoTerminalTerminals()
            if params.terminals is None
            else TwoTerminalTerminals(**params.terminals)
        )
        self._config = (
            InductorConfig()
            if params.config is None
            else InductorConfig(**params.config)
        )

        super().__init__(params)

    @property
    def terminals(self) -> dict[str, Node | None]:
        """Mapping of Terminals to Nodes"""

        return asdict(self._terminals)

    @property
    def config(self) -> dict[str, Any]:
        """Device-specific Configuration"""

        return asdict(self._config)
