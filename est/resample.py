#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# Developer : Shashank Sharma(shashankrnr32@gmail.com)
# License : MIT License
# Year : 2019
# =============================================================================
# =============================================================================
# Description:
#     Resample a .wav file
# =============================================================================

import speech_tools as est
import argparse

parser = argparse.ArgumentParser(description = 'Resample a Wave file')

parser.add_argument('-i', nargs = '?', required = True, type = str, help = 'Input File (.wav)')
parser.add_argument('-o', nargs = '?', required = True, type = str, help = 'Output File (.wav)')
parser.add_argument('-f', nargs = '?', required = True, type = int, help = 'Output Sampling Frequency in Hz')
parser.add_argument('-info',default = False, action = 'store_true', help = 'Print Info of Output Wave')
args = parser.parse_args()

#Resample
est.resample(args.i, args.o, args.f)

#If -info is True, print info about output wave
if args.info:
    est.info(args.o)