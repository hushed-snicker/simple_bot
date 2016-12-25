#!/usr/bin/python

#TODO:
#flesh out bot.serve()
#flesh out bot.parse_input()
#Get logger working
##File "simple_bot.py", line 21
##  if self.debug == True:
##                       ^
##SyntaxError: invalid syntax

def output(s):
  print(s)

class bot(object):
  def __init__(self, name, **kwargs):

    print('##############')
    print('# Start Init #')
    print('##############')

    print('[INIT] Name set.')
    self.name = name
    kwargs['name'] = name
    print('[INIT] Name set to %s' % self.name)

    print('[INIT] Command character set')
    self.commandChar = '!'
    print('[INIT] Command characters are %s' % self.commandChar)

    print('[INIT] Debug set.')
    if kwargs['debug']:
      self.debug = kwargs['debug']
    else:
      self.debug = False
    print('[INIT] Debug set to %s' % self.debug)
    self.log('DEBUG', 'Debug test')

    #Input buffer
    print('[INIT] I/O Buffers')
    self.input_buffer = ''
    self.log_buffer = ''

    print("#################")
    print("# Finished Init #")
    print("#################")
    print()
    print("Hello User. Please start a conversation.")

  def log(self, code, msg):
    self.log_buffer = '[%s] %s' % (code, msg)
    if code == 'ERROR':
      output(self.log_buffer)
    if code == 'DEBUG':
      output(self.log_buffer)

  def handle_greeting(self):
    self.log('DEBUG', 'User greeted bot')
    output('Hello!')

  def handle_command(self):
    self.log('DEBUG', 'User passed a command character')

    #Removes the command character from the buffer
    self.input_buffer = self.input_buffer[1:]

    if self.input_buffer.lower() == 'quit':
      quit()

  def recv_input(self):
    self.input_buffer = input()
    self.log('DEBUG', 'Input is %s' % self.input_buffer)

  def parse_input(self):
    #Responds to Hello <self.name> with 'Hello!'
    if self.input_buffer.lower() == 'hello':
      self.handle_greeting()
    if self.input_buffer[0] == self.commandChar:
      self.handle_command()

  def serve(self):
    self.recv_input()
    self.parse_input()

  def serve_forever(self):
    try:
      while True:
        bot.serve(self)
    except KeyboardInterrupt:
      print()
      pass
