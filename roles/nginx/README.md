# Nginx

Deploys **Nginx** service - an HTTP web server, reverse proxy, content cache, and load balancer

## Usage

```yaml
---
- name: Deploy Nginx
  hosts: all
  roles:
    - scalified.services.nginx
```

## Handlers

**Reload:** after configuration changes

```yaml
- name: Copy configuration file
  ansible.builtin.copy:
    src: appserver.conf
    dest: "{{ nginx_conf_dir }}"
  notify: "nginx : reload"
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
| `nginx_bind_ip`                 | Bind IP address for port mapping      | `{{ services_bind_ip }}`               |
| `nginx_ports`                   | Port mappings                         | `["80:80/tcp", "443:443/tcp"]`         |
| `nginx_conf_roles`              | List of roles to include configs from | `[]`                                   |
| `nginx_conf_files`              | List of custom config template files  | `[]`                                   |
| `nginx_user`                    | Basic auth username                   | `admin`                                |
| `nginx_password`                | Basic auth password                   | `admin`                                |

## Networks

**Nginx** service can be connected to external **Docker** networks to enable communication with other containers.
These networks must be defined in the `nginx_networks` variable:

```yaml
nginx_networks:
  - default
  - frontend
  - backend
```

> The networks listed in `nginx_networks` must already exist before running the `nginx` role

## Ports

**Nginx** service exposes the following ports:

| Port  | Protocol | Description |
|-------|----------|-------------|
| `80`  | TCP      | HTTP        |
| `443` | TCP      | HTTPS       |

Exposed ports must be defined in the `nginx_ports` variable:

```yaml
nginx_ports:
  - "80:80/tcp"
  - "443:443/tcp"
```

## Snippets

Reusable configuration snippets can be included into the Nginx server or location blocks for common features

### Basic Authentication

The `auth_basic.conf` snippet enables HTTP Basic Authentication using the `/etc/nginx/conf.d/.htpasswd` file.

To use the snippet, include it in a server block:

```nginx
server {
    listen 80;
    server_name example.com;

    include /etc/nginx/conf.d/auth_basic.conf;

    # ...other configuration...
}
```

## Configuration Files from Roles

Nginx configuration files from other roles can be included by listing the role names in the `nginx_conf_roles` variable:

```yaml
nginx_conf_roles:
  - appserver
  - scalified.services.monitor
```

> Configuration files should be placed in `roles/<role_name>/templates/nginx/` directory

## Configuration Files

Nginx configuration templates can be included by listing their paths in the `nginx_conf_files` variable:

```yaml
nginx_conf_files:
  - templates/appserver.conf
```
