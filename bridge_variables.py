import scratchapi
USERNAME = 'blah'
PASSWORD = 'blah'
SOURCEPROJECT = '000'
SOURCEVARIABLE = 'a'
TARGETPROJECT = '000'
TARGETVARIABLE = 'a'
  def refreshprogram()
  s = scratchapi.ScratchUserSession(USERNAME, PASSWORD)
  var = (s.cloud.get_var(a, str(SOURCEPROJECT)))
  s.cloud.set_var(TARGETVARIABLE, var, str(TARGETPROJECT))
  def startprogram()
  print "Enter the source project ID: ",
  SOURCEPROJECT = raw_input()
  print "Enter the target project ID: ",
  TARGETPROJECT = raw_input()
  print "Enter the source project variable: ",
  SOURCEVARIABLE = raw_input()
  print "Enter the target project variable: ",
  TARGETVARIABLE = raw_input()
  print "Enter your username: ",
  USERNAME = raw_input()
  print "Enter your password: ",
  PASSWORD = raw_input()
  while True:
  print 'sleeping.'
  time.sleep(10)
  print 'refreshing.'
  refreshprogram()
  
