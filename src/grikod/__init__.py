from __future__ import annotations
from . import grikod
import warnings

def eski_fonksiyon():
    warnings.warn(
        "Bu fonksiyon gelecekte kaldırılacak. Lütfen alternatif bir fonksiyon kullanın. "
        "Grikod Python 3.8-3.13 sürümlerinde sorunsuz çalışmalıdır.",
        DeprecationWarning
    )

eski_fonksiyon()

__version__ = "1.0.6"
