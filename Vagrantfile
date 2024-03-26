Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"
  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update
    sudo apt-get install -y docker.io
    sudo usermod -aG docker vagrant
  SHELL
  config.vm.synced_folder ".", "/vagrant", disabled: false
  config.vm.network "forwarded_port", guest: 30000, host: 30000
end
