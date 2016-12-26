#!/usr/bin/python

import logging

class parser(object):

  def __init__(self, commandChar, debug):
    logger = logging.logger(debug)

    self.commandChar = commandChar

    logger.log('PARSER', 'Parser loaded')

  def input(self, input):
    if input[0].lower() == 'hello':
      logger.log('DEBUG', 'User greeted bot')
      output('Hello!')

  def command(self, cmd, args):
    self.cmd = cmd
    self.args = args
