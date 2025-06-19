# Command Cheat Sheet

This repository hosts a collection of command cheat sheets, primarily for Linux commands, with consistent documentation for quick reference. Commands are organized by category, with details on usage, options, and examples, generated from YAML data using Jinja2 templates.

## Table of Contents

- Project Structure
- Generating Pages
- Contributing

## Project Structure

- `data/`: Stores YAML data files defining command categories and details (e.g., `linux_system.yaml`).
- `data/schema/`: Contains JSON Schema files (e.g., `command_category_schema.json`) for validating YAML data.
- `pages/`: Hosts generated Markdown pages for command cheat sheets. See **[pages/README.md](./pages/README.md)** for details.
- `templates/`: Contains Jinja2 templates for generating Markdown pages:
  - `category_template.md.j2`: For category pages (e.g., `index.md`).
  - `command_template.md.j2`: For individual command pages (e.g., `top.md`).
- `tools/`: Stores scripts for generating pages:
  - `generate_pages.py`: Python script to generate Markdown pages from YAML and templates.

## Generating Pages

To generate Markdown pages, use the `generate_pages.py` script in `tools/`. For usage details, refer to **[tools/README.md](./tools/README.md)**.

## Contributing

Contributions are welcome! To contribute:

- Fork the repository and submit a pull request.
- Add new commands or categories by updating YAML files in `data/`.
- Enhance templates in `templates/` for improved formatting.
- Report issues or suggest features via GitHub Issues.