# Tools Documentation

This directory contains scripts for generating Markdown pages for the Command Cheat Sheet project, which organizes Linux commands into structured documentation using YAML data and Jinja2 templates. The recommended approach is to use `generate_pages.sh` within a Python virtual environment (venv) to ensure dependency isolation.

## Table of Contents

- Scripts Overview
- Requirements Installation
- Virtual Environment Setup
- External References

## Scripts Overview

### generate_pages.sh (Recommended)

A shell script that prompts for a YAML data file and runs `generate_pages.py` to generate Markdown pages, outputting to `out/<yaml_filename>/`.

**Usage**:

```bash
chmod +x generate_pages.sh
./generate_pages.sh
```

**Steps**:

1. Run the script and enter the YAML file path when prompted (e.g., `../data/linux_system.yaml`).
2. The script generates Markdown files in `out/<yaml_filename>/` (e.g., `out/linux_system/`).

**Example**:

```bash
./generate_pages.sh
# Input: ../data/linux_system.yaml
```

Output: Markdown files in `out/linux_system/` (e.g., `index.md`, `top.md`).

### generate_pages.py

A Python script that generates Markdown pages from YAML data and Jinja2 templates. Use `generate_pages.sh` for a simpler interface, but this script can be run directly for advanced control.

**Usage**:

```bash
python3 generate_pages.py --data-file <yaml_file> --template-dir <template_dir> --output-dir <output_dir>
```

**Parameters**:

- `--data-file`: Path to the YAML data file (required, e.g., `../data/linux_system.yaml`).
- `--template-dir`: Directory containing Jinja2 templates (`category_template.md.j2`, `command_template.md.j2`). Default: `../templates`.
- `--output-dir`: Directory for generated Markdown files (required, e.g., `out/linux_system`).

**Example**:

```bash
python3 generate_pages.py --data-file ../data/linux_system.yaml --template-dir ../templates --output-dir out/linux_system
```

## Requirements Installation

The scripts require Python packages listed in `requirements.txt`. Install them within a virtual environment (see below).

**Install dependencies**:

```bash
pip install -r requirements.txt
```

**requirements.txt**:

```
PyYAML==6.0.2
Jinja2==3.1.4
```

## Virtual Environment Setup

We strongly recommend using a Python virtual environment (venv) to isolate dependencies and avoid conflicts with system-wide packages.

**Create and activate a virtual environment**:

```bash
# Create a virtual environment in the project root
python3 -m venv ./venv

# Activate on Linux/macOS
source ./venv/bin/activate

# Activate on Windows
./venv\Scripts\activate
```

**Install dependencies in the virtual environment**:

```bash
pip install -r requirements.txt
```

**Run scripts in the virtual environment**:

```bash
./generate_pages.sh
# or
python3 generate_pages.py --data-file ../data/linux_system.yaml --template-dir ../templates --output-dir out/linux_system
```

**Deactivate the virtual environment**:

```bash
deactivate
```

## External References

- PyYAML Documentation: Guide for YAML parsing in Python.
- Jinja2 Documentation: Reference for Jinja2 templating.
- Python Virtual Environments: Official guide for `venv`.
- Command Cheat Sheet Project README: Main project overview.