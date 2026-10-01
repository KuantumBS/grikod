from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension(
        name="grikod",
        sources=["grikod/grikod.py"],  # Doğru yol
    )
]

setup(
    ext_modules=cythonize(
        extensions,
        compiler_directives={'language_level': 3},
    ),
    zip_safe=False,
)
