# sand-timer-lammps

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

 * From `granregion` run `lammps < in.granregion.TYPE`
   * Where `TYPE = 'box' | 'funnel' | 'mixer' | 'sand-timer'`
 * This will run the script on the `in` file an generate a `movie-TYPE.avi` file

## Generate .xyz

 * Running the lammps program for the <strong>sand-timer</strong> will generate an .xyz file with trash information on it, to clean it, run the following script
   * From the granregion folder execute `./generate-xyz.sh NUMBER_OF_PARTICLES_USED`  
