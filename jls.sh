#!/bin/bash

FILE=$(date '+%Y-%m-%d')_LessonPlan.odt

#if [ -e! "./$FILE" ]
#then
    cp ~/Templates/TextDocument.odt ~/JLS/
    mv ~/JLS/TextDocument.odt ~/JLS/"$FILE"
    libreoffice ~/JLS/"$FILE"
#else
#    libreoffice ./"$FILE"
#fi
