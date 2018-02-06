#!/bin/bash

PARTICLES=$1

sed -i 's/0.0000000000000000e+00 5.0000000000000000e+01//g' sand-timer.xyz
sed -i 's/0.0000000000000000e+00 9.0000000000000000e+01//g' sand-timer.xyz

perl -0777 -i -pe "s/ITEM: TIMESTEP\n0\nITEM: NUMBER OF ATOMS\n0\nITEM: BOX BOUNDS pp pp ff\n\n\n\nITEM: ATOMS radius id x y z vx vy vz \nITEM: TIMESTEP/$PARTICLES/igs" sand-timer.xyz

perl -0777 -i -pe "s/ITEM: NUMBER OF ATOMS\n$PARTICLES\nITEM: BOX BOUNDS pp pp ff\n\n\n\nITEM: ATOMS radius id x y z vx vy vz \n//igs" sand-timer.xyz

sed -i "s/ITEM: TIMESTEP/$PARTICLES/g" sand-timer.xyz
