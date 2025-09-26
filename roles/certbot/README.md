# Certbot

Manages SSL certificates using Certbot with Cloudflare DNS challenge

## Usage

```yaml
---
- name: Setup SSL certificates with Certbot
  hosts: all
  roles:
    - scalified.services.certbot
```

## Variables

| Variable                     | Description                                       | Default Value                |
|------------------------------|---------------------------------------------------|------------------------------|
| `certbot_version`            | Certbot Docker image version                      | `latest`                     |
| `certbot_container_name`     | Docker container name for Certbot                 | `certbot`                    |
| `certbot_watchtower_enabled` | Enable Watchtower for automatic updates           | `true`                       |
| `certbot_domain`             | Primary domain for SSL certificate                | `{{ domain }}`               |
| `certbot_domains`            | List of domains to include in certificate         | `[domain, *.domain]`         |
| `certbot_dir`                | Directory for Certbot configuration               | `{{ services_dir }}/certbot` |
| `certbot_owner`              | Owner for Certbot files and directories           | `{{ services_owner }}`       |
| `certbot_group`              | Group for Certbot files and directories           | `{{ services_group }}`       |
| `certbot_dir_mode`           | Permissions for Certbot directories               | `{{ services_dir_mode }}`    |
| `certbot_file_mode`          | Permissions for Certbot files                     | `{{ services_file_mode }}`   |
| `certbot_cf_email`           | Cloudflare account email (required)               | *undefined*                  |
| `certbot_cf_api_token`       | Cloudflare API token for DNS challenge (required) | *undefined*                  |
| `certbot_deploy_hook`        | Deploy hook command to run after SSL update       | *undefined*                  |

## Required Variables

The following variables must be defined when using this role:

- `certbot_domain` or `domain` - The domain for SSL certificate
- `certbot_cf_email` - Cloudflare account email
- `certbot_cf_api_token` - Cloudflare API token with DNS edit permissions

## Cloudflare API Token

This role requires a Cloudflare API token with the following permissions:
- Zone:Zone:Read
- Zone:DNS:Edit

Create the token for the specific zone(s) where DNS records need to be managed for certificate validation

## Certificate Storage

Generated Let's Encrypt certificates are stored on the host system at:

- **Certificate Directory**: `/etc/letsencrypt/live/{{ certbot_domain }}/`
- **Full Certificate Chain**: `/etc/letsencrypt/live/{{ certbot_domain }}/fullchain.pem`
- **Private Key**: `/etc/letsencrypt/live/{{ certbot_domain }}/privkey.pem`
- **Certificate**: `/etc/letsencrypt/live/{{ certbot_domain }}/cert.pem`
- **Certificate Chain**: `/etc/letsencrypt/live/{{ certbot_domain }}/chain.pem`
