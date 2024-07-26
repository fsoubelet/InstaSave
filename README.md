<h1 align="center">
  <b>instasave</b>
</h1>

A simple script to download media from Instagram posts.

## Install

This code is compatible with all currently supported Python versions.
Install it in your virtual enrivonment with:

```bash
python -m pip install instasave
```

## Usage

> [!WARNING]  
> Abusing this script may get your IP banned by Instagram.

With this package installed in the activated enrivonment, it can be called through `python -m instasave` or through a newly created `instasave` command.

Detailed usage goes as follows:

```bash
Usage: python -m instasave [OPTIONS] [URL]                                                 
                                                                                            
 Download media from Instagram posts.                                                       
                                                                                            
╭─ Arguments ──────────────────────────────────────────────────────────────────────────────╮
│   url      [URL]  Link to the Instagram post you want to download the content of.        │
│                   [default: None]                                                        │
╰──────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────────────────╮
│ --log-level                 TEXT  The base console logging level. Can be 'debug',        │
│                                   'info', 'warning' and 'error'.                         │
│                                   [default: info]                                        │
│ --install-completion              Install completion for the current shell.              │
│ --show-completion                 Show completion for the current shell, to copy it or   │
│                                   customize the installation.                            │
│ --help                            Show this message and exit.                            │
╰──────────────────────────────────────────────────────────────────────────────────────────╯
```

The downloaded files will be saved in the current directory under a name composed of the file type (image / video) appended by the download timestamp.

---

<div align="center">
  <sub><strong>Made with ♥︎ by fsoubelet</strong></sub>
  <br>
  <sub><strong>MIT &copy 2020 Felix Soubelet</strong></sub>
</div>
