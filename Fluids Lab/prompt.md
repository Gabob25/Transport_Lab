# Prompt Log

## Prompt 1

> Alright copilot, we need to create a program where we can estimate some values of a rising bubble from a video i took with my phone. The bubble is formed in three separate liquids thats why i sent you 3 mp4 videos. I need you to verify you can access them. This is all for a lab report of fluid transport experiment. I will give you further instructions, but for now confirm you can access the videos, and create a prompt.md file where you record, starting from this one, all the prompts i text you and save it in the fluids lab folder next to the videos,

## Prompt 2

> Can you open each video and display every 10 frames, so we can follow the bubble movement. Add a slider so i can manually move through each frame

## Prompt 3

> This works. Can you modify it so that the slider only lets you select every 10 frames for each video. Keep everything else the same.

## Prompt 4

> Perfect. Can you change just the oil and the water slider to select every 5 frames as the bubble moves too quickly.

## Prompt 5

> Now we want to track the bubbles position over time. You dont need to automatically track it, just let me track it manually by clicking the center of the bubble at each selected frame.

## Prompt 6

> Can you make the pointer one fourth of its size and let me zoom in and out of the frame

## Prompt 7

> Can you allow me to move around the image by clicking and dragging

## Prompt 8

> Now we need to be able to convert pixels into cms using the ruler next to the liquid. I need you to give the option to switch between center marking mode and length calibration mode. For the center marking mode keep everything as we have now. When i select length mode, i need to be able to click on two points on their image and you need to draw a straight line between and find the number of pixles of that line. Also let me zoom and move around in that mode as well.

## Prompt 9

> Continue recording the prompts after this one. Now based on the data i provide for the center of the bubble, you need to extrapolate and associate each bubble position with the correct video time.

## Prompt 10

> Can you access the the data the user inputs in the manual position and calculate it from there. Also only do it every 10 frames for glycerol and every 5 frames for water and oil

## Prompt 11

> Now using the values provided by the user in the manual position log, and create a plot position vs time, and another one velocity vs time, with units and labeled axes

## Prompt 12

> So for the graphs, consider the center bottom of the flask as the origin. Also, only consider the positions and velocitites in y

## Prompt 13

> Now, using the values obtained in the log calculate the terminal velocity

## Prompt 14

> I uploaded a new screenshot in the fluids lab folder, with the mass and volume of each fluid, calculate their densities and added on the selected liquid characteristics, below frame count. Also can you add a new section like the one for the other liquids, that uses the new stokes reference.mp4 video i uploaded as well.

## Prompt 15

> change the stoke reference slider to every 10 frames

## Prompt 16

> Now we need to find the radius of the bubble. To do this lets use the length calibration mode but add a new option for the radius

## Prompt 17

> I wanted you to include the radius option inside the length calibration so you can inmediately find the radius in cm from the calibration set prior. Inside length calibration, below the pixles to cm convertor, add the bubble radius mode

## Prompt 18

> Perfect. Now we need to calculate the viscosity for each fluid. To do this we are going to use an approximate stokes model we adopted in the laboratory. Could you add below the terminal velocity estimate, a procedure where you first include the data needed, then display the formula, then display the formula but plug in the values, and in the end the final result. The formula is viscosity is equal to a fraction, where the numerator is 2 times pressure squared times a paranthesis of the difference of density of the selected liquid minus the density of air, close parenthesis. This times gravity which in our case will equal 9.81 meters per second squared and divide all of the above by 9 times the terminal velocity in meters per second. This should give you a viscoisty with units pascal times seconds

## Prompt 19

> For all the graphs can you set your the y value to go from 0 upwards and x value from 0 forward, so that you dont get a graph that is zoomed in

## Prompt 20

> Lets modify the plots. Change the background color of the squares with the plots to white, and the text to black. Also, for the origin, make the first x value on the graph, the time of the first bubble center on the manual log
