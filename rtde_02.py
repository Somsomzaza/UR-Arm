#!/usr/bin/env python
# encoding: utf=8

""" 
#UR Controller Primary Client Interface Reader
# For software version 3.0
#
# Datastream info found here: http://support.universal-robots.com/Technical/PrimaryAndSecondaryClientInterface
# Struct library used to extract data, info found here: https://docs.python.org/2/library/struct.html
"""

import socket, time

robot = '10.10.0.61'
port = 30003
gripper_port  = 63352

#####################################################################################################################
#Establish connection to controller
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect((robot, port))
#####################################################################################################################

g = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
g.connect((robot, gripper_port))
g.send(b'SET ACT 1\n')
time.sleep(3)
g.send(b'SET GTO 1\n')
g.send(b'SET SPE 255\n')
g.send(b'SET FOR 255\n')
g.send(b'SET POS 0\n')


def main():
        # pos = [i/1000 for i in [-35.88,-370.43,-67.04]] + [3.164, -0.052, -0.050]
        # pos_str = str(pos)
        # home = [-0.03588, -0.37043, -0.06704, 3.164, -0.052, -0.05,0]
        s.send(b'movel(p[-0.18003, -0.3300, -0.3000, 3.167, -0.078, 0.27], 1, 0.5, 0, 0)\n')
        time.sleep(1)
        s.send(b'movel(p[-0.18003, -0.3300, -0.3300, 3.167, -0.078, 0.27], 1, 0.5, 0, 0)\n')
        time.sleep(1)
        g.send(b'SET POS 255\n')
        time.sleep(1)
        s.send(b'movel(p[-0.18003, -0.3300, -0.2000, 3.167, -0.078, 0.27], 1, 0.5, 0, 0)\n')
        time.sleep(1)
        s.send(b'movel(p[0.1600, -0.3300, -0.2000, 3.167, -0.078, 0.27], 1, 0.5, 0, 0)\n')
        time.sleep(1)
        s.send(b'movel(p[0.1600, -0.3300, -0.3300, 3.167, -0.078, 0.27], 1, 0.5, 0, 0)\n')
        time.sleep(1)
        g.send(b'SET POS 0\n')
        time.sleep(1)
        s.send(b'movel(p[0.1600, -0.3300, -0.2000, 3.167, -0.078, 0.27], 1, 0.5, 0, 0)\n')
        time.sleep(1)
        
if __name__ == '__main__': 
    import sys
    main()

