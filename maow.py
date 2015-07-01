from twisted.internet.protocol import Protocol, Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor

class MaowProtocol(Protocol):
    
    loggedIn = False

    def connectionMade(self):
        self.transport.write('Maow Server\r\nlogin: ')

    def dataReceived(self, data):
        if not self.loggedIn:
            self.username = data.strip()
            self.loggedIn = True
            self.transport.write('%s@maow> ' % (self.username,))
        else:
            cmd = data.strip()
            if len(cmd) > 0:
                if cmd == "quit":
                    self.transport.loseConnection()
                    return
            self.transport.write('mewmewmew\r\n%s@maow> ' % (self.username,))

factory = Factory()
factory.protocol = MaowProtocol
endpoint = TCP4ServerEndpoint(reactor, 2323)
endpoint.listen(factory)
reactor.run()

