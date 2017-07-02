# sand-timer-lamps

## Installation

 * Download lammps
 * Make the Makefile.serial (with the download you should probably have one of those, replace it with the given one)
 * Run `make yes-standard`
 * Re-make the serial

## Life hacks

 * Open `~/.bashrc`
 * Add to the end of it `alias lammps='~/[Directory to lammps]/src/lmp_serial'`
 * Now you can run `lammps` anywhere.

## Run

 * From `granregion` run `lampps < in.granregion.TYPE`
   * Where `TYPE = 'box' | 'funnel' | 'mixer'`
 * This will run the script on the `in` file an generate a `movie-TYPE.avi` file
