#!/bin/bash

MINPARAMS=1
if [ $# -lt "$MINPARAMS" ]
then
  echo
  echo "usage: sudo $0 <interface>"
  exit
fi

if (($UID > 0)); then
   echo 'This script can be run only by the system administrator'
   exit
fi

# grab the interface
interface=$1
oldMAC=$(ifconfig $interface | grep HWaddr | awk '{print $5}')
# get the OUI
#OUI=$(ifconfig $interface | grep HWaddr | awk '{print $5}' | cut -b 1-8)
echo "old MAC: $oldMAC"

# get the OUI from a list of legit OUIs
OUI_ARRAY=(
	00:1c:bf # intel
	00:12:f0 # intel
	00:1b:e9 # broadcom
	18:c0:86 # broadcom
	d4:ae:52 # dell
	d4:be:d9 # dell
	00:1d:09 # dell
	d4:c9:ef # hp
	d8:9d:67 # hp
	d8:9e:3f # apple
	d8:a2:5e # apple
)
RANGE=12
idx=$RANDOM
let "idx %= $RANGE"
OUI=${OUI_ARRAY[idx]}

# generate a new NIC specific identifier
NIC=$(date | md5sum | sed 's/../&:/g' | cut -b 9-17)
newMAC="$OUI$NIC"
echo "new MAC: $newMAC"

# assign the new MAC to the interface
echo "Do you wish to assign $newMAC to $interface?"
options=("Yes" "No")
select yn in "${options[@]}"
do
	case $yn in
		"Yes")
				ifconfig $interface down;
				sleep 2 # allow interface to go down
				ifconfig $interface hw ether $newMAC;
				sleep 2 # allow time to assign MAC to interface 
				ifconfig $interface up;
				# display the new MAC
				ifconfig $interface | grep HWaddr;
				break
				;;
		"No") exit
			;;
	esac
done
