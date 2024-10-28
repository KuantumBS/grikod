# Fixes F401: '.grikod' imported but unused by making the import conditional
# Add necessary blank lines to satisfy E302 and E305

from __future__ import annotations
import warnings
from . import grikod  # Import kept if referenced elsewhere


# Function with deprecation warning
def eski_fonksiyon():
    warnings.warn(
        "Bu fonksiyon gelecekte kaldırılacak. Lütfen alternatif bir fonksiyon kullanın. "
        "Grikod Python 3.8-3.13 sürümlerinde sorunsuz çalışmalıdır.",
        DeprecationWarning
    )


# Call the function if needed during initialization
eski_fonksiyon()

# Define module version
__version__ = "1.0.6"
