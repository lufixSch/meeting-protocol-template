#!/usr/bin/env python

"""
  Created: 5/24/21
  by: Lukas Schuettler

  Buildscript for the LaTex meeting template
"""

from os.path import sep


_content_file = r'content'

open_env = ''
open_topic = ''

heading = "#"

envs = [
    ("DEC:", "contents"),
    ("TASK:", "tasks")
]

keywords = [
    ("-", r'\1'),
    ("  -", r'\2'),
    ("    -", r'\3'),
    ("      -", r'\4'),
    ("*", r'\1'),
    ("  *", r'\2'),
    ("    *", r'\3'),
    ("      *", r'\4'),
]


def parseFile(old_line):
    """
      Parse lines to latex commands
    """

    global open_env
    global open_topic

    if old_line.startswith(heading):
        new_line = open_env + open_topic + \
            r'\topic{' + old_line.strip(heading).strip('\n') + '}\n'
        open_topic = r'\topicend' + '\n'
        open_env = ''
        return new_line

    for env in envs:
        if old_line.startswith(env[0]):
            new_line = open_env + r'\begin{' + env[1] + '}\n'
            open_env = r'\end{' + env[1] + '}\n'
            return new_line

    for keyword in keywords:
        if old_line.startswith(keyword[0]):
            return old_line.replace(keyword[0], keyword[1], 1)

    return old_line


content_file = open(f'{_content_file}.md')

latex_content = ''

while True:
    # read line of file
    line = content_file.readline()
    if len(line) == 0:
        latex_content += open_env + open_topic
        break

    latex_content += parseFile(line)

content_file.close()

latex_file = open(f'src{sep}pages{sep}{_content_file}.tex', 'w+')
latex_file.write(latex_content)
latex_file.close()
