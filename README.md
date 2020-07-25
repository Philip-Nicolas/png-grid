## png-grid

Tool for overlaying grids onto png images.

### Dependencies

* [pypng](https://pypng.readthedocs.io/en/latest/index.html)

### Usage

`python pgrid.py [<pathspec>]`

`<pathspec>` PNG file to use.
Can be the path to a file, or a file in the current directory.
If no extension is provided, `.png` is assumed.

Once the script is launched, grid dimensions can be specified in the command line.

### Caveats

* Only supports RGBA files.
* Not errorproof in the slightest.