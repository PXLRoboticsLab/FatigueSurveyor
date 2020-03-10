#!/bin/bash
if [ "$(docker ps -a | grep anti_fatigue)" ]; then
	docker container stop anti_fatigue
fi
(cd ./FatigueSurveyorContainer; ./Start_FatigueSurveyorContainer.sh)
