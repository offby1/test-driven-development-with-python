# -*- mode: ruby -*-

Vagrant.configure(2) do |config|
  config.vm.box = "trusty64-updated-vboxguest"
  config.vm.network :forwarded_port, guest: 80, host: 8080
end
