from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.topo import Topo
from mininet.cli import CLI

class Topology(Topo):
    def build(self):
 
        switch1 = self.addSwitch('s1')
        switch2 = self.addSwitch('s2')
        
        host1 = self.addHost('h1', ip='192.168.1.1/24')
        host2 = self.addHost('h2', ip='192.168.1.2/24')
        host3 = self.addHost('h3', ip='192.168.1.3/24')
        host4 = self.addHost('h4', ip='192.168.1.4/24')
        
        self.addLink(host1, switch1)
        self.addLink(host2, switch1)
        self.addLink(host3, switch2)
        self.addLink(host4, switch2)
        
        self.addLink(switch1, switch2)


net = Mininet(topo=Topology(), controller=None)

controller = RemoteController('c0', ip=, port=6633)
net.addController(controller)

net.start()

CLI(net)

net.stop()
