#alias control
alias aliasedit='vi ~/Documents/faster-zsh/code_aliases.zsh'
alias src='source ~/.zshrc'
alias aliasshow='cat ~/.oh-my-zsh/custom/code_aliases.zsh'
alias aliassave='py ~/Documents/faster-zsh/alias_starter.py aliassave'

#wifi
alias wifi='nmcli'
alias wifisaved='nmcli c'

#python
alias py='python3'
alias py2='python2'
alias supy='sudo python3'

#virtualenv
alias envnew='virtualenv -p python3 env'
alias envstart='source env/bin/activate'
alias envstop='deactivate'
alias envdelete='rm -rf ./env/'

#shadow
alias shadow='~/Shadow.AppImage'

#VS code
alias vs='code .'
alias vsdir='code ..'

#againPy
alias again='python3 ~/Documents/againPy/again.py'

#zsh
alias rm='rm -rf'
alias rmrf='sudo rm -rf'
alias mk='mkdir'
alias doc='cd ~/Documents/ && l'
alias term='gnome-terminal'
alias aliasup='py ~/Documents/faster-zsh/alias_starter.py aliasup'
alias ap='cd ~/Documents/project_5/purBeurre/core && l'
alias learn='cd ~/Documents/python-learning/advanced && l'
alias pp='cd ~/Documents/faster-zsh/ && l'
alias trash='cd ~/Documents/trash/ && l'
alias safe='cd ~/Documents/safezone/ && l'
alias web='cd ~/Documents/websites-clients/PCwebsite/ && l'

alias retry='py ~/Documents/project_5/purBeurre/uninstall.py && py ~/Documents/project_5/purBeurre/install.py'

#faster zsh
alias fzh='py ~/Documents/faster-zsh/alias_starter.py'
alias hello='py ~/Documents/faster-zsh/hello.py && doc'
alias gitnew='hub init && hub create'
alias gitdel='fzsh gitdel'
alias gitpush='fzsh gitpush'
alias newdev='fzsh newdevice'
alias rmpr='fzsh rmpr'
alias chnpr='fzsh chnpr'
alias bright='fzsh bright'
alias gitimport='fzsh gitimport'
alias gitrez='fzsh gitreload'
alias hardpush='fzsh hardpush'
alias apt='fzsh apt'
alias mysqlScript='fzsh msqlScript'
alias gitapi='py ~/Documents/python-learning/API/github_API.py'

#pip
alias pip='sudo pip3'
alias pipm='python3 -m pip3'
alias freeze='pip3 freeze > requirements.txt'

#django
alias djangonew='django-admin startproject'
alias djangostart='python3 manage.py runserver'

#postgres
alias pgstart='sudo -i -u postgres'
alias pgnew='sudo createdb -O neltarim'

#mysql
alias mysql='sudo mysql -h localhost -u root -p'

#keyboard control
alias xin='xinput set-prop 9 305 1'
alias fr='setxkbmap fr'
alias us='setxkbmap us'

#Windows tilling manager
alias wsave='i3-save-tree --workspace 1 > ~/.i3/workspace-1.json'
alias isave='i3-resurrect save -w'
alias iload='i3-resurrect restore -w'
alias chrome='i3-resurrect restore -w 2'
alias logout='gnome-session-quit'
