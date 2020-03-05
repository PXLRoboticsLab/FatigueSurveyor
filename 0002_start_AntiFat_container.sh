#!/bin/bash
if [ "$(docker ps -a | grep anti_fatigue)" ]; then
	docker container stop anti_fatigue
fi
(cd ./AntiFatigueApp; ./AntiFat_start_container.sh)
