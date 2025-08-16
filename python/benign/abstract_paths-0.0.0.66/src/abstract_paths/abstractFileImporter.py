import os
import sys
import importlib.util
from abstract_utilities import *
from .content_utils import findContent
class AbstractFileFinderImporter:
    def __init__(self, start_dir=None, preferred_dir=None):
        start_dir = start_dir or '.'
        self.start_dir = os.path.abspath(start_dir)
        self.preferred_dir = os.path.abspath(preferred_dir) if preferred_dir else None

    def find_paths(self, basenames):
        """
        Finds all paths to files with the given basename(s) starting from start_dir.
        """
        if isinstance(basenames, str):
            basenames = [basenames]

        matching_paths = []

        for root, dirs, files in os.walk(self.start_dir):
            found_files = set(basenames).intersection(files)
            for basename in found_files:
                full_path = os.path.join(root, basename)
                matching_paths.append(full_path)

        # Remove duplicates and sort paths by distance from start_dir
        matching_paths = list(set(matching_paths))
        matching_paths.sort(key=lambda path: self._compute_distance(path))

        return matching_paths

    def _compute_distance(self, path):
        path = os.path.abspath(path)
        if self.preferred_dir and os.path.commonpath([self.preferred_dir, path]) == self.preferred_dir:
            return -1000 + self._path_length(path)

        relative_path = os.path.relpath(path, self.start_dir)
        distance = len(relative_path.split(os.sep))

        return distance

    def _path_length(self, path):
        return len(path.split(os.sep))

    def import_module_from_path(self, module_path):
        """
        Dynamically imports a module from a given file path, handling relative imports within the module.
        """
        module_name = os.path.splitext(os.path.basename(module_path))[0]
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)

        # Add the module's directory and any necessary subdirectories to sys.path temporarily
        module_dir = os.path.dirname(module_path)
        original_sys_path = list(sys.path)
        sys.path.insert(0, module_dir)

        # If `scripts` exists in the module directory, add it to sys.path
        scripts_dir = os.path.join(module_dir, 'scripts')
        if os.path.isdir(scripts_dir):
            sys.path.insert(0, scripts_dir)

        try:
            spec.loader.exec_module(module)
        except Exception as e:
            raise ImportError(f"Failed to import module {module_name}: {e}")
        finally:
            sys.path = original_sys_path  # Restore original sys.path

        return module

    def import_function_from_path(self, module_path, function_name):
        """
        Imports a specific function from a module file path.
        """
        module = self.import_module_from_path(module_path)
        if not hasattr(module, function_name):
            raise AttributeError(f"Function {function_name} not found in module {module.__name__}")

        return getattr(module, function_name)

def return_function(start_dir=None,preferred_dir=None,basenames=None,functionName=None):
    if basenames:
        basenames = make_list(basenames)
        abstract_file_finder = AbstractFileFinderImporter(start_dir=start_dir,preferred_dir=preferred_dir)
        paths = abstract_file_finder.find_paths(basenames)
        func = abstract_file_finder.import_function_from_path(paths[0], functionName)
        return func
def getLineNums(file_path):
    lines=[]
    if file_path and isinstance(file_path,dict):
        lines = file_path.get('lines')
        file_path = file_path.get('file_path')
    return file_path,lines
def get_line_content(obj):
    line,content=None,None
    if obj and isinstance(obj,dict):
        line=obj.get('line')
        content = obj.get('content')
    print(f"line: {line}\ncontent: {content}")
    return line,content
def get_edit(file_path):
    if file_path and os.path.isfile(file_path):
        os.system(f"code {file_path}")
        input()
def editLines(file_paths):
    for file_path in file_paths:
        file_path,lines = getLineNums(file_path)
        for obj in lines:
            line,content = get_line_content(obj)
        get_edit(file_path)
def findContentAndEdit(
    directory: str,
    paths: Optional[Union[bool, str]] = True,
    exts: Optional[Union[bool, str, List[str]]] = True,
    recursive: bool = True,
    strings: list=[],
    total_strings=True,
    parse_lines=False,
    spec_line=False,
    get_lines=True,
    edit_lines=True
    ):
    if isinstance(exts,list):
        exts ='|'.join(exts)
    
    file_paths = findContent(
        directory=directory,
        paths=paths,
        exts=exts,
        recursive=recursive,
        strings=strings,
        total_strings=total_strings,
        parse_lines=parse_lines,
        spec_line=spec_line,
        get_lines=get_lines
        )
    if edit_lines:
        editLines(file_paths)
    return file_paths
