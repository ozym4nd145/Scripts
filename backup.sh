#! /bin/bash
rsync -r -t -o -v --progress --modify-window=1 -s /home/suyash1212/Coding /media/suyash1212/Suyash_1TB/Backup
rsync -r -t -o -v --progress --modify-window=1 -s /home/suyash1212/bin /media/suyash1212/Suyash_1TB/Backup
rsync -r -t -o -v --progress --modify-window=1 -s /home/suyash1212/Screenshots /media/suyash1212/Suyash_1TB/Backup
rsync -r -t -o -v --progress --modify-window=1 -s /home/suyash1212/.config /media/suyash1212/Suyash_1TB/Backup/dotfiles
rsync -r -t -o -v --progress --modify-window=1 -s /home/suyash1212/.i3 -c -s /media/suyash1212/Suyash_1TB/Backup/dotfiles
rsync -t -v -o -h --progress --modify-window=1 -s /home/suyash1212/.bashrc -c -s /media/suyash1212/Suyash_1TB/Backup/dotfiles
rsync -t -v -o -h --progress --modify-window=1 -s /home/suyash1212/.bash_history -c -s /media/suyash1212/Suyash_1TB/Backup/dotfiles
rsync -t -v -o -h --progress --modify-window=1 -s /home/suyash1212/.dircolors -c -s /media/suyash1212/Suyash_1TB/Backup/dotfiles
rsync -t -v -o -h --progress --modify-window=1 -s /home/suyash1212/.vimrc -c -s /media/suyash1212/Suyash_1TB/Backup/dotfiles
rsync -t -v -o -h --progress --modify-window=1 -s /home/suyash1212/.vim -c -s /media/suyash1212/Suyash_1TB/Backup/dotfiles
rsync -t -v -o -h --progress --modify-window=1 -s /home/suyash1212/.tmux.conf -c -s /media/suyash1212/Suyash_1TB/Backup/dotfiles
rsync -t -v -o -h --progress --modify-window=1 -s /home/suyash1212/.gitconfig -c -s /media/suyash1212/Suyash_1TB/Backup/dotfiles
rsync -t -v -o -h --progress --modify-window=1 -s /home/suyash1212/installed_programs.dat -c -s /media/suyash1212/Suyash_1TB/Backup/dotfiles
rsync -t -v -o -h --progress --modify-window=1 -s /home/suyash1212/systemlog.txt -c -s /media/suyash1212/Suyash_1TB/Backup/dotfiles
rsync -r -t -o -v --progress --modify-window=1 -s /media/500_GB/Important /media/suyash1212/Suyash_1TB/Backup
