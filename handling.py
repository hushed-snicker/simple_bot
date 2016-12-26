#!/usr/bin/python

import logging

class handler(object):

  def __init__(self, debug):
    logger = logging.logger(debug)

    logger.log('HANDLER', 'Handler loaded')

  def handle_command(self):
    self.log('DEBUG', 'User passed a command character')
    self.log('DEBUG', 'IB[0]: %s' % self.input_buffer[0])
    self.log('DEBUG', 'IB[1]: %s' % self.input_buffer[1])
    self.log('DEBUG', 'IB[2]: %s' % self.input_buffer[2])

    #Removes the command character from the buffer
    self.input_buffer = self.input_buffer[1:]
    self.input_buffer = self.input_buffer.split()
    self.log('DEBUG', 'IB[0]: %s' % self.input_buffer[0])

    self.log('DEBUG', 'IB[1]: %s' % self.input_buffer[1])
    self.log('DEBUG', 'IB[2]: %s' % self.input_buffer[2])

    if self.input_buffer[0].lower() == 'quit':
      quit()

    #return input buffer for command parser
    else:
      return self.input_buffer
