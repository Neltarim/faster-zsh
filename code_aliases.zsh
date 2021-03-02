#alias control
alias aliasedit='vi ~/Documents/faster-zsh/code_aliases.zsh'
alias src='source ~/.zshrc'
alias aliasshow='cat ~/.oh-my-zsh/custom/code_aliases.zsh'
alias aliassave='py ~/Documents/faster-zsh/alias_starter.py aliassave'

#network
alias wifi='nmcli'
alias wifisaved='nmcli c'
alias scanport='sudo netstat -lpn |grep'

#python
alias py='python3'
alias py2='python2'
alias supy='sudo python3'
alias pudb='sudo pudb3'

#virtualenv
alias envnew='virtualenv -p python3 env'
alias envstart='source env/bin/activate'
alias envstop='deactivate'

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
alias ap='cd ~/Documents/Project_5/ && l'
alias learn='cd ~/Documents/python-learning/advanced && l'
alias pp='cd ~/Documents/faster-zsh/ && l'
alias trash='cd ~/Documents/trash/ && l'
alias safe='cd ~/Documents/safezone/ && l'
alias web='cd ~/Documents/websites-clients/PCwebsite/ && l'

alias retry='py ~/Documents/project_5/purBeurre/uninstall.py && py ~/Documents/project_5/purBeurre/install.py'

#faster zsh
alias fzsh='py ~/Documents/faster-zsh/alias_starter.py'
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
alias fcolors='fzsh color'
alias mysqlscript='fzsh msqlscript'
alias gitapi='py ~/Documents/python-learning/API/github_API.py'
alias bastion='fzsh bastion'
alias scout='fzsh scout'
alias quicksql='fzsh quicksql'
alias msqlreset='fzsh msqlreset'
alias wmove='fzsh wmove'
alias killport='fzsh killport'
alias delcache='fzsh delcache'
alias brightfor='fzsh brightfor'
alias newflask='fzsh newflask'
alias exponew='fzsh exponew'
alias rchmod='fzsh rchmod'
alias finstaller='fzsh finstaller'
alias fgitinit="fzsh fgitinit"
alias hrconsole='fzsh herokuconsole'
alias djmanager='fzsh djmanager'

#pip
alias pip='sudo pip3'
alias pipm='python3 -m pip3'
alias freeze='pip3 freeze > requirements.txt && cat requirements.txt'
alias pipreq='pip install -r requirements.txt'


#django & flask
alias dj='python3 manage.py'
alias djnew='django-admin startproject'
alias djstart='python3 manage.py runserver'
alias djmigrate='python3 manage.py migrate'
alias djnewapp='django-admin startapp'
alias djtmpl='fzsh djtmpl'

alias flask='FLASK_APP=run.py flask'

#JavaScript
alias npm='sudo npm'
alias reactnew='sudo create-react-app'

#mysql
alias sqleasyscript='mysql -h localhost -u root'
alias mysqlconsole='sudo mysql -h localhost -u root -p'
alias mysqlreload='sudo systemctl daemon-reload && sudo systemctl restart mysql'

#postgres
alias pgstart='sudo -i -u postgres'
alias pgnew='sudo createdb -O neltarim'

#keyboard control
alias xin='xinput set-prop 10 "libinput Tapping Enabled" 1'
alias fr='setxkbmap fr'
alias us='setxkbmap us'

#i3 windows tilling manager
alias wsave='i3-save-tree --workspace 1 > ~/.i3/workspace-1.json'
alias isave='i3-resurrect save -w'
alias iload='i3-resurrect restore -w'
alias chrome='i3-resurrect restore -w 2'
alias logout='gnome-session-quit'
alias autosleep='xset -dpms'
