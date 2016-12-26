#!/usr/bin/python

import simple_botv2

bot = simple_botv2.bot('Test_Bot', debug=True, cmdChar='!')

bot.serve()

print()
print('Would you like to have me loop until a Keyboard Interrupt occurs? (y/n)')
answer = input()

if answer[0].lower() == 'y':
  bot.serve_forever()
else:
  print('Goodbye')
