import os

COLLECTION_PREFIX = 'scalified.services.'


def select_path(role_name, role_path, playbook_dir):
    """
    Selects the appropriate path for role templates based on role name format.

    This filter helps determine the correct template path depending on whether
    the role is a fully qualified collection role or a local role.

    Args:
        role_name (str): The name of the role, may contain dots for collection roles
        role_path (str): The current role's path
        playbook_dir (str): The playbook directory path

    Returns:
        str: The selected path - role_path with prefix removed if role_name starts with 'scalified.services.',
             otherwise playbook_dir/roles/role_name (local role)

    Examples:
        # For collection roles with scalified.services prefix
        "scalified.services.nginx" | select_path(role_path, playbook_dir) -> role_path/nginx

        # For local roles (no dots)
        "nginx" | select_path(role_path, playbook_dir) -> playbook_dir/roles/nginx

    Note:
        This filter is particularly useful in scenarios where template paths need
        to be dynamically determined based on whether the role is part of an
        Ansible collection or a local role within the playbook structure.
    """
    if role_name.startswith(COLLECTION_PREFIX):
        return os.path.join(os.path.dirname(role_path), role_name.removeprefix(COLLECTION_PREFIX))
    else:
        return os.path.join(playbook_dir, 'roles', role_name)


class FilterModule(object):
    def filters(self):
        return {
            'select_path': select_path
        }
