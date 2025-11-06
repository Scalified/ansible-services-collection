# Ansible Services Collection

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build](https://github.com/Scalified/ansible-services-collection/actions/workflows/build.yml/badge.svg)](https://github.com/Scalified/ansible-services-collection/actions)
[![Release](https://img.shields.io/github/v/release/Scalified/ansible-services-collection?style=flat-square)](https://github.com/Scalified/ansible-services-collection/releases/latest)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-scalified.services-blue.svg)](https://galaxy.ansible.com/scalified/services)

Ansible collection providing streamlined services setup

## Requirements

- **Ansible:** >= 2.16.0
- **Python:** >= 3.6
- **Docker** >= 3.4

> Package cache must be updated before running any services role

## Installation

### Ansible Galaxy

```bash
ansible-galaxy collection install scalified.services
```

### Git Repository

```bash
ansible-galaxy collection install git+https://github.com/scalified/ansible-services-collection.git
```

### Requirements File

`requirements.yml`:

```yaml
---
collections:
  - name: scalified.services
```

```bash
ansible-galaxy collection install -r requirements.yml
```

## Roles

* [Bootstrap](roles/bootstrap/README.md)
* [Certbot](roles/certbot/README.md)
* [Nginx](roles/nginx/README.md)
* [Watchtower](roles/watchtower/README.md)
* [NUT UI](roles/nut_ui/README.md)
* [Monitor](roles/monitor/README.md)

---

**Made with ❤️ by [Scalified](http://www.scalified.com)**
