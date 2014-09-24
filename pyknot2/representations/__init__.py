'''
Knot representations
====================

This module contains classes and functions for representing
knots in knot diagrams, mainly the
:class:`pyknot2.representations.gausscode.GaussCode` and
:class:`pyknot2.representations.planardiagram.PlanarDiagram`.

These provide convenient methods to convert between different
representations, and to simplify via Reidemeister moves.
'''

from .gausscode import GaussCode
from .planardiagram import PlanarDiagram
__all__ = ['GaussCode', 'PlanarDiagram']

