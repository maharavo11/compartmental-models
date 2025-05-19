import os
import shutil
import subprocess
import urllib

def custom_install_cmdstan(cmdstanpy_version= "1.2.5",
                           tgz_file="colab-cmdstan-2.36.0.tar.gz",
                           tgz_url="https://github.com/stan-dev/cmdstan/releases/download/v2.36.0/colab-cmdstan-2.36.0.tgz"):
    print(f"Installing cmdstanpy=={cmdstanpy_version}")
    subprocess.run(
        ["pip", "install", "--upgrade", f"cmdstanpy=={cmdstanpy_version}"],
        check=True)

    if not os.path.exists(tgz_file):
        print(f"Downloading {tgz_file}")
        urllib.request.urlretrieve(tgz_url, tgz_file)
    else:
        print(f"{tgz_file} has already been downloaded")
    print(f"Unpacking {tgz_file}")
    shutil.unpack_archive(tgz_file)

    print("Installing required libtbb2 Linux package")
    subprocess.run(["apt", "install", "-y", "libtbb2"], check=True)

    print("Setting cmdstan path")
    cmdstan_path_var = "./cmdstan-2.36.0"
    os.environ["CMDSTAN"] = cmdstan_path_var

    # Check that cmdstan can be found
    from cmdstanpy import cmdstan_path

    out = cmdstan_path()

    print("CmdStan successfully installed!")
