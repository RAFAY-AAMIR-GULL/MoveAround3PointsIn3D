from controller import Robot
import math
import random
from ikpy.chain import Chain
from ikpy.link import OriginLink, URDFLink

from controller import AnsiCodes

print("This is " + AnsiCodes.RED_FOREGROUND + "red" + AnsiCodes.RESET + "!")



robot=Robot()
timestep=64

shoulder_pan_joint_sensor=robot.getDevice("shoulder_lift_joint_sensor")
shoulder_pan_joint_sensor.enable(timestep)
shoulder_pan_joint=robot.getDevice("shoulder_pan_joint")
shoulder_pan_joint.setPosition(float('inf'))
shoulder_pan_joint.setPosition(0)

shoulder_lift_joint_sensor=robot.getDevice("shoulder_lift_joint_sensor")
shoulder_lift_joint_sensor.enable(timestep)
shoulder_lift_joint=robot.getDevice("shoulder_lift_joint")
shoulder_lift_joint.setPosition(float('inf'))
shoulder_lift_joint.setPosition(0) #-1.5708=90deg


elbow_joint_sensor=robot.getDevice("elbow_joint_sensor")
elbow_joint_sensor.enable(timestep)
elbow_joint=robot.getDevice("elbow_joint")
elbow_joint.setPosition(float('inf'))
elbow_joint.setVelocity(0)


wrist_1_joint_sensor=robot.getDevice("wrist_1_joint_sensor")
wrist_1_joint_sensor.enable(timestep)
wrist_1_joint=robot.getDevice("wrist_1_joint")
wrist_1_joint.setPosition(float('inf'))
wrist_1_joint.setPosition(0)

wrist_2_joint_sensor=robot.getDevice("wrist_2_joint_sensor")
wrist_2_joint_sensor.enable(timestep)
wrist_2_joint=robot.getDevice("wrist_2_joint")
wrist_2_joint.setPosition(float('inf'))
wrist_2_joint.setPosition(0)

wrist_3_joint_sensor=robot.getDevice("wrist_3_joint_sensor")
wrist_3_joint_sensor.enable(timestep)
wrist_3_joint=robot.getDevice("wrist_3_joint")
wrist_3_joint.setPosition(float('inf'))
wrist_3_joint.setPosition(0)
    
    
    
def rand():
    return [0.01*random.randrange(-200, 200),0.01*random.randrange(-200, 200),0.01*random.randrange(-200, 200)]


def setposition(jointang):
    shoulder_pan_joint.setPosition(jointang[1])
    shoulder_pan_joint.setVelocity(1)
    
    shoulder_lift_joint.setPosition(-jointang[2])
    shoulder_lift_joint.setVelocity(1)
      
    elbow_joint.setPosition(-6.38+(3.14+jointang[3]))
    elbow_joint.setVelocity(1)
         
    wrist_1_joint.setPosition(jointang[4])
    wrist_1_joint.setVelocity(1)
    
    wrist_2_joint.setPosition(jointang[5])
    wrist_2_joint.setVelocity(1)
    
    wrist_3_joint.setPosition(jointang[6])
    wrist_3_joint.setVelocity(1)

def main():
    
    
    
    
    my_chain = Chain.from_urdf_file("D:/Webots/controllers/IK_Practice/ikpy_master/resources/poppy_ergo.URDF")
    left_arm_chain = Chain(name='left_arm', links=[
    OriginLink(),
    URDFLink(
      name="shoulder",
      origin_translation=[-10, 0, 5],
      origin_orientation=[0, 1.57, 0],
      rotation=[0, 1, 0],
    ),
    URDFLink(
      name="elbow",
      origin_translation=[25, 0, 0],
      origin_orientation=[0, 0, 0],
      rotation=[0, 1, 0],
    ),
    URDFLink(
      name="wrist",
      origin_translation=[22, 0, 0],
      origin_orientation=[0, 0, 0],
      rotation=[0, 1, 0],
    )
    ])

  
    print("Inverse Kinematics:  ")
    randomposition=rand()
    print("It is the rest position: X, Y, Z: ", end ="")
    print(randomposition)
    
    jointang = my_chain.inverse_kinematics(target_position=randomposition)
    # jointang=my_chain.inverse_kinematics(target_position=[-.2,.7,-.7])
    print(jointang)
    
    
    
    counter=0
    while robot.step(timestep)!=-1:
        
    
        if counter==1:
            setposition(jointang)
                
                
        if counter ==100:
            print("\n\n\n")
            print("Inverse Kinematics:  ")
            ranposition=rand()
            print("Point %s is: X, Y, Z: " %(1), end="")
            print(ranposition)
            
            jointangles=my_chain.inverse_kinematics(target_position=ranposition)
            # jointang=my_chain.inverse_kinematics(target_position=[-.2,.7,-.7])
            print(jointangles)
            print("\n\n\n")
            setposition(jointangles)    
                
            
        if counter == 200:
            print("\n\n\n")
            print("Inverse Kinematics:  ")
            ranposition=rand()
            print("Point %s is: X, Y, Z: " %(2), end="")
            print(ranposition)
            
            jointangles=my_chain.inverse_kinematics(target_position=ranposition)
            # jointang=my_chain.inverse_kinematics(target_position=[-.2,.7,-.7])
            print(jointangles)
            print("\n\n\n")
            setposition(jointangles) 
        
        if counter == 300:
            print("\n\n\n")
            print("Inverse Kinematics:  ")
            ranposition=rand()
            print("Point %s is: X, Y, Z: " %3, end="")
            print(ranposition)
            
            jointangles=my_chain.inverse_kinematics(target_position=ranposition)
            # jointang=my_chain.inverse_kinematics(target_position=[-.2,.7,-.7])
            print(jointangles)
            print("\n\n\n")
            setposition(jointangles)
            
            
        if counter == 400:
            print("\n\n\n")
            print("Back to rest position: X, Y, Z: ", end ="")
            print(randomposition)
             # jointang=my_chain.inverse_kinematics(target_position=[-.2,.7,-.7])
            print(jointang)
            print("\n\n\n")
            setposition(jointang)
            
            
          
        counter+=1


if __name__=="__main__":
    main()