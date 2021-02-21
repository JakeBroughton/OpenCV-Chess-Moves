# LegGambit
Project Objective:
- Recognize chess moves on physical board using camera, which are made on a Lichess.com analysis board.

Aims:
- Recognize chess board with camera
- Recognize moves
- Send moves to python-chess
- Connect to API
- Send moves to API


TODO:
- Main progress:
	* Implement contour finding to "before move" and "after move" difference images
	* Translate "before and after" contours into piece movement
	* Put moves into chess engine/list


- Small fixes/improvements:
	* Fix warning text in console
	* Make bigWindow function more flexible to number of input windows
	* Remove hard coded 480 x 480 values from bigWindow, use global windowW and windowH instead
	* Refactor main loop for clarity
	* Group functions into better organised modules, not just all in myfuncs.py
	* Add labels to windows
	* Add instructions to pop up windows
	* Implement Kivy?