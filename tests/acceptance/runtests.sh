#! /bin/sh

if [ ! $1 ];
then
    # We need an environment to run robot tests
	echo ERROR: No environment passed 1>&2
    exit 1 # terminate and indicate error
fi

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Execute the robot tests, designating the output directory
robot --variable ENVIRONMENT:"$1" --outputdir $DIR/results $DIR/robot/
