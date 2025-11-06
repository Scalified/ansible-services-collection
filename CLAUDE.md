# CLAUDE.md

This file provides context and structure for Claude Code (claude.ai/code) to work effectively with this repository.

## Overview

This is an **Ansible Collection** for streamlined services, published as: `scalified.services`.

- Complies with **Ansible Galaxy** standards.
- Supports and is tested on systems with Docker installed.

## Development Commands

- `ansible-lint` — validates code style and Ansible best practices.
- `molecule test` — runs the full test suite.

> ⚠️ On Windows, use `wsl` to run these commands, e.g., `wsl ansible-lint`

## Repository Structure

- `roles/` — Role definitions (e.g., nginx, monitor)
- `extensions/molecule/default/` — Molecule test scenario configuration
- `galaxy.yml` — Ansible Galaxy metadata
- `.ansible-lint.yml` — Ansible Lint rules configuration

## Code Style & Conventions

* All files must end with a newline.
* Follow all ansible-lint rules:
    * Use **Fully Qualified Collection Names (FQCN)**.
    * Provide descriptive task names.
    * Variables names from within roles must use `<role>_` as a prefix.
* Use consistent **indentation**, **naming**, and **file structure** across all roles.
* Prefer **Ansible modules** over `ansible.builtin.shell` or `ansible.builtin.command`.
* Avoid `set_fact` unless required.
* Each role must include:
    * `README.md` — usage documentation, consistent format.
    * `meta/main.yml` — Galaxy metadata and role dependencies.

## Molecule Tests

* Run integration tests with: molecule test.
* Every file with logic must have a corresponding test file in: `extensions/molecule/default/roles/<role>/tasks/`
* Role-level verifications are placed in: `extensions/molecule/default/verify.yml`
* Use the following test files as templates:
    * `extensions/molecule/default/certbot/tasks/certbot.yml` — verify files and directories attributes and content.
