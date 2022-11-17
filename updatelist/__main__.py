import datetime
import math
import os.path
import os

from . import version

LACKEY_SERVER_ROOT = os.getenv("LACKEY_SERVER_ROOT")

# remove any trailing slash
assert LACKEY_SERVER_ROOT, "LACKEY_SERVER_ROOT environment variable required"
if LACKEY_SERVER_ROOT[-1] == "/":
    LACKEY_SERVER_ROOT = LACKEY_SERVER_ROOT[:-1]


def checksum(path):
    with open(path, "rb") as fp:
        value = 0
        char = fp.peek(1)
        while char:
            char = fp.read(1)
            if char in [b"\n", b"\r"]:
                continue
            if char:
                # original code silently cast to signed char
                value += int.from_bytes(char, byteorder="big", signed=True)
            else:
                value -= 1
            # C modulus (truncated mod), Python % is floored, so we use math.fmod
            # https://en.wikipedia.org/wiki/Modulo_operation#In_programming_languages
            value = int(math.fmod(value, 100000000))
    return value


TOP_PATH = {
    "plugin/fonts",
    "plugin/skins",
    "plugin/images/avatars",
    "plugin/images/backgrounds",
    "plugin/images/zonebackgrounds",
}

version_date = datetime.date.fromisoformat(version.version)

with open("plugin/version.txt", "w") as fp:
    fp.write(
        f"""<version>

<lastupdateYYMMDD>{version_date:%y%m%d}</lastupdateYYMMDD>
 <quality>HIGH</quality>
 <versionurl>https://lackey.krcg.org/version.txt</versionurl>
 <updateurl>https://lackey.krcg.org/updatelist.txt</updateurl>
 <message>VtES updated to version {version_date:%Y-%m-%d}</message>
</version>
"""
    )

with open("plugin/updatelist.txt", "w") as fp:
    print("vtes", f"{version_date:%m-%d-%y}", sep="\t", file=fp)
    for dirpath, dirnames, filenames in os.walk("plugin"):
        for filename in sorted(filenames):
            if filename in [".DS_Store", "updatelist.txt", "index.html"]:
                continue
            filepath = os.path.join(dirpath, filename)
            if dirpath in TOP_PATH:
                local_path = dirpath.replace("plugin/", "") + "/" + filename
            else:
                local_path = dirpath.replace("plugin", "plugins/vtes") + "/" + filename
            server_path = dirpath.replace("plugin", LACKEY_SERVER_ROOT) + "/" + filename
            if filename in ["pluginpreferences.txt", "defaultchat.txt"]:
                h = 0
            else:
                h = checksum(filepath)
            print(local_path, server_path, h, sep="\t", file=fp)
            if local_path in {
                "plugins/vtes/cardback.jpg",
                "plugins/vtes/spawned.jpg",
                "plugins/vtes/spawned.png",
            }:
                local_path = local_path.replace(
                    "plugins/vtes", "plugins/vtes/sets/setimages/general"
                )
                print(local_path, server_path, h, sep="\t", file=fp)
    print("CardGeneralURLs:", file=fp)
    print("https://static.krcg.org/card/", file=fp)
