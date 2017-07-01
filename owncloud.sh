#! /bin/bash
rsync -r -t -o -v --progress --modify-window=1 -s /home/suyash1212/Coding /media/500_GB/Backup --delete
rsync -r -t -o -v --progress --modify-window=1 -s /home/suyash1212/bin /media/500_GB/Backup --delete
rsync -r -t -o -v --progress --modify-window=1 -s /home/suyash1212/Screenshots /media/500_GB/Backup --delete

rsync -r -t -o -v --progress --modify-window=1 -s /home/suyash1212/.config/dconf /media/500_GB/Backup/dotfiles/.config --delete
rsync -r -t -o -v --progress --modify-window=1 -s /home/suyash1212/.config/dunst /media/500_GB/Backup/dotfiles/.config --delete
rsync -r -t -o -v --progress --modify-window=1 -s /home/suyash1212/.config/touchegg /media/500_GB/Backup/dotfiles/.config --delete
rsync -r -t -o -v --progress --modify-window=1 -s /home/suyash1212/.solarized /media/500_GB/Backup/dotfiles --delete

rsync -r -t -o -v --progress --modify-window=1 -s /home/suyash1212/.i3 -c -s /media/500_GB/Backup/dotfiles/ --delete
rsync -t -v -o -h --progress --modify-window=1 -s /home/suyash1212/.bashrc -c -s /media/500_GB/Backup/dotfiles/
rsync -t -v -o -h --progress --modify-window=1 -s /home/suyash1212/.bash_history -c -s /media/500_GB/Backup/dotfiles/
rsync -t -v -o -h --progress --modify-window=1 -s /home/suyash1212/.dircolors -c -s /media/500_GB/Backup/dotfiles/
rsync -t -v -o -h --progress --modify-window=1 -s /home/suyash1212/.vimrc -c -s /media/500_GB/Backup/dotfiles/
rsync -t -v -o -h --progress --modify-window=1 -s /home/suyash1212/.tmux.conf -c -s /media/500_GB/Backup/dotfiles/
rsync -t -v -o -h --progress --modify-window=1 -s /home/suyash1212/.gitconfig -c -s /media/500_GB/Backup/dotfiles/
rsync -t -v -o -h --progress --modify-window=1 -s /home/suyash1212/installed_programs.dat -c -s /media/500_GB/Backup/dotfiles/
rsync -t -v -o -h --progress --modify-window=1 -s /home/suyash1212/systemlog.txt -c -s /media/500_GB/Backup/dotfiles/
rsync -r -t -o -v --progress --modify-window=1 -s /media/500_GB/Important /media/500_GB/Backup --delete

echo "Backup on "$(date) >> ~/logs/backup.log

