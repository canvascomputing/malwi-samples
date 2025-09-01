class POV_OT_update_addon(bpy.types.Operator):
    """Update this addon to the latest version"""

    bl_idname = "pov.update_addon"
    bl_label = "Update POV addon"

    def execute(self, context):
        import os
        import shutil
        import tempfile
        import urllib.error
        import urllib.request
        import zipfile

    def recursive_overwrite(self, src, dest, ignore=None):
        """Update the script automatically (along with other addons).

        Arguments:
            src -- path where to update from
            dest -- storing temporary download here
        Keyword Arguments:
            ignore -- leave some directories alone (default: {None})

        Returns:
            finished flag for operator which is a set()
        """
        if os.path.isdir(src):
            if not os.path.isdir(dest):
                os.makedirs(dest)
            files = os.listdir(src)
            ignored = ignore(src, files) if ignore is not None else set()
            unignored_files = (fle for fle in files if fle not in ignored)
            for f in unignored_files:
                source = os.path.join(src, f)
                destination = os.path.join(dest, f)
                recursive_overwrite(source, destination, ignore)
        else:
            shutil.copyfile(src, dest)

        print("-" * 20)
        print("Updating POV addon...")

        with tempfile.TemporaryDirectory() as temp_dir_path:
            temp_zip_path = os.path.join(temp_dir_path, "master.zip")

            # Download zip archive of latest addons master branch commit
            # More work needed so we also get files from the shared addons presets /pov folder
            # switch this URL back to the BF hosted one as soon as gitweb snapshot gets fixed
            url = "https://github.com/blender/blender-addons/archive/refs/heads/master.zip"
            try:
                print("Downloading", url)

                with urllib.request.urlopen(url, timeout=60) as url_handle, open(
                    temp_zip_path, "wb"
                ) as file_handle:
                    file_handle.write(url_handle.read())
            except urllib.error.URLError as err:
                self.report({"ERROR"}, "Could not download: %s" % err)

            # Extract the zip
            print("Extracting ZIP archive")
            with zipfile.ZipFile(temp_zip_path) as zip_archive:
                pov_addon_pkg = (member for member in zip_archive.namelist() if
                                  "blender-addons-master/render_povray" in member)
                for member in pov_addon_pkg:
                    # Remove the first directory and the filename
                    # e.g. blender-addons-master/render_povray/nodes.py
                    # becomes render_povray/nodes.py
                    target_path = os.path.join(
                        temp_dir_path, os.path.join(*member.split("/")[1:-1])
                    )

                    filename = os.path.basename(member)
                    # Skip directories
                    if not filename:
                        continue

                    # Create the target directory if necessary
                    if not os.path.exists(target_path):
                        os.makedirs(target_path)

                    source = zip_archive.open(member)
                    target = open(os.path.join(target_path, filename), "wb")

                    with source, target:
                        shutil.copyfileobj(source, target)
                        print("copying", source, "to", target)

            extracted_render_povray_path = os.path.join(temp_dir_path, "render_povray")

            if not os.path.exists(extracted_render_povray_path):
                self.report({"ERROR"}, "Could not extract ZIP archive! Aborting.")
                return {"FINISHED"}

            # Find the old POV addon files
            render_povray_dir = os.path.abspath(os.path.dirname(__file__)) # Unnecessary abspath?
            print("POV addon addon folder:", render_povray_dir)

            # TODO: Create backup

            # Delete old POV addon files
            # (only directories and *.py files, user might have other stuff in there!)
            print("Deleting old POV addon files")
            # remove __init__.py
            os.remove(os.path.join(render_povray_dir, "__init__.py"))
            # remove all folders
            dir_names = 1
            for directory in next(os.walk(render_povray_dir))[dir_names]:
                shutil.rmtree(os.path.join(render_povray_dir, directory))

            print("Copying new POV addon files")
            # copy new POV addon files
            # copy __init__.py
            shutil.copy2(
                os.path.join(extracted_render_povray_path, "__init__.py"),
                render_povray_dir,
            )
            # copy all folders
            recursive_overwrite(extracted_render_povray_path, render_povray_dir)

        bpy.ops.preferences.addon_refresh()
        print("POV addon update finished, restart Blender for the changes to take effect.")
        print("-" * 20)
        self.report({"WARNING"}, "Restart Blender!")
        return {"FINISHED"}
