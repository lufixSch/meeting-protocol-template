#!/usr/bin/env python

"""
  Created: 5/24/21
  by: Lukas Schuettler

  Setupscript for the LaTex meeting template
"""


import argparse
import os
import datetime

_main_file = r'main.tex'
_params_file = r'params.tex'

arg_def = {
    "topic": ("-t", "--topic", "topic of the meeting"),
    "project": ("-p", "--project", "discussed project"),
    "location": ("-l", "--location", "location of the meeting (Online for Onlinemeetings)"),
    "minute_taker": ("-m", "--minute-taker", "name of the minute taker"),
    "chair_person": ("-c", "--chair-person", "name of the chair person"),
    "participants": ("-pa", "--participants", "names of further participants (optional)")
}


def parseArguments():
    """
      Parse arguments given by the arg_def dict
      Ask for them via input if they are not given as commandline options
    """
    parser = argparse.ArgumentParser()

    for key in arg_def:
        short, cmd, description = arg_def[key]
        parser.add_argument(short, cmd, help=description)

    args = parser.parse_args().__dict__

    for key in args:
        arg = args[key]

        if arg is None:
            args[key] = input(f'{arg_def[key][2]}: ')

    return args


def setupFilestructure():
    """
      Rename files and replace placeholder with given options
    """

    filename = f'meeting_{date_name}.tex'
    os.rename(_main_file, filename)

    params = open(_params_file)
    params_str = params.read()
    params.close()

    params_str = params_str.replace(
        '$TOPIC$', meeting_params['topic']).replace(
        '$PROJECT$', meeting_params['project']).replace(
        '$SECRETARY$', meeting_params['minute_taker']).replace(
        '$LEADER$', meeting_params['chair_person']).replace(
        '$LOCATION$', meeting_params['location']).replace(
        '$PARTICIPANTS$', meeting_params['participants']).replace(
        '$DATE$', date).replace(
        '$TIME$', time)

    params = open(_params_file, 'w')
    params.write(params_str)
    params.close()

    makefile = open(r'Makefile', 'w')
    content = makefile.read()
    makefile.write(content.replace(r"%ENTRYPOINT%", filename))

    print('Meeting protocol initialized')


meeting_params = parseArguments()

date = datetime.datetime.now().strftime(r'%d.%m.%Y')
date_name = datetime.datetime.now().strftime(r'%y_%m_%d')
time = datetime.datetime.now().strftime(r'%H:%M')

setupFilestructure()
