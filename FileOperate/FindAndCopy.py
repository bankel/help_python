import os
import subprocess

rootpath = "/Users/lyf/Downloads/daxigua-1.0-2.0/res/raw-assets"
os.chdir(rootpath)

images = (
    "ad16ccdc-975e-4393-ae7b-8ac79c3795f2.png",
    "0cbb3dbb-2a85-42a5-be21-9839611e5af7.png",
    "d0c676e4-0956-4a03-90af-fee028cfabe4.png",
    "74237057-2880-4e1f-8a78-6d8ef00a1f5f.png",
    "132ded82-3e39-4e2e-bc34-fc934870f84c.png",
    "03c33f55-5932-4ff7-896b-814ba3a8edb8.png",
    "665a0ec9-6c43-4858-974c-025514f2a0e7.png",
    "84bc9d40-83d0-480c-b46a-3ef59e603e14.png",
    "5fa0264d-acbf-4a7b-8923-c106ec3b9215.png",
    "564ba620-6a55-4cbe-a5a6-6fa3edd80151.png",
    "5035266c-8df3-4236-8d82-a375e97a0d9c.png"
)


pendding_command = "find ./ -name {0}"
for image in images:
    command = pendding_command.format(image)
    output = subprocess.getoutput(command)

    command = "cp %s ~/Desktop/temp/mergeWaterMelon/" % output
    os.system(command)
