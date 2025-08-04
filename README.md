# Grikod (Gri Kod, Gray Code)

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FKuantumBS%2Fgrikod.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FKuantumBS%2Fgrikod?ref=badge_shield)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FKuantumBS%2Fgrikod.svg?type=shield&issueType=security)](https://app.fossa.com/projects/git%2Bgithub.com%2FKuantumBS%2Fgrikod?ref=badge_shield&issueType=security)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FKuantumBS%2Fgrikod.svg?type=small)](https://app.fossa.com/projects/git%2Bgithub.com%2FKuantumBS%2Fgrikod?ref=badge_small)
[![Documentation Status](https://readthedocs.org/projects/grikod/badge/?version=main)](https://grikod.readthedocs.io/en/main/?badge=main)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.12731345.svg)](https://doi.org/10.5281/zenodo.12731345)

[![WorkflowHub DOI](https://img.shields.io/badge/DOI-10.48546%2Fworkflowhub.datafile.12.1-blue)](https://doi.org/10.48546/workflowhub.datafile.12.1)
[![WorkflowHub DOI](https://img.shields.io/badge/DOI-10.48546%2Fworkflowhub.datafile.12.2-blue)](https://doi.org/10.48546/workflowhub.datafile.12.2)

[![Anaconda-Server Badge](https://anaconda.org/bilgi/grikod/badges/version.svg)](https://anaconda.org/bilgi/grikod)
[![Anaconda-Server Badge](https://anaconda.org/bilgi/grikod/badges/latest_release_date.svg)](https://anaconda.org/bilgi/grikod)
[![Anaconda-Server Badge](https://anaconda.org/bilgi/grikod/badges/platforms.svg)](https://anaconda.org/bilgi/grikod)
[![Anaconda-Server Badge](https://anaconda.org/bilgi/grikod/badges/license.svg)](https://anaconda.org/bilgi/grikod)
[![Open Source](https://img.shields.io/badge/Open%20Source-Open%20Source-brightgreen.svg)](https://opensource.org/)
[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![Python CI](https://github.com/KuantumBS/grikod//actions/workflows/python_ci.yml/badge.svg?branch=main)](https://github.com/KuantumBS/grikod//actions/workflows/python_ci.yml)
[![codecov](https://codecov.io/gh/KuantumBS/grikod/graph/badge.svg?token=AQHUAMY4RJ)](https://codecov.io/gh/KuantumBS/grikod)
[![Documentation Status](https://readthedocs.org/projects/grikod/badge/?version=latest)](https://grikod.readthedocs.io/en/latest/)
[![Binder](https://terrarium.evidencepub.io/badge_logo.svg)](https://terrarium.evidencepub.io/v2/gh/KuantumBS/grikod/HEAD)
[![PyPI version](https://badge.fury.io/py/grikod.svg)](https://badge.fury.io/py/grikod)
[![PyPI Downloads](https://static.pepy.tech/badge/grikod)](https://pepy.tech/projects/grikod)
[![Linted with Ruff](https://img.shields.io/badge/Linted%20with-Ruff-green?logo=python&logoColor=white)](https://github.com/astral-sh/ruff)

---

<p align="left">
    <table>
        <tr>
            <td style="text-align: center;">PyPI</td>
            <td style="text-align: center;">
                <a href="https://pypi.org/project/grikod/">
                    <img src="https://badge.fury.io/py/grikod.svg" alt="PyPI version" height="18"/>
                </a>
            </td>
        </tr>
        <tr>
            <td style="text-align: center;">Conda</td>
            <td style="text-align: center;">
                <a href="https://anaconda.org/bilgi/grikod">
                    <img src="https://anaconda.org/bilgi/grikod/badges/version.svg" alt="conda-forge version" height="18"/>
                </a>
            </td>
        </tr>
        <tr>
            <td style="text-align: center;">DOI</td>
            <td style="text-align: center;">
                <a href="https://doi.org/10.5281/zenodo.12731345">
                    <img src="https://zenodo.org/badge/DOI/10.5281/zenodo.12731345.svg" alt="DOI" height="18"/>
                </a>
            </td>
        </tr>
        <tr>
            <td style="text-align: center;">License: MIT</td>
            <td style="text-align: center;">
                <a href="https://opensource.org/licenses/MIT">
                    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License" height="18"/>
                </a>
            </td>
        </tr>
    </table>
</p>

---

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
@software{kececi_2025_12731345,
  author       = {Keçeci, Mehmet},
  title        = {Grikod},
  month        = may,
  year         = 2025,
  publisher    = {GitHub, PYPI (Python Package Index, Python
                   Software Foundation), Anaconda, Zenodo
                  },
  doi          = {10.5281/zenodo.12731345},
  url          = {https://doi.org/10.5281/zenodo.12731345},
}
```

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
Keçeci, M. (2025). Grikod [Data set].  WorkflowHub. https://doi.org/10.48546/workflowhub.datafile.12.2

Keçeci, M. (2025). Grikod [Data set].  WorkflowHub. https://doi.org/10.48546/workflowhub.datafile.12.1

Keçeci, M. (2025). Grikod. Zenodo. https://doi.org/10.5281/zenodo.12731345

```

### Chicago

```
Keçeci, Mehmet. "Grikod" [Data set].  WorkflowHub, 2025. https://doi.org/10.48546/workflowhub.datafile.12.2

Keçeci, Mehmet. "Grikod" [Data set].  WorkflowHub, 2025. https://doi.org/10.48546/workflowhub.datafile.12.1

Keçeci, Mehmet. "Grikod". Zenodo, 06 Mayıs 2025. https://doi.org/10.5281/zenodo.12731345.

```


### Lisans (Türkçe) / License (English)

```
This project is licensed under the MIT License.
```
```
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FKuantumBS%2Fgrikod.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FKuantumBS%2Fgrikod?ref=badge_large)
```
```
[Grikod YouTube Video Linki](https://www.youtube.com/watch?v=IJnIpOuV92E)
```
