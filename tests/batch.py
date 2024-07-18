import multiprocessing

from pipeproxy import proxy

def work(proxy):
    print(dir(proxy))
    proxy.compute()

class Comp:
    def __init__(self):
        self.proxy = None
        self.proxy_listener = None

    def start(self):
        p = multiprocessing.Process(target=work, args=(self.proxy,))
        p.start()
        self.proxy_listener.listen()

    def add(self, prox):
        self.proxy, self.proxy_listener = prox