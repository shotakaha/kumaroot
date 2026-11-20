# Geant4 Examples

[Task](https://taskfile.dev) definitions for copying Geant4 examples from `basic/` into this directory, then building and running them.

## Prerequisites

- Geant4 installed in a version directory that contains `install/`
- `cmake` and `task` available on your `PATH`

The default layout is:

```text
$G4_ROOT/v$G4_VERSION/install/
```

The defaults are `G4_ROOT=/Users/shotakaha/geant4` and `G4_VERSION=11.4.3`. Change them to match your environment.

## Directory layout

Each example keeps its source and build output separate (out-of-source build).

```text
g4examples/
├── Taskfile.yml
├── B1/
│   ├── app/      # Source copied from Geant4
│   └── build/    # CMake build output
├── B2a/
└── B2b/
```

`app/` and `build/` are excluded by `.gitignore`.

## Usage

```sh
task                              # List tasks and usage
task b1:build                     # Copy and build B1
task b1:run                       # Run B1 in batch mode (app/run1.mac)
task b1:clean                     # Remove B1/build
```

Replace `b1` with `b2a` or `b2b` for the other examples.

### Other examples

`EXAMPLE` takes a path relative to `basic/`.

```sh
task example:build EXAMPLE=B2/B2b
task example:run EXAMPLE=B2/B2b
task example:run EXAMPLE=B1 ARGS=app/run2.mac   # Run a different macro
task example:clean EXAMPLE=B1
task example:copy EXAMPLE=B2/B2a                # Copy only
```

The directory and executable names come from the last segment of `EXAMPLE`. For example, `B2/B2a` produces `B2a/` and `exampleB2a`.

### Geant4 environment

| Task | Description |
| --- | --- |
| `task g4:versions` | List installed versions |
| `task g4:env` | Source `geant4.sh` and print `geant4-config --version` |

Each task that needs Geant4 sources `geant4.sh` inside its own commands. Your interactive shell's environment is not changed.

## Switching the version

```sh
task b1:build G4_VERSION=11.3.2
G4_VERSION=11.3.2 task b1:build
```

Run `task g4:versions` to see which versions are installed.

## Notes

- `example:copy` does not overwrite an existing `app/`. To re-copy the source, delete `<name>/app/` by hand first.
- `example:clean` removes only `build/`.
