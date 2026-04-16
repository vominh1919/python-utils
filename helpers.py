#!/usr/bin/env python3
"""Helper functions for common tasks."""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def run_command(cmd: str, cwd: str = None) -> tuple:
    """Run shell command and return output."""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd)
    return result.returncode, result.stdout, result.stderr

def create_dir(path: str) -> None:
    """Create directory if not exists."""
    Path(path).mkdir(parents=True, exist_ok=True)

def copy_file(src: str, dst: str) -> None:
    """Copy file from src to dst."""
    shutil.copy2(src, dst)

def remove_file(path: str) -> None:
    """Remove file if exists."""
    if os.path.exists(path):
        os.remove(path)

def get_env(key: str, default: str = None) -> str:
    """Get environment variable."""
    return os.environ.get(key, default)

def is_windows() -> bool:
    """Check if running on Windows."""
    return sys.platform.startswith('win')

def is_linux() -> bool:
    """Check if running on Linux."""
    return sys.platform.startswith('linux')

def is_mac() -> bool:
    """Check if running on macOS."""
    return sys.platform == 'darwin'
