# Plex

Deploys [Plex Media Server](https://www.plex.tv/) - a service for media organization and streaming

## Usage

```yaml
---
- name: Deploy Plex
  hosts: all
  roles:
    - scalified.services.plex
```

## Variables

| Variable                       | Description                                       | Default Value                            |
|--------------------------------|---------------------------------------------------|------------------------------------------|
| `plex_dir`                     | Base directory for Plex installation              | `{{ services_dir }}/plex`                |
| `plex_owner`                   | Owner for Plex files and directories              | `{{ services_owner }}`                   |
| `plex_group`                   | Group for Plex files and directories              | `{{ services_group }}`                   |
| `plex_dir_mode`                | Permissions for Plex directories                  | `{{ services_dir_mode }}`                |
| `plex_file_mode`               | Permissions for Plex files                        | `{{ services_file_mode }}`               |
| `plex_version`                 | Plex Docker image version                         | `latest`                                 |
| `plex_container_name`          | Plex Docker container name                        | `plex`                                   |
| `plex_watchtower_enabled`      | Enable Watchtower for automatic container updates | `{{ services_watchtower_enabled }}`      |
| `plex_timezone`                | Timezone for Plex container                       | `{{ services_timezone }}`                |
| `plex_deploy_resources_limits` | Resource limits for Plex container                | `{"cpus": "2.0", "memory": "4G"}`        |
| `plex_volumes`                 | Additional volumes to mount                       | `[]`                                     |
| `plex_networks`                | Custom Docker networks to connect to              | `[]`                                     |
| `plex_bind_ip`                 | Bind IP address for port mapping                  | `{{ services_bind_ip }}`                 |
| `plex_ports`                   | Port mappings for Plex                            | See [Ports](#ports) section              |
| `plex_nginx_server_name`       | Nginx server name for reverse proxy configuration | `{{ plex_container_name }}.{{ domain }}` |

## Networks

**Plex** service can be connected to external **Docker** networks to enable communication with other containers.
These networks must be defined in the `plex_networks` variable:

```yaml
plex_networks:
  - nginx
```

> The networks listed in `plex_networks` must already exist before running the `plex` role

## Ports

**Plex** service exposes the following ports:

| Port    | Protocol | Description                      |
|---------|----------|----------------------------------|
| `32400` | TCP      | Plex Media Server                |
| `1900`  | UDP      | Plex DLNA Server                 |
| `32469` | TCP      | Plex DLNA Server                 |
| `8324`  | TCP      | Plex for Roku via Plex Companion |
| `32410` | UDP      | Plex GDM Network Discovery       |
| `32412` | UDP      | Plex GDM Network Discovery       |
| `32413` | UDP      | Plex GDM Network Discovery       |
| `32414` | UDP      | Plex GDM Network Discovery       |

Exposed ports must be defined in the `plex_ports` variable:

```yaml
plex_ports:
  - "{{ plex_bind_ip }}:32400:32400/tcp"
  - "{{ plex_bind_ip }}:1900:1900/udp"
  - "{{ plex_bind_ip }}:32469:32469/tcp"
  - "{{ plex_bind_ip }}:8324:8324/tcp"
  - "{{ plex_bind_ip }}:32410:32410/udp"
  - "{{ plex_bind_ip }}:32412:32412/udp"
  - "{{ plex_bind_ip }}:32413:32413/udp"
  - "{{ plex_bind_ip }}:32414:32414/udp"
```

> **Security Warning**: For security reasons, it is strongly advised against allowing these additional ports through the firewall or forwarding them in router, especially if the `Plex Media Server` is running on a machine with a public/WAN IP address. This applies to servers hosted in data centers and machines on a local network that have been placed in the DMZ (De-Militarized Zone) of the network router. This setup is not necessary for most users and should be avoided for better security

## Claim

**Plex** requires claiming a server to associate it with user account, which is essential for security, proper functioning, and device discovery.
If a claim is not provided via the `plex_claim` variable, the role attempts automatic claiming during the initial setup. For automatic claiming the following variables must be provided:

 * `plex_client_identifier`
 * `plex_token`

These values are taken from the `X-Plex-Client-Identifier` and `X-Plex-Token` HTTP request headers while the user is signed in at [https://app.plex.tv](https://app.plex.tv) (visible in browser developer tools).

If `plex_claim` is set it is used directly. Claim tokens expire quickly and should be used immediately after being generated

## Server Discovery

Since Plex operates inside a Docker container, the server advertises the container's internal IP address rather than the host's IP.
To ensure proper server discovery, the administrator must configure the following value in the `Plex Server Web UI` under `Settings` -> `Network` -> `Custom server access URLs`:

`https://<server-ip>:<server-port>`

where:

 * `server-ip` - the host machine IP address
 * `server-port` - the host port mapped to the Plex container port (`32400`)
