<h1 align="center">
  <b>instasave</b>
</h1>

A simple script to download media from Instagram posts.

## Install

This script runs on `Python 3.7+`.
You can install it from PyPI with:
```bash
pip install instasave
```

## Usage

With this package installed in the activated enrivonment, it can be called through `python -m instasave` or through a newly created `instasave` command.

Detailed usage goes as follows:
```bash
Usage: instasave [OPTIONS] [URL]

  Download media from Instagram posts.

Arguments:
  [URL]  Link to the Instagram post you want to download the content of.

Options:
  --log-level TEXT      The base console logging level. Can be 'debug',
                        'info', 'warning' and 'error'.  [default: info]

  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or
                        customize the installation.

  --help                Show this message and exit.
```

The downloaded files will be saved in the current directory under a name composed of the file type (image / video) appended by the download timestamp.

Warning: abusing this script may get your IP banned by Instagram.

## TODO

- [x] Implement proper logging.
- [x] Make into a package.
- [x] Make callable as a python module (`python -m instasave ...`).
- [x] Improving the command line experience.

---

<div align="center">
  <sub><strong>Made with ♥︎ by fsoubelet</strong></sub>
  <br>
  <sub><strong>MIT &copy 2020 Felix Soubelet</strong></sub>
</div>



[license]: https://github.com/fsoubelet/InstaSave/blob/master/LICENSE
[loguru_url]: https://github.com/Delgan/loguru
[requests_url]: https://github.com/psf/requests
[tqdm_url]: https://github.com/tqdm/tqdm
