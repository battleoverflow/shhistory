# Shhistory
Simple Python library to return your shell history or dump to a JSON file.

You can install this library via pip:
```bash
pip install shhistory
```

## Example
A quick example to print the JSON data to stdout:
```python
# test.py
from shhistory import ShellHistory

print(ShellHistory.get_shell_history())
```

You can also create a quick bash utility with this library by piping to `jq` for nicer formatting:
```bash
python3 test.py | jq
```

If you would like to analyze the data more securely, you can also dump to a file:
```python
from shhistory import ShellHistory

print(ShellHistory.dump_shell_history())
```

NOTE: Windows is not currently supported. This may be added in a future update.