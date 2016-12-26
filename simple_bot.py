#!/usr/bin/python

import logging
import handling
import parsing

class bot(object):

  def __init__(self, name, **kwargs):

    print('##############')
    print('# Start Init #')
    print('##############')

    #Logger setup
    print('[INIT] Logger setup')

    print('[LOGGER] Debug Check')
    if kwargs['debug']:
      self.debug = kwargs['debug']
    else:
      self.debug = false

    logger = logging.logger(self.debug)
    logger.log('INIT', 'Logger started') #Switch to loggers init

    #Arg Handler
    logger.log('INIT', 'Arg Set')

    if kwargs['cmdChar']:
      self.commandChar = kwargs['cmdChar']
      logger.log('INIT', 'commandChar: %s' % self.commandChar)

    #Buffer Init
    logger.log('INIT', 'Buffer Set')
    self.input_buffer = ''

    #Name set
    logger.log('INIT', 'Setting my name to %s' % name)
    self.name = name

    #Parser set
    logger.log('INIT', 'Setting up parser')
    parser = parsing.parser(self.commandChar, self.debug)

    #Handler set
    logger.log('INIT', 'Setting up handler')
    handler = handling.handler(self.debug)

    logger.log('INIT', 'Init Finished')

  def recv_input(self):
    self.input_buffer = input()
    logger.log('DEBUG', 'Input is %s' % self.input_buffer)

  def serve(self):
    self.recv_input()
    parser.input(self.input_buffer)

  def serve_forever(self):
    try:
      while True:
        bot.serve(self)
    except KeyboardInterrupt:
      print()
