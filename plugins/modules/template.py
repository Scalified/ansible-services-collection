# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Vladyslav Baidak <vld.x@hotmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: template
short_description: Template a directory of files recursively
description:
  - This action plugin templates all files in a source directory recursively to a destination directory.
  - It creates the destination directory structure as needed.
  - It uses the ansible.builtin.template action for individual files.
  - It uses the ansible.builtin.file module to create directories.
version_added: "1.0.0"
options:
  src:
    description:
      - Path to the source directory containing template files.
      - This directory will be walked recursively.
      - Can be an absolute path or relative path.
      - Relative paths are resolved relative to the role's templates directory (if in a role)
        or playbook templates directory, similar to ansible.builtin.template.
    required: true
    type: path
  dest:
    description:
      - Path to the destination directory where templated files will be placed.
      - The directory structure will be preserved from the source.
    required: true
    type: path
  directory_mode:
    description:
      - Mode to set for directories created during templating.
      - If not specified, directories will be created with default permissions.
      - Refer to the ansible.builtin.template action plugin for more information about mode.
    required: false
    type: raw
  owner:
    description:
      - Owner to set for directories created during templating.
      - If not specified, directories will be created with default ownership.
    required: false
    type: str
  group:
    description:
      - Group to set for directories created during templating.
      - If not specified, directories will be created with default group ownership.
    required: false
    type: str
seealso:
  - module: ansible.builtin.template
author:
  - Vladyslav Baidak (@scalified)
'''

EXAMPLES = r'''
- name: Template entire directory structure
  scalified.services.template:
    src: templates/config/
    dest: /etc/myapp/
    directory_mode: '0755'
    owner: root
    group: root

- name: Template directory with default permissions
  scalified.services.template:
    src: templates/www/
    dest: /var/www/html/
'''

RETURN = r'''
changed:
  description: Whether any files or directories were changed.
  returned: always
  type: bool
  sample: true
results:
  description: List of results from individual file and directory operations.
  returned: always
  type: list
  sample: [{"changed": true, "path": "/etc/myapp/config.conf"}]
'''
