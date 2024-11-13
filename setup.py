from setuptools import setup, find_packages
import setuptools_scm

setup(
    name='grikod',
    use_scm_version = True,  # Bu satır version bilgisini setuptools_scm ile alır
    requires = ["setuptools", "wheel", "setuptools_scm"],  # gerekli modüller
    version='1.0.8',
    packages=find_packages(where="src"),  # src dizinindeki modülleri bul
    package_dir={"": "src"},  # src dizinine yönlendirme
    setup_requires=["setuptools", "wheel", "setuptools_scm"],
    use_scm_version=True,  # sürüm bilgisini setuptools_scm ile al
    include_package_data=True,  # Gerektiğinde diğer dosyaları dahil et
    install_requires=[
        # Buraya bağımlılıkları ekleyin
    ],
)
