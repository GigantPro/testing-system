#!/bin/sh

SOURCE_FILE=./edu.nginx.conf
PATH_TO_FILE=/etc/nginx/conf.d/edu.nginx.conf
if test -f "$PATH_TO_FILE"; then
    if cmp -s $SOURCE_FILE $PATH_TO_FILE ; then
        echo $SOURCE_FILE == $PATH_TO_FILE
    else
        sudo rm $PATH_TO_FILE
        sudo cp $SOURCE_FILE $PATH_TO_FILE

        echo "Nginx config file updated! Restarting..."
        sudo systemctl restart nginx
    fi
else 
    echo "$SOURCE_FILE does not exist. Copying..."
    sudo cp $SOURCE_FILE $PATH_TO_FILE

    echo "Nginx config file updated! Restarting..." 
    sudo systemctl restart nginx
fi
echo "Nginx config loaded!"

sudo docker-compose -f /opt/xiver/testing-system/docker-compose.yml up --build
