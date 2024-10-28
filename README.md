# Grikod (Gri Kod, Gray Code)

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FKuantumBS%2Fgrikod.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FKuantumBS%2Fgrikod?ref=badge_shield)
[![Documentation Status](https://readthedocs.org/projects/grikod/badge/?version=main)](https://grikod.readthedocs.io/en/main/?badge=main)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.12731346.svg)](https://doi.org/10.5281/zenodo.12731346)

## Tanım (Türkçe)

Gri Kod: İkili sayıları Gri Koda çevirir

## Description (English)

Grikod converts binary numbers to Gray Code.

---

## Kurulum (Türkçe) / Installation (English)

### Python ile Kurulum / Install with pip

```bash
pip install grikod -U
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
import grikod

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
# Restart Kernel and Clear Outputs
```

---

## References

Keçeci, Mehmet. “Grikod.” Zenodo, February 18, 2024. [https://doi.org/10.5281/zenodo.12731346](https://doi.org/10.5281/zenodo.12731346)

---

## Lisans (Türkçe) / License (English)

Açık Kaynak: MIT, Apache License 2.0, GNU General Public License (GPL), GPLv3

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FKuantumBS%2Fgrikod.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FKuantumBS%2Fgrikod?ref=badge_large)
