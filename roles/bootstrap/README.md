# Bootstrap

Performs services initialization

## Usage

```yaml
---
- name: Initialize services
  hosts: all
  roles:
    - scalified.services.bootstrap
```

## Variables

| Variable            | Description                              | Default Vaule           |
|---------------------|------------------------------------------|-------------------------|
| `services_dir`      | Base directory for services installation | `/opt`                  |
| `services_owner`    | Owner for services files and directories | `{{ ansible_user_id }}` |
| `services_group`    | Group for services files and directories | `root`                  |
| `services_dir_mode` | Permissions for services directories     | `"0770"`                |
| `services_file_mode`| Permissions for services files           | `"0660"`                |
