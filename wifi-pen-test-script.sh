#!/bin/bash
#all vars
    #mode
    #file_name
    #cracking_list
    #session_name
    #mode_wifi
    #wordlist_mode
    #options
    #session_name
    #counter
    #file_number
    #wordlist_number
    #installer_mode
#menue
    clear
    echo What do you want to do?
    echo Enter 0 to crack a file in hashcat
    echo Enter 1 to get to the wordlist menue
    echo Enter 2 to restore a session
    echo enter 3 to enter the capture mode
    echo enter 4 to open the dependencie installer
    echo enter 5 to exit
    read -p "Enter the mode: " mode

    while [ $mode != 5 ]; do

        if [ $mode -eq 0 ]
            then
            #ask for file
                #display the list of files
                    clear
                    echo Select the file
                    for i in ./hashcat_files/*; do
                    ((counter++))
                        echo $counter: $i
                    done
                #ask for file
                    read -p "Enter the file number: " file_number
                #reset counter to search for file
                    counter=0
                #search for file
                    for i in ./hashcat_files/*; do
                        ((counter++))
                        if [ $counter -eq $file_number ]
                            then
                            file_name=$i
                        fi
                    done
            #ask for wordlist
                #reset counter to search for wordlist
                    counter=0
                #display the list of Wordlists
                    echo Select the file
                        for i in ./wordlists/*; do
                            ((counter++))
                            echo $counter: $i
                        done
                #ask for wordlist
                    read -p "Enter the wordlist number: " wordlist_number
                #reset counter to search for wordlist
                    counter=0
                #search for wordlist
                    for i in ./wordlists/*; do
                        ((counter++))
                        if [ $counter -eq $wordlist_number ]
                            then
                            cracking_list=$i
                        fi
                    done
            #ask for session name
                clear
                echo Whats the session name?
                read session_name

            ##execute the hashcat command
                hashcat -m 22000 -a 0 --session $session_name $file_name $cracking_list
        fi

        if [ $mode -eq 1 ]
            then
            clear
            echo What do you want to do?
            echo Enter 0 to exit
            echo Enter 1 to start mentalist
            echo Enter 2 to start crunch
            read -p "Enter the mode: " wordlist_mode

            while [ $wordlist_mode != 0 ]; do

                if [ $wordlist_mode -eq 1 ]
                    then
                    echo opening mentalist can take a while so be patient
                    ./Mentalist
                fi
                if [ $wordlist_mode -eq 2 ]
                    then
                    echo please enter all options for crunch
                    read -p "enter options: " options
                    crunch $options
                fi

                clear
                echo What do you want to do?
                echo Enter 0 to exit
                echo Enter 1 to start mentalist
                echo Enter 2 to start crunch
                read -p "Enter the mode: " wordlist_mode

            done
        fi

        if [ $mode -eq 2 ]
            then
            clear
            echo What is the session name
            read session_name
            hashcat --restore --session $session_name
        fi

        if [ $mode -eq 3 ]
            then
            clear
            echo Enter 1 to open airgeddon
            echo Enter 2 to open wireshark
            read -p "Enter the mode: " mode_wifi
            fi
            if [ $mode_wifi -eq 1 ]
            then
                sudo bash ./airgeddon/airgeddon.sh
            fi
            if [ $mode_wifi -eq 2 ]
            then
                sudo wireshark
            fi

        if [ $mode -eq 4 ]
            then
            clear
            echo Enter 1 to install all dependencies
            echo Enter 2 to install only the cracking tools not working right now
            read -p "Enter the mode: " installer_mode
            if [ $installer_mode -eq 1 ]
                then
                    sudo apt update
                    sudo apt install hashcat
                    sudo apt install wireshark
                    sudo apt install crunch
                    sudo apt install python3
                    sudo apt install git
                    sudo apt-get install python3-setuptools py-tk
                    echo airgeddon could not be installed please install manually
                    echo mentalist could not be installed please download the executable and install manually
            fi
        fi
        echo What do you want to do?
        echo Enter 0 to crack a file in hashcat
        echo Enter 1 to get to the wordlist menue
        echo Enter 2 to restore a session
        echo enter 3 to enter the capture mode
        echo enter 4 to open the dependencie installer
        echo enter 5 to exit
        read -p "Enter the mode: " mode
    done

