# Create Python Project with uv

To create a python project using uv:
```
# create default project name (default python version following default python in the OS)
uv init <name>

# create default project name with specific python version
uv init <name> --python 3.12

Example:
uv init demo1 --python 3.12
```
If it create successfully, the output will likes:
```
Initialized project `demo1` at `/home/toms/demo1`
```

Change to folder demo1:
```
cd demo1
```
It will create default 3 files.
```
main.py  pyproject.toml  README.md
```
At this step, the virtual environment (venv) is not yet created.

## Create & Activate venv
Run `uv sync` to create/update the venv:
```
uv sync
```
The output will likes:
```
Using CPython 3.12.12
Creating virtual environment at: .venv
Resolved 1 package in 12ms
Audited in 0.00ms
```

To activate the venv:
```
source .venv/bin/activate
```

To deactivate the venv:
```
deactivate
```

## Add dependencies
To add dependencies lib use `uv add'
```
# Add pandas and matplotlib
uv add pandas matplotlib
```
Output:
```
esolved 15 packages in 128ms
Installed 14 packages in 55ms
 + contourpy==1.3.3
 + cycler==0.12.1
 + fonttools==4.60.1
 + kiwisolver==1.4.9
 + matplotlib==3.10.7
 + numpy==2.3.4
 + packaging==25.0
 + pandas==2.3.3
 + pillow==12.0.0
 + pyparsing==3.2.5
 + python-dateutil==2.9.0.post0
 + pytz==2025.2
 + six==1.17.0
 + tzdata==2025.2

```
It automatically update dependencies in the pyproject.toml 
```
[project]
name = "demo1"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "matplotlib>=3.10.7",
    "pandas>=2.3.3",
]
```




