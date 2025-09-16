import os
from ansible.plugins.action import ActionBase
from ansible.utils.display import Display

display = Display()

class ActionModule(ActionBase):

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = {}

        result = dict(changed=False, results=[])

        src_root = self._task.args.get("src")
        dest_root = self._task.args.get("dest")
        directory_mode = self._task.args.get("directory_mode", None)
        owner = self._task.args.get("owner", None)
        group = self._task.args.get("group", None)

        if not src_root or not dest_root:
            return {"failed": True, "msg": "'src' and 'dest' are required"}

        if not os.path.isdir(self._loader.path_dwim(src_root)):
            return {"failed": True, "msg": f"src '{src_root}' must be a directory"}

        display.v(f"Template src_root: {src_root}, dest_root: {dest_root}")

        display.vv(f"Starting directory walk from: {self._loader.path_dwim(src_root)}")

        for root, _, files in os.walk(self._loader.path_dwim(src_root)):
            rel_root = os.path.relpath(root, self._loader.path_dwim(src_root))
            remote_dir = os.path.join(dest_root, rel_root) if rel_root != "." else dest_root

            display.vvv(f"Processing directory: {root}")
            display.vvv(f"Relative path: {rel_root}, Remote directory: {remote_dir}")

            file_task = self._task.copy()
            file_task.args = {
                "path": remote_dir,
                "state": "directory",
            }
            if directory_mode:
                file_task.args["mode"] = directory_mode
            if owner:
                file_task.args["owner"] = owner
            if group:
                file_task.args["group"] = group

            dir_res = self._execute_module(
                module_name="ansible.builtin.file",
                module_args={
                    "path": remote_dir,
                    "state": "directory",
                    "mode": directory_mode,
                },
                task_vars=task_vars
            )

            if dir_res.get("failed", False):
                return dir_res

            result["results"].append(dir_res)
            if dir_res.get("changed", False):
                result["changed"] = True
                display.v(f"Directory created/changed: {remote_dir}")

            display.vv(f"Found {len(files)} files in {root}")

            for file in files:
                src_file = os.path.join(root, file)
                rel_path = os.path.relpath(src_file, self._loader.path_dwim(src_root))
                dest_file = os.path.join(dest_root, rel_path)

                display.vvv(f"Processing file: {file}")
                display.vvv(f"Source: {src_file}, Destination: {dest_file}")

                template_task = self._task.copy()
                template_task.args = dict(self._task.args)
                template_task.args.update({
                    "src": src_file,
                    "dest": dest_file,
                })

                template_action = self._shared_loader_obj.action_loader.get(
                    "ansible.builtin.template",
                    task=template_task,
                    connection=self._connection,
                    play_context=self._play_context,
                    loader=self._loader,
                    templar=self._templar,
                    shared_loader_obj=self._shared_loader_obj,
                )

                template_res = template_action.run(tmp=tmp, task_vars=task_vars)

                if template_res.get("failed", False):
                    return template_res

                result["results"].append(template_res)
                if template_res.get("changed", False):
                    result["changed"] = True

        display.vv(f"Template action completed. Total results: {len(result['results'])}")
        display.v(f"Overall changed status: {result['changed']}")
        return result
