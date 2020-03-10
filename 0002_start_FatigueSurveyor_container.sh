#!/bin/bash
if [ "$(docker ps -a | grep fatigue_surveyor)" ]; then
	docker container stop fatigue_surveyor
fi
(cd ./FatigueSurveyorContainer; ./Start_FatigueSurveyorContainer.sh)
