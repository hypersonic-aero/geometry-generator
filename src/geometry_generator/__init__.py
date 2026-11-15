"""Public package interface for geometry_generator."""

# --------------------------------------------------
# load necessary modules
# --------------------------------------------------
from importlib.metadata import (
    PackageNotFoundError,
    version,
)

from geometry_generator.blunted_tangent_ogive import BluntedTangentOgive
from geometry_generator.blunted_wedge import BluntedWedge
from geometry_generator.moldline import Moldline, sample_moldline
from geometry_generator.profile import Profile2D
from geometry_generator.writers import write_moldline

# --------------------------------------------------
# resolve package version
# --------------------------------------------------
try:
    __version__ = version("geometry-generator")
except PackageNotFoundError:
    __version__ = "0+unknown"


__all__ = [
    "BluntedTangentOgive",
    "BluntedWedge",
    "Moldline",
    "Profile2D",
    "__version__",
    "sample_moldline",
    "write_moldline",
]
