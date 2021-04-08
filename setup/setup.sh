#!/bin/bash

#****************************************
# $1 => Thema
# $2 => Projekt
# $3 => Ort
# $4 => Protokollführer
# $5 => Gesprächsführer
# $6 => Restliche Teilnehmer
#****************************************

if [ "$1" ]; then
  TOPIC=$1
else
  read -p "Thema des Meetings: " TOPIC
fi

if [ $2 ]; then
  PROJECT=$2
else
  read -p "Projekt: " PROJECT
fi

if [ $3 ]; then
  LOC=$3
else
  read -p "Ort (Online für Onlinemeetings): " LOC
fi

if [ $4 ]; then
  SECRETARY=$4
else
  read -p "Name des Protokollführers: " SECRETARY
fi

if [ $5 ]; then
  LEADER=$5
else
  read -p "Name des Gesprächsführers: " LEADER
fi

if [ $6 ]; then
  PART=$6
else
  read -p "weitere Teilnehmer: " PART
fi

DATE=`date +"%d.%m.%Y"`
DATE_NAME=`date +"%y_%m_%d"`
TIME=`date +"%I:%M"`

cat > meeting_${DATE_NAME}.tex << EOF
\input{./src/config/index}

\begin{document}
  \input{./src/pages/index}
\end{document}
EOF

cat > daten.tex << EOF
\newcommand{\objective}{${TOPIC}} %Thema des Meetings
\newcommand{\project}{${PROJECT}} %Projekt welches im Meeting besprochen wird
\newcommand{\secretary}{${SECRETARY}} %Name des Protokollführers
\newcommand{\leader}{${LEADER}} %Name des Gesprächsführers

\newcommand{\location}{${LOC}} %Ort des Meetings -> Online für Onlinemeetings

\newcommand{\duration}{----} %Dauer des Meetings
\renewcommand{\date}{${DATE}} %Datum des Meetings
\renewcommand{\time}{${TIME}} %Uhrzeit des Meetings

\newcommand{\participants}{${PART}} %Teilnehmer des Meetings
EOF

echo "" > inhalt.tex

echo "Protokoll initialisiert"

#git remote rename origin vorlage
#git branch -m master vorlage-master
#
#if [ ${REPO} ]; then
#  git remote add origin ${REPO}
#
#  git checkout -b master origin/master
#  git push
#else
#  git checkout -b master
#  echo "Keine neue remote Branch übergeben"
#fi
#
#echo "Repository strukturiert"