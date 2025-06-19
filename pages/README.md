# Command Cheat Sheet

Welcome to the Command Cheat Sheet! This is a collection of commonly used command-line tools and commands, designed to help developers quickly reference and learn commands. The Cheat Sheet is organized by categories, covering Linux commands, programming language commands, tools, databases, and cloud-related commands. Each category will have its own dedicated page with detailed command lists and examples.

## Index

### Linux Commands
Linux commands are subdivided by function, covering system management, file operations, networking, and utilities.

- **[File](./linux/file.md)**: File and directory operation commands
  - `find`, `ls`, `cp`, `mv`, `rm`, `tar`
- **[Network](./linux/network.md)**: Network-related commands
  - `curl`, `wget`, `ping`, `netstat`, `nslookup`, `dig`
- **[User](./linux/user.md)**: User account, group, permission, and password policy management commands
  - `useradd`, `passwd`, `sudo`, `chage`
- **[System](./linux/system/index.md)**: System monitoring and management commands
  - `top`, `htop`, `df`, `du`, `free`, `systemctl`
- **[Process](./linux/process.md)**: Process management commands
  - `ps`, `kill`, `nice`, `jobs`
- **[Utilities](./linux/utilities.md)**: General-purpose utility commands for text processing and data manipulation
  - `grep`, `awk`, `sed`, `sort`

### Programming Language Commands
Commands related to programming languages, covering development, building, and package management.

- **[Python](./programming/python.md)**: Python development and package management
  - `python`, `pip`, `venv`, `pytest`
- **[Ruby](./programming/ruby.md)**: Ruby development and package management
  - `ruby`, `gem`, `bundle`, `rake`
- **[Go](./programming/go.md)**: Go language build and module management
  - `go`, `go mod`, `go build`, `go test`
- **[Java](./programming/java.md)**: Java compilation and execution
  - `java`, `javac`, `jar`, `mvn`
- **[Kotlin](./programming/kotlin.md)**: Kotlin compilation and execution
  - `kotlinc`, `kotlin`, `gradle`
- **[Android](./programming/android.md)**: Android development commands
  - `adb`, `gradlew`, `aapt`, `dexdump`

### Tool Commands
Commands for popular development and operations tools, covering containerization, orchestration, and automation.

- **[Docker](./tools/docker.md)**: Container management and building
  - `docker run`, `docker build`, `docker-compose`, `docker ps`
- **[Kubernetes](./tools/kubernetes.md)**: Container orchestration and management
  - `kubectl get`, `kubectl apply`, `kubectl describe`, `kubectl logs`
- **[Ansible](./tools/ansible.md)**: Automation and configuration management
  - `ansible`, `ansible-playbook`, `ansible-vault`, `ansible-galaxy`

### Database Commands
Commands for managing and interacting with databases.

- **[MySQL](./databases/mysql.md)**: MySQL database management
  - `mysql`, `mysqldump`, `mysqladmin`, `mysqlimport`
- **[PostgreSQL](./databases/postgresql.md)**: PostgreSQL database management
  - `psql`, `pg_dump`, `pg_restore`, `createdb`
- **[SQLite](./databases/sqlite.md)**: SQLite lightweight database management
  - `sqlite3`, `.schema`, `.dump`

### Cloud Commands
Commands for interacting with cloud platforms.

- **[AWS CLI](./cloud/aws.md)**: Amazon Web Services command-line interface
  - `aws s3`, `aws ec2`, `aws configure`, `aws lambda`
- **[Google Cloud SDK](./cloud/gcloud.md)**: Google Cloud command-line tools
  - `gcloud compute`, `gcloud auth`, `gcloud storage`, `gcloud functions`
- **[Azure CLI](./cloud/azure.md)**: Microsoft Azure command-line interface
  - `az vm`, `az login`, `az storage`, `az group`

## Future Expansion (TODO List)
To make this Cheat Sheet more comprehensive and user-friendly, we plan to:
- Add multilingual support (e.g., separate English and Chinese versions).
- Convert the Cheat Sheet into a static website using GitHub Pages, MkDocs, or Docsify.
- Implement a search function for easier command lookup (e.g., Docsify search plugin).
- Create a contribution template for GitHub Issues to streamline community submissions.

## Contribution Guidelines
We welcome contributions from the community! To contribute:
1. Fork this repository.
2. Create or update Markdown files in the appropriate subdirectory (e.g., `linux/`, `programming/`).
3. Submit a Pull Request with a description of your changes.

## License
This project is licensed under the [MIT License](LICENSE).
