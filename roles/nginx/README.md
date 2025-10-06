# Nginx

Deploys **Nginx** service as a Docker container with comprehensive configuration options

## Usage

```yaml
---
- name: Deploy Nginx
  hosts: all
  roles:
    - scalified.services.nginx
```

## Variables

| Variable                        | Description                           | Default Value                          |
|---------------------------------|---------------------------------------|----------------------------------------|
| `nginx_dir`                     | Base directory for Nginx deployment   | `{{ services_dir }}/nginx`             |
| `nginx_conf_dir`                | Configuration directory path          | `{{ nginx_dir }}/nginx/conf.d`         |
| `nginx_owner`                   | File owner                            | `{{ services_owner }}`                 |
| `nginx_group`                   | File group                            | `{{ services_group }}`                 |
| `nginx_dir_mode`                | Directory permissions                 | `{{ services_dir_mode }}`              |
| `nginx_file_mode`               | File permissions                      | `{{ services_file_mode }}`             |
| `nginx_version`                 | Nginx Docker image version            | `alpine`                               |
| `nginx_container_name`          | Docker container name                 | `nginx`                                |
| `nginx_watchtower_enabled`      | Enable Watchtower auto-updates        | `false`                                |
| `nginx_deploy_resources_limits` | Container resource limits             | `{cpus: "0.50", memory: 500M}`         |
| `nginx_ssl_keys_server_path`    | SSL private key path                  | `{{ services_ssl_keys_server_path }}`  |
| `nginx_ssl_certs_server_path`   | SSL certificate path                  | `{{ services_ssl_certs_server_path }}` |
| `nginx_volumes`                 | Additional volume mounts              | `[]`                                   |
| `nginx_networks`                | Custom Docker networks                | `[]`                                   |
| `nginx_bind_host`               | Host binding address                  | `{{ services_bind_host }}`             |
| `nginx_ports`                   | Port mappings                         | `["80:80/tcp", "443:443/tcp"]`         |
| `nginx_conf_roles`              | List of roles to include configs from | `[]`                                   |
| `nginx_conf_files`              | List of custom config template files  | `[]`                                   |
| `nginx_user`                    | Basic auth username                   | `admin`                                |
| `nginx_password`                | Basic auth password                   | `admin`                                |

## Configuration Files from Roles

Use `nginx_conf_roles` variable to include Nginx configurations from other roles:

```yaml
nginx_conf_roles:
  - appserver
  - monitoring
```

> Configuration files should be placed in `roles/<role_name>/templates/nginx/` directory

## Configuration Files

Use `nginx_conf_files` to specify custom Nginx configuration templates

```yaml
nginx_conf_files:
  - templates/appserver.conf
  - templates/monitoring.conf
```
