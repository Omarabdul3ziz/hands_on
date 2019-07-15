from threading import Thread
from time import sleep

class Hi(Thread):
    def run(self):
        for i in range(5):
            print('HI')
            sleep(1)

class Bye(Thread):
    def run(self):
        for i in range(5):
            print('BYE')
            sleep(1)

hi = Hi()
bye = Bye()

hi.start()
sleep(0.5)
bye.start()

hi.join()
bye.join()

print('Exitting ..')
