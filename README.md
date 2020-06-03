# svgtogcode
A simple script to convert svg files to gcode, only with 3D-Printers in mind that have a pen mount and can act as plotters.

Not very polished right now, but functional.
## Prerequisites
-Python 3 with numpy and svgpathtools

## Usage
- Drop a svg-file into the same directory as the script
- In the script, change Z_OFFSET to the height at which the pen can draw on the build plate
- In the script, change START_X and START_Y to where you want to the lower left corner to be
- (All of these values should be read from your 3D-Printer or a control software)
- In the script, set WIDTH to the width you want the final picture to be in mm. The picture will be scaled and aspect ratio will be conserved.
**There is no check to see if the picture will be too high after scaling!**
- Run the script.
- It will output out.gcode, which is ready to run on your Printer
