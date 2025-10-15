# Watchtower

Deploys **Watchtower** service for automating Docker container base image updates

## Usage

```yaml
---
- name: Deploy Watchtower
  hosts: all
  roles:
    - scalified.services.watchtower
```

## Variables

| Variable                             | Description                                   | Default Value                   |
|--------------------------------------|-----------------------------------------------|---------------------------------|
| `watchtower_dir`                     | Base directory for Watchtower deployment      | `{{ services_dir }}/watchtower` |
| `watchtower_owner`                   | Owner for Watchtower files and directories    | `{{ services_owner }}`          |
| `watchtower_group`                   | Group for Watchtower files and directories    | `{{ services_group }}`          |
| `watchtower_dir_mode`                | Permissions for Watchtower directories        | `{{ services_dir_mode }}`       |
| `watchtower_file_mode`               | Permissions for Watchtower files              | `{{ services_file_mode }}`      |
| `watchtower_version`                 | Watchtower Docker image version               | `latest`                        |
| `watchtower_container_name`          | Docker container name                         | `watchtower`                    |
| `watchtower_deploy_resources_limits` | Container resource limits                     | `{cpus: "0.50", memory: 500M}`  |
| `watchtower_timezone`                | Timezone for Watchtower                       | `{{ services_timezone }}`       |
| `watchtower_cleanup`                 | Remove old images after updating              | `true`                          |
| `watchtower_remove_volumes`          | Remove attached volumes before updating       | `true`                          |
| `watchtower_include_restarting`      | Monitor containers that are restarting        | `false`                         |
| `watchtower_include_stopped`         | Monitor stopped containers                    | `false`                         |
| `watchtower_revive_stopped`          | Start stopped containers after updating       | `false`                         |
| `watchtower_label_enable`            | Only monitor containers with specific labels  | `true`                          |
| `watchtower_disable_containers`      | Comma-separated list of containers to exclude | `""`                            |
| `watchtower_monitor_only`            | Only monitor for updates, don't update        | `false`                         |
| `watchtower_label_take_precedence`   | Labels take precedence over arguments         | `false`                         |
| `watchtower_no_restart`              | Don't restart containers after updating       | `false`                         |
| `watchtower_no_pull`                 | Don't pull new images                         | `false`                         |
| `watchtower_no_startup_message`      | Disable startup message                       | `true`                          |
| `watchtower_scope`                   | Limit monitoring to specific scope            | `""`                            |
| `watchtower_schedule`                | Cron schedule for update checks               | `"0 23 3 * * *"`                |
| `watchtower_rolling_restart`         | Restart containers one at a time              | `true`                          |
| `watchtower_timeout`                 | Timeout for container operations              | `10s`                           |
| `watchtower_notifications_hostname`  | Hostname for notifications                    | `{{ ansible_host }}`            |
| `watchtower_notification_url`        | Notification service URL (e.g., Slack, email) | `""`                            |

> See [**Watchtower** Arguments detailed information](https://containrrr.dev/watchtower/arguments)
