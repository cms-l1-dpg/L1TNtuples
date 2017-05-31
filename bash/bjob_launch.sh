#!/bin/bash
# Lxplus Batch Job Script

## 
## usage
## bjob_launch.sh <configuration file name> <cfg file directory> <input file path> <input file name> <output file >


if [ -n "$1" ]
    then
    CFG_FILE=$1
fi

if [ -n "$2" ]
    then 
    WRK=$2
fi

if [ -n "$3" ]
    then 
    INPUTFILEPATH=$3
fi

if [ -n "$4" ]
    then 
    INPUTFILE=$4
fi

echo $WRK
cd $WRK

#set the environment - todo : take it from the environment where the job in laucnhed
export SCRAM_ARCH=slc6_amd64_gcc530
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh
eval `scramv1 runtime -sh`

echo cmsRun $WRK/$CFG_FILE $INPUTFILEPATH $INPUTFILE
cmsRun $WRK/$CFG_FILE $INPUTFILEPATH $INPUTFILE 

OUTPUTFILE=""
if [ -n "$5" ]
    then
    OUTPUTFILE=$5
fi

STOREDIR=/eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2017/Stage2/NanoDST/$USER/
echo $STOREDIR
if [ ! -d "$STOREDIR" ]
    then
    mkdir $STOREDIR
fi


if [ -n "$OUTPUTFILE" ]
    then
    cp $OUTPUTFILE $STOREDIR`basename $OUTPUTFILE`
    rm -rf $OUTPUTFILE
fi
#exit
