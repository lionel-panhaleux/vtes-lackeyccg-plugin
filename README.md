# LackeyCCG VTES Plugin

[![Validation](https://github.com/lionel-panhaleux/vtes-lackeyccg-plugin/workflows/Test/badge.svg)](https://github.com/lionel-panhaleux/vtes-lackeyccg-plugin/actions)
[![License](https://img.shields.io/badge/License-MIT-blue)](https://opensource.org/licenses/MIT)

This is a [LackeyCCG](https://lackeyccg.com) plugin for
[VTES (Vampire: The Eternal Struggle)](https://www.blackchantry.com/products/what-is-vampire-the-eternal-struggle/).

To use it in LackeyCCG, use this update URL: `https://lackey.krcg.org/updatelist.txt`

[Changelog](CHANGELOG.md)

![Dark Pack](https://raw.githubusercontent.com/lionel-panhaleux/krcg/master/dark-pack.png)

## New version generation

This plugin uses [Python](https://python.org) scripts to update the cards list
from the official [VEKN CSV](https://www.vekn.net/card-lists)
and generate the `updatelist.txt` and `version.txt` files.

### Perpare your python environment

Use your favorite python environment, `python -m venv lackey_env` for example. Check
[the official documentation](https://docs.python.org/3/library/venv.html#how-venvs-work)
if you're new to virtual environments.
Then call `make update` to install the Python requirements. You're ready.

### Prepare the plugin update

- Make sure the cards images are on `https://static.krcg.org`.
  See the [krcg-static repository](https://github.com/lionel-panhaleux/krcg-static) on how to proceed with this operation if you need to do it first.
- To update the cards list: `make cards`
- To generate the plugin list and version files: `make list`
- Update `CHANGELOG.md` file
- Commit and push your results
- Make sure [the tests pass](https://github.com/lionel-panhaleux/vtes-lackeyccg-plugin/actions)
- [Tag it](https://git-scm.com/book/en/v2/Git-Basics-Tagging)
- Use `make build` to build the plugin `zip` and `tar.gz` files in the `build` folder
- Create a [release in Github](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases), upload the `zip` and `tar.gz` files

### Put it online

The access to the current update server (`krcg.org`) is private for now.
In the future, I will try to setup the proper Github actions so that every administrator
can update and deploy the plugin.

In the mean time, you can host the plugin your own server with a simple variable change:

```bash
SERVER_HTTP=https://example.com/path_to_plugin make list
SERVER_SSH=example.com:server/path_to_plugin make static
```

You need to be able to connect via `ssh` to your server for this command to work.
Do not forget to regenerate the `updatelist.txt` file when changing the server URL.
