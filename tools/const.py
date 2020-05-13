class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def colortest(self):
        print(self.HEADER + "HEADER" +self.ENDC)
        print(self.OKBLUE + "OKBLUE" +self.ENDC)
        print(self.OKGREEN + "OKGREEN" +self.ENDC)
        print(self.WARNING + "WARNING" +self.ENDC)
        print(self.FAIL + "FAIL" +self.ENDC)
        print(self.BOLD + "BOLD" +self.ENDC)
        print(self.UNDERLINE + "UNDERLINE" +self.ENDC)
