<h1 align="center">
  <b>instasave</b>
</h1>

A simple script to download media from Instagram posts.

## Install

This script runs on Python3.6+, and requires the following libraries: [`requests`][requests_url], [`tqdm`][tqdm_url] and [`loguru`][loguru_url].
You can install this package from PyPI with:
```bash
pip install instasave
```

## Usage

With this package is installed in the activated enrivonment, usage is:
```bash
python -m instasave --url link_to_instagram_post
```

Detailed options go as follows:
```bash
usage: __main__.py [-h] -u URL [-l LOG_LEVEL]

Downloading media from Instagram posts.

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     Link to the Instagram post you want to download the
                        content of.
  -l LOG_LEVEL, --logs LOG_LEVEL
                        The base console logging level. Can be 'debug',
                        'info', 'warning' and 'error'. Defaults to 'info'.
```

The downloaded files will be saved in the current directory under a name composed of the file type (image / video) appended by the download timestamp.

Warning: abusing this script may get your IP banned by Instagram.

## TODO

- [x] Implement proper logging.
- [x] Make into a package.
- [x] Make callable as a python module (`python -m instasave ...`).

## License

Copyright &copy; 2020 Felix Soubelet. [MIT License][license]

[loguru_url]: https://github.com/Delgan/loguru
[requests_url]: https://github.com/psf/requests
[tqdm_url]: https://github.com/tqdm/tqdm