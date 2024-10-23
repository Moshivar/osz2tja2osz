from osu2tja.osu2tja import osu2tja, reset_global_variables
from tja2osu.tja2osu_file_dvide import divide_tja  # Use divide_tja for tja2osz conversion
from zipfile import ZipFile, is_zipfile
from typing import Dict, List
from os import path
import os
import sys
from io import TextIOWrapper

# Define a default MEASURE value
MEASURE = "4/4"  # Assuming a default measure, change if needed

def extract_osu_file_info(file) -> Dict[str, object]:
    line: str = file.readline()
    result: Dict[str, object] = dict()
    while line:
        if line.startswith("Version:"):
            result["version"] = line.split(":")[1].strip()
        elif line.startswith("OverallDifficulty:"):
            result["difficulty"] = float(line.split(":")[1])
        elif line.startswith("TitleUnicode:"):
            result["title"] = line.split(":")[1].strip()
        elif line.startswith("AudioFilename:"):
            result["audio"] = line.split(":")[1].strip()

        if len(result.keys()) == 4:
            return result
        line = file.readline()
    return result

def convert_osz2tja(source_path: str, target_path: str) -> None:
    warnings = []  # List to store warnings
    try:
        if not is_zipfile(source_path):
            raise ValueError(f"{source_path} is not a valid zip file")

        osu_zip: ZipFile = ZipFile(source_path, "r")
        osu_files = [filename for filename in osu_zip.namelist() if filename.endswith(".osu")]
        if not osu_files:
            raise ValueError(f"No .osu files found in {source_path}")

        osu_infos = list()
        for filename in osu_files:
            fp = TextIOWrapper(osu_zip.open(filename, "r"), encoding="utf-8")
            osu_info = extract_osu_file_info(fp)
            fp.close()
            osu_info["filename"] = filename
            osu_infos.append(osu_info)

        osu_infos.sort(key=lambda x: x["difficulty"], reverse=True)
        osu_infos = osu_infos[:4]  # Select the top 4 difficulties

        if not osu_infos:
            raise ValueError(f"No valid difficulties found in {source_path}")

        original_audio_name = osu_infos[0]["audio"]
        title = osu_infos[0]["title"]
        new_audio_name = title + path.splitext(original_audio_name)[-1]

        # Generate Oni, Hard, Normal, Easy from the top 4 difficulties
        difficulties = ["Oni", "Hard", "Normal", "Easy"]
        selected_infos = osu_infos[:len(difficulties)]

        head = []
        contents = {diff: [] for diff in difficulties}

        for i, info in enumerate(selected_infos):
            try:
                reset_global_variables()
                fp = TextIOWrapper(osu_zip.open(info["filename"]), encoding="utf-8")
                level = int(info["difficulty"])
                head, contents[difficulties[i]] = osu2tja(fp, difficulties[i], level, new_audio_name)
                fp.close()
            except Exception as e:
                warning_message = f"Error processing difficulty {difficulties[i]}: {e}"
                print(warning_message)
                warnings.append(warning_message)  # Track warnings for non-fatal errors

        # Extract audio
        storage_path = path.join(target_path, title)
        os.makedirs(storage_path, exist_ok=True)
        osu_zip.extract(original_audio_name, storage_path)
        os.rename(path.join(storage_path, original_audio_name), path.join(storage_path, new_audio_name))
        print(f"Extracted Audio for {title}")

        # Save .tja file
        with open(path.join(storage_path, f"{title}.tja"), "w+") as f:
            f.write("\n".join(head))
            for diff in difficulties:
                if contents[diff]:
                    f.write("\n")
                    f.write("\n".join(contents[diff]))
        print(f"Converted {title} to TJA")

        osu_zip.close()

        # If there are warnings, notify the user in the console
        if warnings:
            print(f"\nWarning: {title} may have possible errors due to the following issues:")
            for warning in warnings:
                print(f"- {warning}")

    except Exception as e:
        raise RuntimeError(f"Error converting {source_path}: {e}")

def batch_convert_osz2tja(input_folder: str, output_folder: str):
    skipped_files = []
    for filename in os.listdir(input_folder):
        if filename.endswith(".osz"):
            source_path = path.join(input_folder, filename)
            try:
                convert_osz2tja(source_path, output_folder)
            except Exception as e:
                print(f"Skipping {filename} due to error: {e}")
                skipped_files.append(filename)
    
    if skipped_files:
        print("\nSkipped files:")
        for file in skipped_files:
            print(f"- {file}")

def batch_convert_tja2osz(input_folder: str, output_folder: str):
    for filename in os.listdir(input_folder):
        if filename.endswith(".tja"):
            try:
                divide_tja(path.join(input_folder, filename))
                print(f"Converted {filename} to OSZ")
            except Exception as e:
                print(f"Error converting {filename}: {e}")

if __name__ == "__main__":
    print("Select conversion mode:")
    print("1. osz2tja (default)")
    print("2. tja2osz")
    choice = input("Enter 1 or 2: ")

    input_folder = "Songs"
    output_folder = "Output"

    print(f"Default input folder: {input_folder}")
    print(f"Default output folder: {output_folder}")

    if choice == "2":
        batch_convert_tja2osz(input_folder, output_folder)
    else:
        batch_convert_osz2tja(input_folder, output_folder)

    input("\nPress enter to exit...")
    sys.exit(0)
