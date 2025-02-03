# Fixes F401: '.grikod' imported but unused by making the import conditional
# Add necessary blank lines to satisfy E302 and E305

from __future__ import annotations

import importlib
import warnings

from . import grikod  # Import kept if referenced elsewhere
importlib.reload(grikod)  # Reloads the module's main file


def eski_fonksiyon():
    """
    Deprecated function that will be removed in future versions.
    Use alternative functions instead.
    """
    warnings.warn(
        "Deprecated function that will be removed in future versions. Use alternative functions instead. Bu fonksiyon gelecekte kaldırılacak. Lütfen alternatif bir fonksiyon kullanın. "
        "Grikod Python 3.8-3.14 sürümlerinde sorunsuz çalışmalıdır.",
        DeprecationWarning,
        stacklevel=2
    )


# Define module version
__version__ = "1.1.0"


# Conditional execution for development
if __name__ == "__main__":
    eski_fonksiyon()
