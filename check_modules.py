
class checkModules(object):
    # initialization
    def __init__(self):
        self.url = ''
        self.command = 'pip install {}'

    # connect to database
    def checkIpy(self):
        try:
            self.command.format('IPy')
        except Exception as e:
            print(e)