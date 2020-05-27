#ScriptName: pip.sh
#Author: kshekara
#Description:Easier way to pip new modules it's bullshit - Just a wrapper for pip
###################################################################
if [ $1 != '' ]
then
    echo "Installing $1"
    echo "sudo apt-get install $1"  
    sudo apt-get install $1
fi

if [$1 == '']
then   
    echo ""
    echo "******"
    echo "Babe pls give something to pip!!"
    echo "******"
fi
