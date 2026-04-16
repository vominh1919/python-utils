#!/usr/bin/env python3
"""Python utility functions."""

import os
import sys
import json
import hashlib
from typing import Any, Dict, List, Optional
from datetime import datetime

def read_file(path: str) -> str:
    """Read file content."""
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path: str, content: str) -> None:
    """Write content to file."""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def md5_hash(text: str) -> str:
    """Generate MD5 hash."""
    return hashlib.md5(text.encode()).hexdigest()

def flatten_list(nested: List) -> List:
    """Flatten nested list."""
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

def chunk_list(lst: List, size: int) -> List[List]:
    """Split list into chunks."""
    return [lst[i:i + size] for i in range(0, len(lst), size)]

def merge_dicts(*dicts: Dict) -> Dict:
    """Merge multiple dictionaries."""
    result = {}
    for d in dicts:
        result.update(d)
    return result

def timestamp() -> str:
    """Get current timestamp."""
    return datetime.now().isoformat()

if __name__ == "__main__":
    print("Python Utilities loaded!")
