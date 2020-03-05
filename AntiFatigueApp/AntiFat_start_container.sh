#!/bin/bash

xhost +local:docker

# --device=/dev/video0:/dev/video0
# For non root usage:
# RUN sudo usermod -a -G video developer

vendor=`glxinfo | grep vendor | grep OpenGL | awk '{ print $4 }'`

if [ $vendor == "NVIDIA" ]; then
    docker run -it \
        --device /dev/snd \
	--rm \
	-d \
        --env="DISPLAY" \
        --env="QT_X11_NO_MITSHM=1" \
        --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
        -v `pwd`/../Projects:/home/user/Projects \
        -env="XAUTHORITY=$XAUTH" \
        --volume="$XAUTH:$XAUTH" \
        --runtime=nvidia \
	-w="/home/user/Projects/Python/AntiFatigueApp/src" \
        --device=/dev/video0:/dev/video0 \
	--name anti_fatigue \
        anti_fatigue_app:latest \
        bash &&
    docker container exec -it anti_fatigue bash -c 'xdotool windowminimize $(xdotool getactivewindow) & python3 main.py'    && docker container stop anti_fatigue  && echo "removed container" && exit
    
else
    docker run --privileged -it --rm \
	-d \
        --volume=/tmp/.X11-unix:/tmp/.X11-unix \
        -v `pwd`/../Projects:/home/user/Projects \
        --device=/dev/dri:/dev/dri \
        --env="DISPLAY=$DISPLAY" \
        -e "TERM=xterm-256color" \
	-w="/home/user/Projects/Python/AntiFatigueApp/src" \
        --cap-add SYS_ADMIN --device /dev/fuse \
	--name AntiFatigue \
        anti_fatigue_app:latest \
        bash &&
    docker container exec -it anti_fatigue bash -c 'python3 main.py' && exit && docker container stop anti_fatigue 
fi 
