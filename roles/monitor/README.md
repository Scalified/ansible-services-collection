# Monitor

Deploys **Monitor** service including **Grafana**, **Prometheus**, **cAdvisor**, and **Node Exporter**

## Usage

```yaml
---
- name: Deploy Monitor
  hosts: all
  roles:
    - scalified.services.monitor
```

## Variables

| Variable                                        | Description                                      | Default Value                       |
|-------------------------------------------------|--------------------------------------------------|-------------------------------------|
| `monitor_dir`                                   | Base directory for monitor deployment            | `{{ services_dir }}/monitor`        |
| `monitor_owner`                                 | File owner                                       | `{{ services_owner }}`              |
| `monitor_group`                                 | File group                                       | `{{ services_group }}`              |
| `monitor_dir_mode`                              | Directory permissions                            | `{{ services_dir_mode }}`           |
| `monitor_file_mode`                             | File permissions                                 | `{{ services_file_mode }}`          |
| `monitor_grafana_version`                       | Grafana Docker image version                     | `latest`                            |
| `monitor_grafana_container_name`                | Grafana container name                           | `monitor-grafana`                   |
| `monitor_grafana_watchtower_enabled`            | Enable Watchtower auto-updates for Grafana       | `{{ services_watchtower_enabled }}` |
| `monitor_grafana_user`                          | Grafana admin username                           | `admin`                             |
| `monitor_grafana_password`                      | Grafana admin password                           | `admin`                             |
| `monitor_grafana_slack_webhook_url`             | Slack webhook URL for Grafana alerts             | `""`                                |
| `monitor_grafana_deploy_resources_limits`       | Grafana container resource limits                | `{cpus: "0.50", memory: 1G}`        |
| `monitor_grafana_networks`                      | Additional Docker networks for Grafana           | `[]`                                |
| `monitor_prometheus_version`                    | Prometheus Docker image version                  | `latest`                            |
| `monitor_prometheus_container_name`             | Prometheus container name                        | `monitor-prometheus`                |
| `monitor_prometheus_watchtower_enabled`         | Enable Watchtower auto-updates for Prometheus    | `{{ services_watchtower_enabled }}` |
| `monitor_prometheus_deploy_resources_limits`    | Prometheus container resource limits             | `{cpus: "0.50", memory: 500M}`      |
| `monitor_prometheus_networks`                   | Additional Docker networks for Prometheus        | `[]`                                |
| `monitor_cadvisor_version`                      | cAdvisor Docker image version                    | `latest`                            |
| `monitor_cadvisor_container_name`               | cAdvisor container name                          | `monitor-cadvisor`                  |
| `monitor_cadvisor_watchtower_enabled`           | Enable Watchtower auto-updates for cAdvisor      | `{{ services_watchtower_enabled }}` |
| `monitor_cadvisor_deploy_resources_limits`      | cAdvisor container resource limits               | `{cpus: "0.50", memory: 128M}`      |
| `monitor_node_exporter_version`                 | Node Exporter Docker image version               | `latest`                            |
| `monitor_node_exporter_container_name`          | Node Exporter container name                     | `monitor-node-exporter`             |
| `monitor_node_exporter_watchtower_enabled`      | Enable Watchtower auto-updates for Node Exporter | `{{ services_watchtower_enabled }}` |
| `monitor_node_exporter_deploy_resources_limits` | Node Exporter container resource limits          | `{cpus: "0.50", memory: 128M}`      |

## Pre-configured Dashboards

The monitor role includes several pre-configured Grafana dashboards:

### Node Dashboards
- **Container Metrics**: Docker container resource usage and performance
- **Host Metrics**: System-level metrics (CPU, memory, disk, network)
- **Monitor Metrics**: Monitoring stack components health and performance

## Alerting

Grafana is pre-configured with alerting capabilities:
- **Alert Rules**: Defined in `grafana/provisioning/alerting/alert-rules.yaml`
- **Contact Points**: Configurable Slack webhook integration
- **Notification Policies**: Flexible routing and grouping of alerts

To enable Slack notifications, set the webhook URL:

```yaml
monitor_grafana_slack_webhook_url: "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"
```

## Storage

The monitoring stack uses Docker volumes for persistent storage:
- **grafana**: Grafana configuration and dashboards
- **prometheus**: Prometheus time-series data

## Security

Grafana admin credentials are configurable via `monitor_grafana_user` and `monitor_grafana_password` variables

## Networks

**Monitor** **Grafana** and **Prometheus** services can be connected to external **Docker** networks to enable communication with other containers.
These networks must be defined in the `monitor_grafana_networks` and `monitor_prometheus_networks` variables:

```yaml
monitor_grafana_networks:
  - nginx
monitor_prometheus_networks:
  - nut-ui
```

> The networks listed in `monitor_grafana_networks` and `monitor_prometheus_networks` must already exist before running the `nginx` role

## Configuration Files from Roles

Monitor configuration files from other roles can be included by listing the role names in the `monitor_conf_roles` variable:

```yaml
monitor_conf_roles:
  - appserver
  - scalified.services.nut_ui
```

> Configuration files should be placed in `roles/<role_name>/files/monitor/` directory for static files and `roles/<role_name>/templates/monitor/` directory for templates
