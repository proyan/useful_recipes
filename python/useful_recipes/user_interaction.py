
def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    import sys
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")




import threading
class UserPermittedRun:
    """Creates a thread which runs until user inputs.

    def my_giant_loop():
      #Stuff I want to do
      thr.pause_here()
      #Rest of the stuff I want to do

    thr = UserPermittedRun(my_giant_loop)
    thr.run()

    If user gives an input, thread waits at self.pause_here
    If user doesn't give an input (by default), self.pause_here doesn't do anything

    Problem: Base function return value is suppressed
    """

    def __init__(self,target, args = ()):
        self._base_fn = target
        self._pause = False
        self._continue = threading.Event()
        self._continue.set()
        self._args = args

    def pause_here(self):
        self._continue.wait()

    def run(self):
        self._thread1 = threading.Thread(target=self._base_fn, args = self._args)
        self._thread1.start()
        while self._thread1.is_alive():
            if self._pause == True:
                raw_input("Press Enter to Resume:")
                self._pause = False
                self._continue.set()
            else:
                raw_input("Press Enter to Pause or Finish:")
                self._pause = True
                self._continue.clear()

        print "Exiting from main thread"
        return True
