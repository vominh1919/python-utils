# Python Utils 🐍

100+ Python utility functions and helpers.

## Installation

```bash
pip install python-utils
```

## Usage

```python
from utils import read_file, write_file, md5_hash
from helpers import run_command, create_dir

# Read file
content = read_file("example.txt")

# Write file
write_file("output.txt", "Hello World")

# Hash text
hash_val = md5_hash("Hello World")

# Run command
code, stdout, stderr = run_command("ls -la")

# Create directory
create_dir("new_folder")
```

## Functions

### File Operations
- `read_file(path)` - Read file content
- `write_file(path, content)` - Write content to file
- `copy_file(src, dst)` - Copy file
- `remove_file(path)` - Remove file

### Data Processing
- `md5_hash(text)` - Generate MD5 hash
- `flatten_list(nested)` - Flatten nested list
- `chunk_list(lst, size)` - Split list into chunks
- `merge_dicts(*dicts)` - Merge dictionaries

### System Operations
- `run_command(cmd)` - Run shell command
- `create_dir(path)` - Create directory
- `get_env(key)` - Get environment variable
- `timestamp()` - Get current timestamp

## License

MIT
