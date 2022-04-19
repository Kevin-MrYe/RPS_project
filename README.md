# RPS_project

# Milestone 1
In this milestone, I ues the **Teachable Machine** to create machine learning models for Rock, Paper, Scissors. [Teachable Machine](https://teachablemachine.withgoogle.com/) is a web-based tool which can be used to create machine learning models for images,sounds and poses.

<img src ="https://github.com/Kevin-MrYe/RPS_project/blob/master/images/Teachable.png" width = '700px'>
Just simpily click the Webcam icon and record gestures of Rock, Paper, Scissors. The "Nothing" class represents the lack of option in the image. After training, download the model from the "Tensorflow" tab in Teachable-Machine.

# Milestone 2
In this milestone, I install the dependencies for the game "Rock, Paper and Scissors". To separate dependencies of different projects, I creat isolating environment for this project and then activate it. The commands on terminal are as follow:

**Create new environment with python:**
```python 
conda create --name <env_name> python=3.8
```
**Activate environment**
```python 
conda activate <env_name>
```
**Install pip,opencv,tensorflow and ipykernel**
```python 
conda install pip
pip install opencv-python
pip install tensorflow
pip install ipykernel
```
**Note:** Most of the time there is no difference in installing them with conda or pip. The pip catalog is more complete, while the conda dependency resolver is more robust. Inside a conda virtual environment, you have access to both conda and pip to install libraries.

# Milestone 3 
In this milestone, I write the game logic of Rock-Paper-Scissors. However, in this stage, the game just request input from user's keyboard, rather than the camera. There are two main tasks as follows:
1. Store the user's and computer's choices
  
Define a list ["Rock","Paper","Scissors"]. Call the function **random.choice(list)** to choose a random action for computer. Then, call **input()** to request a input from user. To prevent spelling mistake, just ask an integer and use the index to find the corresponding action in list.
  
2. Figure out who won

Using if-else statements to choose a winner based on the classic rules of Rock-Paper-Scissors. If the action of user is the same as the computer's action, it is a tie and nothing will happen. If the action of user is one of Rock,Paper or Scissors, the computer will have two different actions. print the winner under different situation according to the game rules.


# Milestone 4
In this milestone, I combine the code that used the webcam with the function that ask user for an input. Replace the manual input for the output of the RPS model. In addtion, I add three code part to improve the interaction of the game application. These parts are as follows:
1. Count down 

To give user enough time to prepare action, I create a countdown to get ready for the game. I set a countdown variable name **TIMER**, TIMER will decrease by one every second. When the TIMER = 0, the webcam will capture the image and pass this image to RPS model to predict the user's action. In function **make_prediction()** the computer will choose a random action so that I can judge if the computer win or the user win through the game rules.

2. Repeat until a player gets three victories
To implement this part, I set two global variables named **usr_win_count** and **cp_win_count** to calculate the victory times for user and computer.
If it is a tie, these two variable will not change. If the user win, usr_win_count will increase by 1, otherwise cp_win_count increases by 1. After every round, judge if user or computer already won three times.(usr_win_count = 3 or cp_win_count = 3)

3. Press c to continue

