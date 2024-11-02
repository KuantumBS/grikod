# Grikod (Gri Kod, Gray Code)

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FKuantumBS%2Fgrikod.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FKuantumBS%2Fgrikod?ref=badge_shield)
[![Documentation Status](https://readthedocs.org/projects/grikod/badge/?version=main)](https://grikod.readthedocs.io/en/main/?badge=main)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.12731346.svg)](https://doi.org/10.5281/zenodo.12731346)

[![Anaconda-Server Badge](https://anaconda.org/bilgi/grikod/badges/version.svg)](https://anaconda.org/bilgi/grikod)
[![Anaconda-Server Badge](https://anaconda.org/bilgi/grikod/badges/latest_release_date.svg)](https://anaconda.org/bilgi/grikod)
[![Anaconda-Server Badge](https://anaconda.org/bilgi/grikod/badges/platforms.svg)](https://anaconda.org/bilgi/grikod)
[![Anaconda-Server Badge](https://anaconda.org/bilgi/grikod/badges/license.svg)](https://anaconda.org/bilgi/grikod)

## Tanım (Türkçe)

Gri Kod: İkili sayıları Gri Koda çevirir

## Description (English)

Grikod converts binary numbers to Gray Code.

![Gri Kod](https://i.imgur.com/6wpucpo.png)

---

## Kurulum (Türkçe) / Installation (English)

### Python ile Kurulum / Install with pip

```bash
pip install grikod -U

conda install bilgi::grikod -y

mamba install bilgi::grikod -y
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

---

## Cite this repository:

APA Style:

Keçeci, M. (2024). Gri Kod (Version 1.0.7) [Computer software]. https://pypi.org/project/grikod/

## References

Chicago Style:

Keçeci, Mehmet. “Grikod”. Anaconda, Inc., November 01, 2024. [https://zenodo.org/records/14029276](https://zenodo.org/records/14029276).

Keçeci, Mehmet. “Grikod”. Python Package Index, November 01, 2024. [https://zenodo.org/records/14029245](https://zenodo.org/records/14029245).

Keçeci, Mehmet. “Grikod”. Python Package Index, October 29, 2024. [https://doi.org/10.5281/zenodo.14004878](https://doi.org/10.5281/zenodo.14004878).

Keçeci, Mehmet. “Grikod”. Anaconda, Inc., October 29, 2024. [https://doi.org/10.5281/zenodo.14004846](https://doi.org/10.5281/zenodo.14004846).

Keçeci, Mehmet. “Grikod.” PYPI, February 18, 2024. [https://doi.org/10.5281/zenodo.12731346](https://doi.org/10.5281/zenodo.12731346).

## BibTeX

@software{Kececi_Gri_Kod_2024,

author = {Keçeci, Mehmet},

license = {MIT},

month = nov,

title = {{Gri Kod}},

url = {
https://pypi.org/project/grikod/
},

version = {1.0.7},

year = {2024}

}

---

## Lisans (Türkçe) / License (English)

Açık Kaynak: MIT, Apache License 2.0, GNU General Public License (GPL), GPLv3

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FKuantumBS%2Fgrikod.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FKuantumBS%2Fgrikod?ref=badge_large)

[Grikod YouTube Video Linki](https://www.youtube.com/watch?v=IJnIpOuV92E)
