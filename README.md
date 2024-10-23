
# README.md

## Overview
This project provides a tool for converting `.osz` files (osu! beatmap files) into OpenTaiko-compatible `.tja` files, suitable for use in Taiko no Tatsujin-style rhythm games. The tool automatically assigns difficulties and supports converting `.osz` files with more than 4 difficulties by splitting them into multiple Taiko-compatible folders. The program also allows customization of input and output folders for batch processing.

## Features
- **Batch conversion** of `.osz` files to `.tja` files.
- Automatically maps osu! difficulties (up to 4 per `.tja` file) to Taiko's **Oni**, **Hard**, **Normal**, and **Easy** difficulties.
- Supports maps with **more than 4 difficulties** by splitting them into multiple folders (e.g., `title - 1`, `title - 2`).
- **Progressive star scaling**: Difficulty stars are scaled progressively between folders to ensure that stars for higher difficulties increase as you go.
  > Note that these star assignments **ARE NOT** equlivent to the typical Taiko star ratings since osu! has a much broader difficulty range than Taiko.
- **Custom folder support**: Specify custom input and output folders when running the program.
- **Metadata support** Each generated `.tja` file includes the title, subtitle, and creator information.

## Requirements
- Python 3.x
- Dependencies:
  - a `.osz` to convert
  - OpenTaiko or another software that can run `.tja` files

## Setup
1. Place any amount of `.osz` files in the `Songs` folder (default input folder).
2. The generated `.tja` files and audio files will be output to the `Output` folder by default.
   > They will be in their own individual Chart Folders for ease of use
4. You can customize the input and output folders via command-line arguments.

## Usage

To run the program with default settings:

```bash
python main.py
```

This will:
- Look for `.osz` files in the `Songs` folder.
- Output converted `.tja` files into the `Output` folder.
- If an `.osz` file contains more than 4 difficulties, the program will split them into separate folders (e.g., `title - 1`, `title - 2`), in order from easiest difficulties to the hardest.

## Customizing Input and Output Folders
You can specify custom input and output folders when running the program:

- **Specify custom input folder**:
  ```bash
  python main.py <input_folder>
  ```
  Example:
  ```bash
  python main.py a_folder
  ```

- **Specify both input and output folders**:
  ```bash
  python main.py <input_folder> <output_folder>
  ```
  Example:
  ```bash
  python main.py a_folder b_folder
  ```

When specifying folders:
- `<input_folder>` is where your `.osz` files are located.
- `<output_folder>` is where the `.tja` files will be saved.

## Process

1. **Prepare `.osz` files**:
   - Place your `.osz` files in the default `Songs` folder, or specify a custom input folder.
   
2. **Run the script**:
   - Run the script using the default settings or by specifying custom folders.

3. **Output**:
   - The program will create OpenTaiko-compatible folders in the output directory.
   - If there are more than 4 difficulties, the program will split them into multiple folders (e.g., `title - 1`, `title - 2`), scaling difficulty stars progressively.

## Not Implemented
- **`tja2osz` Conversion**: The reverse conversion from `.tja` to `.osz` is not implemented yet. Selecting this option will do nothing.

## Contributing
- Feel free to submit issues or feature requests.
- Contributions are welcome to implement the `tja2osz` functionality or any other feature enhancements.

## License
This project is licensed under the MIT License.
