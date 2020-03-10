FROM pxl_air_opencv:latest


USER root

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils python3-pip xdotool


RUN set -x && apt-get update \
        && apt-get upgrade -y
RUN python3 -m pip install --upgrade pip setuptools
RUN python3 -m pip install PyQt5 imutils
COPY requirements.txt /tmp/base_requirements.txt 

RUN set -x && python3 -m pip install -r /tmp/base_requirements.txt 
ADD app_icon.png /usr/share/pixmaps/


USER user
WORKDIR /home/user
RUN sudo usermod -a -G video user
RUN sudo echo "alias python=python3" >> ~/.bashrc && sudo apt-get update -y && sudo apt-get install -y libxkbcommon-x11-0
STOPSIGNAL SIGTERM


ENTRYPOINT ["/scripts/init_commands.sh"]
CMD sudo service ssh start && /bin/bash 

