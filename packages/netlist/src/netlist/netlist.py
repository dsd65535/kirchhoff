"""This module implements a netlist"""

from .component import Component


class Netlist:
    # pylint:disable=too-few-public-methods  # WIP
    """A Netlist of Componenets"""

    def __init__(self, components: list[Component]) -> None:
        """Initialize"""

        self._components = components
