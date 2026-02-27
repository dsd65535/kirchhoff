"""This module contains definitions for the 9 Primitives"""

from dataclasses import dataclass

from .common import Node


@dataclass
class PrimitiveResistor:
    """A Primitive Resistor"""

    terminals: tuple[Node, Node]
    resistance: float | str  # ohms


@dataclass
class PrimitiveCapacitor:
    """A Primitive Capacitor"""

    terminals: tuple[Node, Node]
    capacitance: float | str  # farads


@dataclass
class PrimitiveInductor:
    """A Primitive Inductor"""

    terminals: tuple[Node, Node]
    inductance: float | str  # henries


@dataclass
class PrimitiveVoltageSource:
    """A Primitive Voltage Source.

    if `voltage` is positive,
    then the potential at `terminals[0]` will be higher
    than the potential at `terminals[1]`
    """

    terminals: tuple[Node, Node]
    voltage: float | str  # volts


@dataclass
class PrimitiveCurrentSource:
    """A Primitive Current Source.

    if `current` is positive,
    then current will be leaving `terminals[0]` and entering `terminals[1]`
    (electrons will be entering `terminals[0]` and leaving `terminals[1]`)
    """

    terminals: tuple[Node, Node]
    current: float | str  # amperes


@dataclass
class PrimitiveVoltageControlledVoltageSource:
    """A Primitive Voltage Controlled Voltage Source.

    if `gain` is positive,
    and the potential at `control_terminals[0]` is higher
    than the potential at `control_terminals[1]`
    then the potential at `source_terminals[0]` will be higher
    than the potential at `source_terminals[1]`
    """

    source_terminals: tuple[Node, Node]
    control_terminals: tuple[Node, Node]
    gain: float | str  # unitless


@dataclass
class PrimitiveVoltageControlledCurrentSource:
    """A Primitive Voltage Controlled Current Source.

    if `transconductance` is positive,
    and the potential at `control_terminals[0]` is higher
    than the potential at `control_terminals[1]`
    then current will be leaving `source_terminals[0]` and entering `source_terminals[1]`
    (electrons will be entering `source_terminals[0]` and leaving `source_terminals[1]`)
    """

    source_terminals: tuple[Node, Node]
    control_terminals: tuple[Node, Node]
    transconductance: float | str  # siemens


@dataclass
class PrimitiveCurrentControlledVoltageSource:
    """A Primitive Current Controlled Voltage Source.

    if `gain` is positive,
    and current is leaving `control_terminals[0]` and entering `control_terminals[1]`
    (electrons are entering `control_terminals[0]` and leaving `control_terminals[1]`)
    then the potential at `source_terminals[0]` will be higher
    than the potential at `source_terminals[1]`
    """

    source_terminals: tuple[Node, Node]
    control_terminals: tuple[Node, Node]
    transresistance: float | str  # ohms


@dataclass
class PrimitiveCurrentControlledCurrentSource:
    """A Primitive Current Controlled Current Source.

    if `gain` is positive,
    and current is leaving `control_terminals[0]` and entering `control_terminals[1]`
    (electrons are entering `control_terminals[0]` and leaving `control_terminals[1]`)
    then current will be leaving `source_terminals[0]` and entering `source_terminals[1]`
    (electrons will be entering `source_terminals[0]` and leaving `source_terminals[1]`)
    """

    source_terminals: tuple[Node, Node]
    control_terminals: tuple[Node, Node]
    gain: float | str  # unitless


Primitive = (
    PrimitiveResistor
    | PrimitiveCapacitor
    | PrimitiveInductor
    | PrimitiveVoltageSource
    | PrimitiveCurrentSource
    | PrimitiveVoltageControlledVoltageSource
    | PrimitiveVoltageControlledCurrentSource
    | PrimitiveCurrentControlledVoltageSource
    | PrimitiveCurrentControlledCurrentSource
)
