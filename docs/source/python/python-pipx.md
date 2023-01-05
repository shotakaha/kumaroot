# pipx

```bash
$ brew install pipx
==> Pouring pipx--1.1.0.monterey.bottle.tar.gz
Error: The `brew link` step did not complete successfully
The formula built, but is not symlinked into /usr/local
Could not symlink bin/register-python-argcomplete
Target /usr/local/bin/register-python-argcomplete
already exists. You may want to remove it:
  rm '/usr/local/bin/register-python-argcomplete'

To force the link and overwrite all conflicting files:
  brew link --overwrite pipx

To list all files that would be deleted:
  brew link --overwrite --dry-run pipx

Possible conflicting files are:
/usr/local/bin/register-python-argcomplete
==> Summary
🍺  /usr/local/Cellar/pipx/1.1.0: 896 files, 11.3MB
==> Running `brew cleanup pipx`...

$ brew link --overwrite pipx
Linking /usr/local/Cellar/pipx/1.1.0... 4 symlinks created.

$ pipx ensurepath
Success! Added /Users/shotakaha/.local/bin to the PATH environment variable.

Consider adding shell completions for pipx. Run 'pipx completions' for instructions.

You will need to open a new terminal or re-login for the PATH changes to take effect.

Otherwise pipx is ready to go! ✨ 🌟 ✨
```

```bash
$ pipx completions

Add the appropriate command to your shells config file
so that it is run on startup. You will likely have to restart
or re-login for the autocompletion to start working.

bash:
    eval "$(register-python-argcomplete pipx)"

zsh:
    To activate completions for zsh you need to have
    bashcompinit enabled in zsh:

    autoload -U bashcompinit
    bashcompinit

    Afterwards you can enable completion for pipx:

    eval "$(register-python-argcomplete pipx)"

tcsh:
    eval `register-python-argcomplete --shell tcsh pipx`

fish:
    # Not required to be in the config file, only run once
    register-python-argcomplete --shell fish pipx >~/.config/fish/completions/pipx.fish
```

```bash
$ register-python-argcomplete --shell fish pipx >~/.config/fish/completions/pipx.fish
```
