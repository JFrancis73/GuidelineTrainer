# GuidelineTrainer
Real world application of billiards/pool/snooker guide-line trainer for beginners of the game.
Billiards, pool, or snooker are popular cue sports that require precision, strategy, and skill. However, for beginners, these games can be daunting and difficult to learn, especially when it comes to aiming shots. To help newcomers to the game develop their aiming skills, a guide-line trainer can be a valuable tool. 

This tool analyses the angle at which the player is holding the cue with respect to the cue ball and uses predictive physics to forecast the path of the cue ball and that of the balls it collides with. This analysis is projected in an animation using matplotlib where the user can view the path of the collision of his/her screen. Further OpenCV is used to analyze the current state and positions of balls on the board.

This is a simple tool that can be added to any existing pool table at an insignificant markup over the original price and for this reason will have an invaluable impact on the game and will encourage new players and motivate novices of the game to better their skills.



<h2>Instructions for use:</h2>
 Connect the Arduino according to the descriptions provided in the links below:
-    https://iotprojectsideas.com/measure-pitch-roll-and-yaw-angles-using-mpu6050-and-arduino/
-    https://circuitdigest.com/microcontroller-projects/interfacing-ir-sensor-module-with-arduino
   
Arduino Connection Explained:
-   Connect gnd on arduino to the ground on the MPU6050 sensor and the IR sensor
-   Connect 5V on arduino to the Vcc on the MPU6050 and the IR sensor
-   MPU6050:
    -    Connect analog IN A4 and A5 on the arduino to the SDA and SLC pins respectively
-   IR sensor:
    -    Connect OUT pin to the ~9 digital pin of the arduino

 further, refer to the images in PICS folder to understand the full connection.
 To deploy arduino code, download arduino IDE, identify the port occupied by the arduino and verify and upload the code into the device. make sure that all connections have been made prior
 
 clone the repo locally and install the necessary packages from requirements.txt.
 
 run the file plot.py to see the results in a popup window by matplotlib.

