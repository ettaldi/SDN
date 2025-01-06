from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.topo import Topo
from mininet.cli import CLI

class Topology(Topo):
    def build(self):
        switch = self.addSwitch('s1')

        host1 = self.addHost('h1', ip='192.168.139.5/24')
        host2 = self.addHost('h2', ip='192.168.139.6/24')
        host3 = self.addHost('h3', ip='192.168.139.7/24')

        self.addLink(host1, switch)
        self.addLink(host2, switch)
        self.addLink(host3, switch)


net = Mininet(topo=Topology(), controller=None)

controller = RemoteController('c0', ip=, port=6633)
net.addController(controller)

net.start()

CLI(net)
