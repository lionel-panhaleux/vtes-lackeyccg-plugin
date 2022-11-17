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
- Release: `make release`. This will check everything and tag the version.
- Create a [release in Github](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases), upload the `zip` and `tar.gz` files sitting in the `build` folder.

### Put it online

Go to Github Actions tab and use the `Deployment` action. Just select your tag and run it.
