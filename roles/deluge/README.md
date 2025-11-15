# Deluge

Deploys [Deluge](https://deluge-torrent.org/) - a lightweight, Free Software, cross-platform BitTorrent client

## Usage

```yaml
---
- name: Deploy Deluge
  hosts: all
  roles:
    - scalified.services.deluge
```

## Variables

| Variable                         | Description                                       | Default Value                                               |
|----------------------------------|---------------------------------------------------|-------------------------------------------------------------|
| `deluge_dir`                     | Base directory for Deluge installation            | `{{ services_dir }}/deluge`                                 |
| `deluge_config_dir`              | Deluge configuration directory                    | `{{ deluge_dir }}/config`                                   |
| `deluge_owner`                   | Owner for Deluge files and directories            | `{{ services_owner }}`                                      |
| `deluge_group`                   | Group for Deluge files and directories            | `{{ services_group }}`                                      |
| `deluge_dir_mode`                | Permissions for Deluge directories                | `{{ services_dir_mode }}`                                   |
| `deluge_file_mode`               | Permissions for Deluge files                      | `{{ services_file_mode }}`                                  |
| `deluge_version`                 | Deluge Docker image version                       | `latest`                                                    |
| `deluge_container_name`          | Deluge Docker container name                      | `deluge`                                                    |
| `deluge_watchtower_enabled`      | Enable Watchtower for automatic container updates | `{{ services_watchtower_enabled }}`                         |
| `deluge_timezone`                | Timezone for Deluge container                     | `{{ services_timezone }}`                                   |
| `deluge_deploy_resources_limits` | Resource limits for Deluge container              | `{"cpus": "2.0", "memory": "4G"}`                           |
| `deluge_volumes`                 | Additional volumes to mount                       | `[]`                                                        |
| `deluge_networks`                | Custom Docker networks to connect to              | `[]`                                                        |
| `deluge_web_port`                | Deluge web interface port                         | `8112`                                                      |
| `deluge_client_port`             | Deluge client port                                | `58846`                                                     |
| `deluge_bind_ip`                 | Bind IP address for port mapping                  | `{{ services_bind_ip }}`                                    |
| `deluge_ports`                   | Port mappings for Deluge                          | `["{{ deluge_client_port }}:{{ deluge_client_port }}/tcp"]` |
| `deluge_nginx_server_name`       | Nginx server name for reverse proxy configuration | `{{ deluge_container_name }}.{{ domain }}`                  |

## Networks

**Deluge** service can be connected to external **Docker** networks to enable communication with other containers.
These networks must be defined in the `deluge_networks` variable:

```yaml
deluge_networks:
  - nginx
```

> The networks listed in `deluge_networks` must already exist before running the `deluge` role

## Ports

**Deluge** service exposes the following ports:

| Port    | Protocol | Description            |
|---------|----------|------------------------|
| `8112`  | TCP      | Web UI                 |
| `58846` | TCP      | Client connection port |

Exposed ports must be defined in the `deluge_ports` variable:

```yaml
deluge_ports:
  - "{{ deluge_bind_ip }}:{{ deluge_web_port }}:{{ deluge_web_port }}/tcp"
  - "{{ deluge_bind_ip }}:{{ deluge_client_port }}:{{ deluge_client_port }}/tcp"
```

## Authentication

**Deluge** client authentication details are stored in the `auth` file located in the **Deluge** configuration directory defined in the `deluge_config_dir` variable

> Web UI default password is `deluge`
