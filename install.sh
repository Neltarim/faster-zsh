sudo apt-get install git
sudo apt-get install curl
zsh
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
git clone http://github.com/Neltarim/faster-zsh.git ~/Documents/faster-zsh
cp ~/Documents/faster-zsh/code_aliases.sh ~/.oh-my-zsh/custom/
source ~/.zshrc

sudo pip3 install --upgrade setuptools
sudo pip3 install --upgrade pip3
sudo apt-get install libmysqlclient-dev
sudo pip3 install mysql
sudo pip3 install mysql-connector-python

echo "Faster-zsh installed successfuly.\nTry \"finstall\" to install more usefuls programs."
