import argparse
import yaml
import os
from jinja2 import Environment, FileSystemLoader

def main():
    # 設定命令列參數
    parser = argparse.ArgumentParser(
        description="Generate Markdown pages for command cheat sheets from YAML data and templates.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generate_pages.py --data-file data/linux_system.yaml --template-dir templates --output-dir linux/system
  python generate_pages.py --data-file data/linux_process.yaml --output-dir linux/process
"""
    )
    parser.add_argument(
        "--data-file",
        required=True,
        help="Path to the YAML data file (e.g., data/linux_system.yaml). Required."
    )
    parser.add_argument(
        "--template-dir",
        default="templates",
        help="Directory containing template files (category_template.md.j2, command_template.md.j2). Default: templates"
    )
    parser.add_argument(
        "--output-dir",
        required=True,
        help="Output directory for generated Markdown files (e.g., linux/system). Required."
    )
    args = parser.parse_args()

    # 檢查 data-file 是否存在
    if not os.path.isfile(args.data_file):
        raise FileNotFoundError(f"YAML file not found: {args.data_file}")

    # 檢查 template-dir 是否存在
    if not os.path.isdir(args.template_dir):
        raise FileNotFoundError(f"Template directory not found: {args.template_dir}")

    # 載入模板環境
    env = Environment(loader=FileSystemLoader(args.template_dir))

    # 讀取 YAML 資料
    with open(args.data_file, "r") as f:
        data = yaml.safe_load(f)

    # 確保輸出目錄存在
    os.makedirs(args.output_dir, exist_ok=True)

    # 生成 Category Page (index.md)
    category_template = env.get_template("category_template.md.j2")
    category_content = category_template.render(
        category=data["category"],
        description=data["description"],
        commands=data["commands"]
    )
    index_path = os.path.join(args.output_dir, "index.md")
    with open(index_path, "w") as f:
        f.write(category_content)
    print(f"Generated {index_path}")

    # 生成 Command Pages
    command_template = env.get_template("command_template.md.j2")
    for command in data["commands"]:
        command_content = command_template.render(
            category=data["category"],
            command=command
        )
        command_path = os.path.join(args.output_dir, f"{command['name']}.md")
        with open(command_path, "w") as f:
            f.write(command_content)
        print(f"Generated {command_path}")

if __name__ == "__main__":
    main()