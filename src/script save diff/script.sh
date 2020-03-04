#!/bin/bash
cp file2.srm file1.srm
cp Castlevania\ -\ Symphony\ of\ the\ Night.srm file2.srm

xxd file1.srm > file1.hex
xxd file2.srm > file2.hex

diff -u file1.hex file2.hex > output.patch
