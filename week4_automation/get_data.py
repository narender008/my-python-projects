import os
import shutil
import sys
import json
from subprocess import PIPE, run

GAME_PATTERN_DIR = "game"
COMPILE_EXTENTION = ".go"
GAME_COMPILE_COMMAND = ["go", "build"]


def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)


def copy_and_overwrite(path, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    shutil.copytree(path, destination)


def create_metadata(path, game_dir):
    data = {
        "game_name": game_dir,
        "number_of_games": len(game_dir),
    }

    with open(path, "w") as outfile:
        json.dump(data, outfile)


def run_command(command, path):
    cwd = os.getcwd()
    os.chdir(path)
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    print(f"complied result: {result}")
    os.chdir(cwd)


def compile_game_code(path):
    code_file_name = None
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(COMPILE_EXTENTION):
                code_file_name = file
                break

        break
    if code_file_name is None:
        return
    command = GAME_COMPILE_COMMAND + [code_file_name]
    run_command(command, path)


def new_dir_name(path, to_strip):
    new_game_dir = []
    for dirs in path:
        _, name = os.path.split(dirs)
        new_name = name.replace(to_strip, "")
        new_game_dir.append(new_name)
    return new_game_dir


def find_game_dir(source_path):
    game_path = []
    for (
        root,
        dirs,
        files,
    ) in os.walk(source_path):
        for directory in dirs:
            if GAME_PATTERN_DIR in directory:
                path = os.path.join(source_path, directory)
                game_path.append(path)
        return game_path
        break


# Adding source and destination paths
def main(source, destination):
    cwd = os.getcwd()
    source_path = os.path.join(cwd, source)
    destination_path = os.path.join(cwd, destination)
    dir_path = find_game_dir(source_path)
    new_name = new_dir_name(dir_path, "_game")
    create_dir(destination_path)
    for src, dest in zip(dir_path, new_name):
        dest_path = os.path.join(destination_path, dest)
        copy_and_overwrite(src, dest_path)
        compile_game_code(dest_path)
    json_path = os.path.join(destination_path, "metadata.json")
    create_metadata(json_path, new_name)


# Running the script
if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise Exception("Invalid number of arguments")
    source, destination = args[1:]
    main(source, destination)
