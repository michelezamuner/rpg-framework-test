class Debug:
  LOG_FILE = 'debug.log'

  @staticmethod
  def log(string):
    file = open(Debug.LOG_FILE, 'a')
    file.write(str(string)+"\n")
    file.close()

  @staticmethod
  def logList(list):
    message = '(' + ', '.join(str(i) for i in list) + ')'
    Debug.log(message)