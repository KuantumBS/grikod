# Grikod (Gri Kod, Gray Code)

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FKuantumBS%2Fgrikod.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FKuantumBS%2Fgrikod?ref=badge_shield)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FKuantumBS%2Fgrikod.svg?type=shield&issueType=security)](https://app.fossa.com/projects/git%2Bgithub.com%2FKuantumBS%2Fgrikod?ref=badge_shield&issueType=security)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FKuantumBS%2Fgrikod.svg?type=small)](https://app.fossa.com/projects/git%2Bgithub.com%2FKuantumBS%2Fgrikod?ref=badge_small)
[![Documentation Status](https://readthedocs.org/projects/grikod/badge/?version=main)](https://grikod.readthedocs.io/en/main/?badge=main)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14148764.svg)](https://doi.org/10.5281/zenodo.14148764)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14147520.svg)](https://doi.org/10.5281/zenodo.14147520)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.12731346.svg)](https://doi.org/10.5281/zenodo.12731346)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14029245.svg)](https://doi.org/10.5281/zenodo.14029245)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14029276.svg)](https://doi.org/10.5281/zenodo.14029276)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14099425.svg)](https://doi.org/10.5281/zenodo.14099425)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14099659.svg)](https://doi.org/10.5281/zenodo.14099659)
[![Anaconda-Server Badge](https://anaconda.org/bilgi/grikod/badges/version.svg)](https://anaconda.org/bilgi/grikod)
[![Anaconda-Server Badge](https://anaconda.org/bilgi/grikod/badges/latest_release_date.svg)](https://anaconda.org/bilgi/grikod)
[![Anaconda-Server Badge](https://anaconda.org/bilgi/grikod/badges/platforms.svg)](https://anaconda.org/bilgi/grikod)
[![Anaconda-Server Badge](https://anaconda.org/bilgi/grikod/badges/license.svg)](https://anaconda.org/bilgi/grikod)
[![Open Source](https://img.shields.io/badge/Open%20Source-Open%20Source-brightgreen.svg)](https://opensource.org/)
[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python library for converting binary numbers to Gray Code with ease.

---

## Tanım (Türkçe)
Gri Kod: Grikod İkili sayıları Gri Koda çevirir.

## Description (English)
Gri Kod: Grikod converts binary numbers to Gray Code.

---

## Kurulum (Türkçe) / Installation (English)

### Python ile Kurulum / Install with pip, conda, mamba
```bash
pip install grikod -U
python -m pip install -U grikod
conda install bilgi::grikod -y
mamba install bilgi::grikod -y
```

```diff
- pip uninstall grikod -y
+ pip install -U grikod
+ python -m pip install -U grikod
```

[PyPI](https://pypi.org/project/grikod/)

### Test Kurulumu / Test Installation

```bash
pip install -i https://test.pypi.org/simple/ grikod -U
```

### Github Master Kurulumu / GitHub Master Installation

**Terminal:**

```bash
pip install git+https://github.com/KuantumBS/grikod.git
```

**Jupyter Lab, Notebook, Visual Studio Code:**

```python
!pip install git+https://github.com/KuantumBS/grikod.git
# or
%pip install git+https://github.com/KuantumBS/grikod.git
```

---

## Kullanım (Türkçe) / Usage (English)

```python
import grikod # Restart Kernel veya/or Restart Kernel and Clear Outputs

# veya/or
import importlib
import grikod
importlib.reload(grikod) # Modülünüzün ana dosyasını burada yeniden yükler

# Run this cell (Shift+Enter): Input: 100
# Output example
# 000:000
# 001:001
# 010:011
# 011:010
# 100:110
# 101:111
# 110:101
# 111:100
```
```python
import grikod
grikod.__version__
```
---

### Development
```bash
# Clone the repository
git clone https://github.com/KuantumBS/grikod.git
cd grikod

# Install in development mode
python -m pip install -ve . # Install package in development mode

# Run tests
pytest

Notebook, Jupyterlab, Colab, Visual Studio Code
!python -m pip install git+https://github.com/KuantumBS/grikod.git
```
---

## Citation

If this library was useful to you in your research, please cite us. Following the [GitHub citation standards](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files), here is the recommended citation.

### BibTeX

```bibtex
@software{Kececi_Gri_Kod_2024,
    author = {Keçeci, Mehmet},
    license = {MIT},
    month = nov,
    title = {{Gri Kod}},
    url = {https://pypi.org/project/grikod/},
    version = {1.1.0},
    year = {2025}
}
```

```bibtex
@software{Kececi_Gri_Kod_2024,
    author = {Keçeci, Mehmet},
    license = {MIT},
    month = nov,
    title = {{Gri Kod}},
    url = {https://pypi.org/project/grikod/},
    version = {1.0.80},
    year = {2024}
}

### APA

```
Keçeci, M. (2025). Gri Kod: Grikod converts binary numbers to Gray Code. (Version 1.1.0) [Computer software]. https://pypi.org/project/grikod/

Keçeci, M. (2024). Gri Kod: Grikod converts binary numbers to Gray Code. (Version 1.0.80) [Computer software]. https://pypi.org/project/grikod/
```

### Chicago

```
Keçeci, Mehmet. “Grikod”. Anaconda, Inc., November 13, 2024. https://doi.org/10.5281/zenodo.14148764.

Keçeci, Mehmet. “Grikod”. PYPI, Python Package Index, Python Software Foundation, November 13, 2024. https://doi.org/10.5281/zenodo.14147520.

Keçeci, Mehmet. “Grikod”. Anaconda, Inc., November 12, 2024. https://doi.org/10.5281/zenodo.14099659.

Keçeci, Mehmet. “Grikod”. PYPI, Python Package Index, Python Software Foundation, November 12, 2024. https://doi.org/10.5281/zenodo.14099425.

Keçeci, Mehmet. “Grikod”. Anaconda, Inc., November 01, 2024. https://zenodo.org/records/14029276.

Keçeci, Mehmet. “Grikod”. Python Package Index, November 01, 2024. https://zenodo.org/records/14029245.

Keçeci, Mehmet. “Grikod”. Python Package Index, October 29, 2024. https://doi.org/10.5281/zenodo.14004878.

Keçeci, Mehmet. “Grikod”. Anaconda, Inc., October 29, 2024. https://doi.org/10.5281/zenodo.14004846.

Keçeci, Mehmet. “Grikod.” PYPI, February 18, 2024. https://doi.org/10.5281/zenodo.12731346.
```
---

## Lisans (Türkçe) / License (English)

This project is licensed under the MIT License.

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FKuantumBS%2Fgrikod.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FKuantumBS%2Fgrikod?ref=badge_large)

[Grikod YouTube Video Linki](https://www.youtube.com/watch?v=IJnIpOuV92E)
