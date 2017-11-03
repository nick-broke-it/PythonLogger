class Logger(object):
    def log(self, message, color=None):
        if color:
            color = color.lower()
        else:
            pass

        if color==None:
            print message
        elif color=="red":
            print u"\u001b[31m {} \u001b[0m".format(message)
        elif color=="green":
            print u"\u001b[32m {} \u001b[0m".format(message)
        elif color=="blue":
            print u"\u001b[36m {} \u001b[0m".format(message)
        else:
            raise NameError(u"\u001b[31m No Valid Color Specified \u001b[0m")

Logger = Logger()

#Logger.log("message here", "color is optional")
