from os import walk
from os.path import join, dirname
from tempfile import TemporaryDirectory
from urllib.request import urlretrieve
from zipfile import ZipFile
import sys

all_files = {}


def index_project(
    source: str | None = None,
):
    if source is None:
        source = "https://github.com/TLCFEM/suanPan/archive/refs/heads/dev.zip"

    with TemporaryDirectory() as tmp_dir:
        if source.startswith("http"):
            file_path = join(tmp_dir, "dev.zip")
            urlretrieve(source, file_path)

            archive_path = join(tmp_dir, "suanPan")

            with ZipFile(file_path, "r") as zip_archive:
                zip_archive.extractall(archive_path)
        else:
            archive_path = source

        cpp_files = {}
        for root, _, files in walk(archive_path):
            for file in files:
                if not file.endswith(".cpp") or "Include" in (
                    cpp_file := join(root, file)
                ):
                    continue
                with open(cpp_file, "r") as f:
                    cpp_files[file.replace(".cpp", "")] = f.read().split("\n")

        return cpp_files


def extract_function(token: str):
    class_name, function_name = token.split("::", 1)
    if class_name not in all_files:
        raise ValueError(f"Class {class_name} not found.")
    if "::" not in function_name:
        function_name = token
    method_content = []
    for line in all_files[class_name]:
        if function_name in line:
            method_content.append(line)
            if line.endswith("}"):
                break
        elif method_content:
            method_content.append(line)
            if "}" == line:
                break
    return method_content


def walk_tex(source: str):
    for root, _, files in walk(source):
        for file in files:
            if not file.endswith(".tex"):
                continue

            tex_file = join(root, file)
            with open(tex_file, "r") as f:
                tex_content = f.read().split("\n")

            all_code_blocks = []
            for i, line in enumerate(tex_content):
                if (
                    r"\begin{cppcode}" == line
                    and "::" in tex_content[i + 1]
                    and r"\end{cppcode}" == tex_content[i + 2]
                ):
                    all_code_blocks.append(i + 1)

            if not all_code_blocks:
                continue

            # replace all lines within the text context by the code block extracted
            new_content = []
            for i, line in enumerate(tex_content):
                if i in all_code_blocks:
                    new_content.extend(extract_function(tex_content[i].strip()))
                else:
                    new_content.append(line)

            with open(tex_file, "w") as f:
                f.write("\n".join(new_content))


if __name__ == "__main__":
    all_files = index_project(sys.argv[1] if len(sys.argv) > 1 else None)
    walk_tex(join(dirname(__file__), "../CHAPTER"))
