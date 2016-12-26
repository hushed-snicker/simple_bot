#!/usr/bin/python

#Temporary output for all files since all use the logger
def output(s):
  print(s)

class logger(object):

  def __init__(self, debug):
    self.log_buffer = ''
    self.debug = debug
    print('[LOGGER] Init Finished')

  def log(self, code, msg):
    self.log_buffer = '[%s] %s' % (code, msg)
    if code == 'DEBUG':
      if self.debug:
        output(self.log_buffer)
      else:
        pass
    else:
      output(self.log_buffer)
