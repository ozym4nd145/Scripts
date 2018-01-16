#! /bin/bash
rsync -r -t -o -v --progress --modify-window=1 -s /home/suyash1212/Coding /media/500_GB/Backup
rsync -r -t -o -v --progress --modify-window=1 -s /home/suyash1212/bin /media/500_GB/Backup
rsync -r -t -o -v --progress --modify-window=1 -s /home/suyash1212/Screenshots /media/500_GB/Backup
rsync -r -t -o -v --progress --modify-window=1 --max-size='2MB' --exclude-from='/home/suyash1212/bin/exclude_list.txt' -s /home/suyash1212/.config /media/500_GB/Backup/dotfiles
rsync -r -t -o -v --progress --modify-window=1 -s /home/suyash1212/.i3 -c -s /media/500_GB/Backup/dotfiles
rsync -t -v -o -h --progress --modify-window=1 -s /home/suyash1212/.bashrc -c -s /media/500_GB/Backup/dotfiles
rsync -t -v -o -h --progress --modify-window=1 -s /home/suyash1212/.bash_history -c -s /media/500_GB/Backup/dotfiles
rsync -t -v -o -h --progress --modify-window=1 -s /home/suyash1212/.dircolors -c -s /media/500_GB/Backup/dotfiles
rsync -t -v -o -h --progress --modify-window=1 -s /home/suyash1212/.vimrc -c -s /media/500_GB/Backup/dotfiles
rsync -t -v -o -h --progress --modify-window=1 -s /home/suyash1212/.vim -c -s /media/500_GB/Backup/dotfiles
rsync -t -v -o -h --progress --modify-window=1 -s /home/suyash1212/.tmux.conf -c -s /media/500_GB/Backup/dotfiles
rsync -t -v -o -h --progress --modify-window=1 -s /home/suyash1212/.gitconfig -c -s /media/500_GB/Backup/dotfiles
rsync -t -v -o -h --progress --modify-window=1 -s /home/suyash1212/installed_programs.dat -c -s /media/500_GB/Backup/dotfiles
rsync -t -v -o -h --progress --modify-window=1 -s /home/suyash1212/systemlog.txt -c -s /media/500_GB/Backup/dotfiles
rsync -r -t -o -v --progress --modify-window=1 -s /media/500_GB/Important /media/500_GB/Backup

rsync -r -t -o -v --progress --modify-window=1 -s /boot/grub/grub.cfg -c -s /media/500_GB/Backup/sys_config/ --delete

echo "Backup on "$(date) >> ~/logs/backup.log
