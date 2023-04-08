# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.define "node1" do |node1|
    node1.vm.box = "ubuntu/focal64"
    node1.vm.hostname = "lsp-vm-node1"
    node1.vm.network "private_network", ip: "192.168.57.10"
    node1.vm.provider "virtualbox" do |vb|
        vb.name = "lsp-vm-node1"
        vb.memory = "2048"
        vb.cpus = 2
    end
  end
end

