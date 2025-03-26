import subprocess, argparse, shutil, sys

if shutil.which('msbuild') is None:
    print("MSBuild is not on path.")
    sys.exit()

parser = argparse.ArgumentParser()
parser.add_argument('sln', help="Solution or Package to restore.")
parser.add_argument(
    '--npc',
    help="Sets RestorePackagesConfig to false.",
    dest='no_packages_config',
    type=bool,
    action=argparse.BooleanOptionalAction,
)

args = parser.parse_args()

command = f"msbuild {args.sln} -t:restore"

if not args.no_packages_config:
    command += " -p:RestorePackagesConfig=true"

subprocess.run(command)