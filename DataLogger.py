#!/usr/bin/python

import glob
import serial
import datetime

################################################################################
################################################################################
def GetSerialPort():
  for ttyName in glob.glob('/dev/ttyACM*'):
    try:
     print 'trying motor controller on', ttyName
     Serial = serial.Serial(ttyName, 115200, timeout=.1)
     print 'Connected on to motor controller on', ttyName
     return Serial
    except:
      Serial = None
      pass

################################################################################
################################################################################
if __name__ == "__main__":
  Serial = GetSerialPort()

  if Serial is None:
    print "ERROR: Couldnt Connect to serial"
    exit()

  with open('OvenData' + str(datetime.date.today()) + '.csv', 'w') as Output:
    while True:
      try:
        Data = Serial.readline()

        if len(Data) > 0:
          SplitData = Data.split(',')
          if len(SplitData) > 1:
            Output.write(Data)
            Output.flush()
          else:
            print Data

      except KeyboardInterrupt:
        exit()
