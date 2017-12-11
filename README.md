# gifsound
This project is for educational purposes only.  It gives simular functionality to the original www.gifsound.com

Users can create combinations of a Youtube video with a gif, allowing a quick, crude way to play custom sound or music on top of a gif.

* Name of project: Gifsound
* Names of team members
  * Carsen Yates
  * Erick Shaffer
* Class
  * Multimedia Design and Programming
* Date
  * The project started 11/4/2017
  
* How to run program
  1. Create a settings.yml file for your configuration.  You can use settings.yml.dist as an example.
  1. Create a python 3.6 environment inside your working directory: `python3.6 -m venv pyenv`
  1. Activate the environment using `source activate`
  1. On Linux, you might need to install the package `libmysqlclient-dev`
    * For Ubuntu: `sudo apt install libmysqlclient-dev`
  1. Install requirements: `pip install -r requirements.txt` (The environment must be activated)
  1. Run the program using one of the following commands
    * `python gifsound.py` (The environment must be activated)
    * `./gifsound.py` (No need to activate env)
  
* Link to GitHub repository
  * https://github.com/Fatburger3/gifsound
  
* Future work
  * Improve the view page by allowing users to control more of the video and gif parameters such as
    * When video playback should start
    * Whether or not the video should be displayed alongside the gif or hidden(audio only)
    * Looping (for either gif or video)
  * Adding giphy api integration and other apis for retrieving videos or gifs
  * Allowing other sources for sound files or videos besides just youtube
