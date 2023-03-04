# -*- coding: utf-8 -*-
# @Time    : 2023/3/5 0:14
# @Author  : Kenny Zhou
# @FileName: path_resolution_tools.py
# @Software: PyCharm
# @Email    ：l.w.r.f.42@gmail.com

"""Path resolution tools."""

from pathlib import Path

def get_path(path: str) -> Path:
    """Get path from the string."""
    return path(str)

if __name__ == '__main__':
    print(get_path(r'D:\github\FinancialCacheDatabase\utils\__init__.py'))
