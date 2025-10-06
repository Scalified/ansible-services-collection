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

| Variable                         | Description                                       | Default Value                                                 |
|----------------------------------|---------------------------------------------------|---------------------------------------------------------------|
| `services_dir`                   | Base directory for services installation          | `/opt`                                                        |
| `services_owner`                 | Owner for services files and directories          | `{{ ansible_user_id }}`                                       |
| `services_group`                 | Group for services files and directories          | `root`                                                        |
| `services_dir_mode`              | Permissions for services directories              | `"0770"`                                                      |
| `services_file_mode`             | Permissions for services files                    | `"0660"`                                                      |
| `services_watchtower_enabled`    | Enable Watchtower for automatic container updates | `true`                                                        |
| `services_ssl_domain`            | SSL domain name                                   | `{{ domain }}`                                                |
| `services_ssl_dir`               | SSL certificates directory                        | `/etc/letsencrypt/live/{{ services_ssl_domain }}`             |
| `services_ssl_certs_server_name` | SSL certificate filename                          | `fullchain.pem`                                               |
| `services_ssl_keys_server_name`  | SSL private key filename                          | `privkey.pem`                                                 |
| `services_ssl_certs_server_path` | Full path to SSL certificate                      | `{{ services_ssl_dir }}/{{ services_ssl_certs_server_name }}` |
| `services_ssl_keys_server_path`  | Full path to SSL private key                      | `{{ services_ssl_dir }}/{{ services_ssl_keys_server_name }}`  |
| `services_bind_host`             | Bind host for services port mapping               | `""`                                                          |
