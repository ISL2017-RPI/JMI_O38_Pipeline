# JMI_O38_Pipeline

This is the source code for our JMI primitive on the seed data O38.

Once you clone this folder into your local repo, you can directly build the Docker image by:

docker build -t jmi38 ./

Then, you can run the pipeline script in the following way:

docker run jmi38 python O38_JMI_wrapper.py "trainData.csv" "trainTargets.csv" 12

The output is the selected features stored in a csv file
