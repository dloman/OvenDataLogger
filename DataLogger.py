#!/usr/bin/python

import glob
import serial
import time

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

  Running = True
  with open('OvenData' + time.asctime().replace(' ','-') + '.csv', 'w') as Output:
    while Running:
      try:
        Data = Serial.readline()

        if len(Data) > 2:
          SplitData = Data.split(',')
          if len(SplitData) > 1:
            Output.write(Data)
            Output.flush()
          else:
            print Data
        else:
          if "Reflow is done!" in Data:
            Running = False


      except KeyboardInterrupt:
        exit()
