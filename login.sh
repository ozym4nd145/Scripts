#!/bin/bash
LOG=login_output.log
SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE" # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
cd $DIR

read -p "Enter your username: " username
read -sp "Enter your password: " password
echo
read -p "Enter your proxy category: " category
rm -f $LOG
export password=$password
nohup python login_terminal.py $username $category &> $LOG &
sleep 5
echo $(head -n2 $LOG)
addr=`python -c "import login_terminal;login_terminal.Proxy.get_proxy_address('$category')"`
echo "Now run 'set_proxy $addr'"
