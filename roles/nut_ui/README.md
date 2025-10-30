# NUT UI

Deploys **NUT (Network UPS Tools)** UI services for monitoring UPS devices:

1. **NUT CGI** (`scalified/nut-cgi`) - Classic CGI web interface that is part of the NUT package
2. **NUT Web UI** (`ghcr.io/superioone/nut_webgui`) - Modern web-based GUI for UPS monitoring
3. **NUT Exporter** (`druggeri/nut_exporter`) - Prometheus metrics exporter for NUT

## Usage

```yaml
---
- name: Deploy NUT UI
  hosts: all
  roles:
    - scalified.services.nut_ui
```

## Variables

| Variable                                  | Description                               | Default Value                                                                                      |
|-------------------------------------------|-------------------------------------------|----------------------------------------------------------------------------------------------------|
| `nut_ui_dir`                              | Base directory for NUT UI deployment      | `{{ services_dir }}/nut-ui`                                                                        |
| `nut_ui_owner`                            | File owner                                | `{{ services_owner }}`                                                                             |
| `nut_ui_group`                            | File group                                | `{{ services_group }}`                                                                             |
| `nut_ui_dir_mode`                         | Directory permissions                     | `{{ services_dir_mode }}`                                                                          |
| `nut_ui_file_mode`                        | File permissions                          | `{{ services_file_mode }}`                                                                         |
| `nut_ui_cgi_version`                      | NUT CGI Docker image version              | `latest`                                                                                           |
| `nut_ui_cgi_container_name`               | Docker container name for CGI service     | `nut-ui-cgi`                                                                                       |
| `nut_ui_cgi_watchtower_enabled`           | Enable Watchtower auto-updates            | `{{ services_watchtower_enabled }}`                                                                |
| `nut_ui_cgi_admin_email`                  | Administrator email for CGI interface     | `{{ services_email }}`                                                                             |
| `nut_ui_cgi_monitor_hosts`                | UPS hosts to monitor                      | `{{ nut_ups_name \| upper }}:{{ nut_ups_name }}@{{ ansible_hostname }}:{{ nut_upsd_listen_port }}` |
| `nut_ui_cgi_deploy_resources_limits`      | Container resource limits for CGI service | `{cpus: "0.50", memory: 500M}`                                                                     |
| `nut_ui_version`                          | NUT Web UI Docker image version           | `latest`                                                                                           |
| `nut_ui_container_name`                   | Docker container name for Web UI          | `nut-ui`                                                                                           |
| `nut_ui_watchtower_enabled`               | Enable Watchtower auto-updates            | `{{ services_watchtower_enabled }}`                                                                |
| `nut_ui_upsd_address`                     | UPS daemon server address                 | `{{ ansible_hostname }}`                                                                           |
| `nut_ui_upsd_port`                        | UPS daemon server port                    | `{{ nut_upsd_listen_port }}`                                                                       |
| `nut_ui_upsd_user`                        | UPS daemon username                       | `{{ nut_users_admin_name }}`                                                                       |
| `nut_ui_upsd_password`                    | UPS daemon password                       | `{{ nut_users_admin_password }}`                                                                   |
| `nut_ui_deploy_resources_limits`          | Container resource limits for Web UI      | `{cpus: "0.50", memory: 500M}`                                                                     |
| `nut_ui_exporter_version`                 | NUT Exporter Docker image version         | `latest`                                                                                           |
| `nut_ui_exporter_container_name`          | Docker container name for exporter        | `nut-exporter`                                                                                     |
| `nut_ui_exporter_server`                  | NUT server address for exporter           | `{{ ansible_hostname }}`                                                                           |
| `nut_ui_exporter_port`                    | NUT server port for exporter              | `{{ nut_upsd_listen_port }}`                                                                       |
| `nut_ui_exporter_username`                | NUT server username for exporter          | `{{ nut_users_monitor_name }}`                                                                     |
| `nut_ui_exporter_password`                | NUT server password for exporter          | `{{ nut_users_monitor_password }}`                                                                 |
| `nut_ui_exporter_variables`               | List of UPS variables to export           | See [NUT Exporter Variables](#nut-exporter-variables)                                              |
| `nut_ui_exporter_deploy_resources_limits` | Container resource limits for exporter    | `{cpus: "0.50", memory: 500M}`                                                                     |
| `nut_ui_network`                          | Docker network configuration              | `{name: nut-ui, address: 192.168.153.0/24, interface_name: "br-{{ nut_ui_network.name }}"}`        |
| `nut_ui_networks`                         | Additional custom Docker networks         | `[]`                                                                                               |

## NUT Variables

The `scalified.services.nut_ui` role is designed to work in conjunction with the `scalified.setup.nut` role.
While it doesn't directly depend on it, this role uses variables that are defined by the `scalified.setup.nut` role to establish proper connectivity with the NUT daemon.

It is recommended to run the `scalified.setup.nut` role first to configure the NUT daemon and define its variables.
This allows `scalified.services.nut_ui` to automatically reuse these values for seamless integration.

The following variables from `scalified.setup.nut` are referenced in the default values of this role:

| Variable                     | Description                   | Example Value |
|------------------------------|-------------------------------|---------------|
| `nut_ups_name`               | Name of the UPS device        | `myups`       |
| `nut_upsd_listen_port`       | Port where NUT daemon listens | `3493`        |
| `nut_users_admin_name`       | NUT admin user name           | `admin`       |
| `nut_users_admin_password`   | NUT admin user password       | `secretpass`  |
| `nut_users_monitor_name`     | NUT monitor user name         | `monitor`     |
| `nut_users_monitor_password` | NUT monitor user password     | `monitorpass` |

> Without these variables defined, `nut_ui_*` variables that depend on them in their default values must be set manually to ensure proper connectivity to the NUT daemon

## Nginx Configuration

The role provides an **Nginx** [`nut-ui.conf`](templates/nginx/nut-ui.conf) configuraiton file that defines:

* **Basic authentication** to ensure secure access
* A route for `/`, serving the modern **NUT Web UI**
* A route for `/cgi`, serving the classic **NUT CGI interface**

## Grafana Configuration

The role provides **Grafana** [`grafana/`](files/monitor/grafana/) configuration files including dashboards and alert rules for UPS monitoring

### Dashboard

- Pre-configured UPS monitoring dashboard with device info, status, load, power, battery, and input/output metrics
- Real-time gauges and time series charts for all UPS parameters
- Color-coded status indicators and threshold warnings

### Alerting

- Predefined alert rules monitoring critical UPS conditions:
  - UPS status changes
  - High load and power consumption
  - Low battery charge levels
  - Input voltage anomalies
  - Output voltage outside safe range
- Alerts configured for notifications

## NUT Exporter

**NUT Exporter** collects UPS metrics from the NUT daemon and exposes them in a format suitable for **Prometheus** monitoring

The role provides **NUT Exporter** [`nut-exporter.yml`](templates/monitor/prometheus/nut-exporter.yml) configuration file for **Prometheus**

### NUT Exporter Variables

The following variables define the key UPS metrics that the NUT Exporter provides for monitoring:

| Variable                   | Description                          |
|----------------------------|--------------------------------------|
| `battery.charge`           | Current battery charge percentage    |
| `battery.charge.low`       | Low battery charge threshold         |
| `battery.runtime`          | Estimated battery runtime in seconds |
| `battery.voltage`          | Current battery voltage              |
| `battery.voltage.nominal`  | Nominal battery voltage              |
| `input.frequency`          | Input line frequency                 |
| `input.transfer.high`      | High voltage transfer point          |
| `input.transfer.low`       | Low voltage transfer point           |
| `input.voltage`            | Input voltage                        |
| `input.voltage.nominal`    | Nominal input voltage                |
| `output.frequency`         | Output frequency                     |
| `output.frequency.nominal` | Nominal output frequency             |
| `output.voltage`           | Output voltage                       |
| `output.voltage.nominal`   | Nominal output voltage               |
| `ups.beeper.status`        | UPS beeper status                    |
| `ups.load`                 | UPS load percentage                  |
| `ups.power`                | Current power consumption in watts   |
| `ups.power.nominal`        | Nominal power rating in watts        |
| `ups.status`               | Overall UPS status                   |
