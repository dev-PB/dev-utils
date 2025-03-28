import os, shutil

CLI_RED = '\033[31m'
CLI_END = '\033[0m'

EXTENSIONS = (".sln", ".csproj", ".vs", ".iml", ".idea")
if not any(item.endswith(EXTENSIONS) for item in os.listdir(".")):
    print("The current directory doesn't appear to be the root of a solution or project. Type 'delbo' to continue.")

    if (input(">").lower() != "delbo"):
        print("Cancelled.")
        quit()

for path, folders, files in os.walk("."):
    for folder in folders:
        if folder == "node_modules":
            folders.remove(folder)
            continue

        if folder == "bin" or folder == "obj":
            folder_path = os.path.join(path, folder)

            try:
                shutil.rmtree(folder_path)
                # Don't recurse into the deleted folder.
                folders.remove(folder)
                print("Deleted " + folder_path)

            except Exception as error:
                print(f"{CLI_RED}\nError deleting folder: '{folder_path}'\n{error}\n{CLI_END}");
