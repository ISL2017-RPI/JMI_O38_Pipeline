FROM keyi/python2-mcr2017a-rpi-isl

COPY JMI_O38/ ./JMI_O38
COPY O38_JMI_wrapper.py ./
COPY setup.py ./
COPY trainData.csv ./
COPY trainTargets.csv ./
