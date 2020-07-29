from os import system as sc
from lib.zsh_c import prompt


#DEPRECATED FOR FZSH 0.9+


############# CONSTANTES #####################

ROOT = "~/Documents/"
OMZ_GIT = "https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh"
FZSH_GIT = "http://github.com/Neltarim/faster-zsh.git"
CHROME = "google-chrome-stable"
APT = "sudo apt-get install "

############# /CONSTANTES ####################

prompt("Installing major packages ...")

sc("{}curl zsh git python3.6 pip virtualenv {}".format(APT, CHROME))
sc("{}snap".format(APT))
sc("sudo snap install hub")

prompt("installing oh-my-zsh ...")
sc("sh -c \"$(curl -fsSL {})\"".format(OMZ_GIT))

prompt("Installing custom ZSH profile ...")
sc("git clone {}".format(FZSH_GIT))
sc("cp ./zsh-profile/code_aliases.zsh ~/.oh-my-zsh/custom/")
sc("source ~/zshrc")