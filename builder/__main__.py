import os
import shutil


LACKEY_SERVER_ROOT = os.getenv("LACKEY_SERVER_ROOT")

# remove any trailing slash
assert LACKEY_SERVER_ROOT, "LACKEY_SERVER_ROOT environment variable required"
if LACKEY_SERVER_ROOT[-1] == "/":
    LACKEY_SERVER_ROOT = LACKEY_SERVER_ROOT[:-1]

updatelist = open("plugin/updatelist.txt")
updatelist.readline()
for line in updatelist:
    values = line.split("\t")
    if len(values) != 3:
        break
    local, server, _hash = values
    if local[:7] != "plugins":
        continue
    server = server.replace(LACKEY_SERVER_ROOT, "plugin")
    local = local.replace("plugins", "build")
    os.makedirs(os.path.dirname(local), exist_ok=True)
    shutil.copyfile(server, local)
shutil.copyfile("plugin/updatelist.txt", "build/vtes/updatelist.txt")
shutil.make_archive("build/vtes", "zip", "build/vtes")
shutil.make_archive("build/vtes", "gztar", "build/vtes")
