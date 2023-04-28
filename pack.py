import os
import zipfile
from pathlib import Path
import gehannes

def get_all_files(folder_path):
    all_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            all_files.append(os.path.join(root, file))
    return all_files

def create_zip(folder_path, all_files):
    gehannes.convert_po_to_mo_with_swapped_msgctxt_and_msgid("nl.po","Language/NL.MO")
    selected_files = ".metadata/metadata.json,.metadata/thumbnail.png,Language/Name.txt,Language/NL.MO,NL.acp".split(',')

    with zipfile.ZipFile('mod.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        for selected_file in selected_files:
            selected_file = selected_file.strip()
            selected_path = Path(folder_path, selected_file)

            if not selected_path.exists():
                print(f"{selected_file} does not exist. Skipping.")
                continue

            if selected_path.is_file():
                arcname = os.path.relpath(selected_path, folder_path)
                zipf.write(selected_path, arcname)
            elif selected_path.is_dir():
                for file in get_all_files(selected_path):
                    arcname = os.path.relpath(file, folder_path)
                    zipf.write(file, arcname)
            else:
                print(f"{selected_file} is not a file or folder. Skipping.")

    os.remove("Language/NL.MO")
    print("mod.zip created successfully.")

if __name__ == "__main__":
    folder_path = "."
    folder_path = os.path.abspath(folder_path)

    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        print(f"The path '{folder_path}' does not exist or is not a directory.")
    else:
        all_files = get_all_files(folder_path)
        create_zip(folder_path, all_files)
