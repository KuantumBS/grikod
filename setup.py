from setuptools import setup, find_packages
import setuptools_scm

setup(
    name='grikod',
    use_scm_version = True,  # Bu satır version bilgisini setuptools_scm ile alır
    requires = ["setuptools", "wheel", "setuptools_scm"],  # gerekli modüller
    version='1.0.8',
    packages=find_packages(),
    install_requires=[
        # Buraya bağımlılıkları ekleyin
    ],
)
