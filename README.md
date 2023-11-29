# Dynamic-Traffic-light-management-system
This repository contains files for the traffic light management system using Reinforcement Learning.

## Basic Concept 

![sample](documentation/samplecity1.PNG)

- Imagine a city grid with four traffic light nodes labeled as n1, n2, n3, and n4. 
- In our model, decisions are made for each node, determining which side should have the green signal.
- It is essential to establish a minimum time limit (e.g., 30 seconds) that our model cannot exceed when selecting the green light duration. 
- The primary objective is to minimize the waiting time for vehicles at traffic signals, where waiting time is calculated by multiplying the total number of cars
  at a signal by the number of seconds.
- Each traffic signal has four waiting time counters for each side of the road, guiding the model's decision on which side to select for the green signal.

## Training Approach:

![train](documentation/train_loop.png)

- The model undergoes training based on numerous events, defined as predetermined motions where vehicles pass through nodes in a fixed (pseudo-random) manner.   
- Keeping events fixed ensures consistent results, as using random events each time would yield unpredictable outcomes. 
- Multiple fixed events are employed for training to enable the model to handle diverse situations. 
- The model's sole input is the count of vehicles on the four sides of each traffic node, and its output determines the selected side for each node. 
- The number of nodes varies depending on the grid's size.

## SUMO for Simulation:
- We use SUMO (Simulator for Urban MObility) software to simulate the traffic lights in real time.
- SUMO is employed for simulation purposes, providing a realistic environment to test and optimize traffic signal strategies in our model.

Here are examples of some of the maps used to train the model.

### San Jose Downtown Map 
![map](/Smart%20Traffic%20Signal/maps\San_Jose_Downtown_Map.jpg)

###  Epoch Vs Time for San Jose Downtown Map 

![evst](/Smart%20Traffic%20Signal/Visualization\time_vs_epochs.png)

## Simulation without Training.

https://github.com/Elcampeoncr7/Smart-Traffic-Light-Management-System/assets/71449727/267482d7-63bf-4c41-9221-7f713b5a64a5

## Simulation of Trained Model.

https://github.com/Elcampeoncr7/Smart-Traffic-Light-Management-System/assets/71449727/90c981f4-052b-4edb-9feb-f8684f6a1503

## How to train new Networks.

Repository Download: Begin by downloading or cloning the repository.
Ensure you have the SUMO GUI downloaded for running simulations. Obtain the SUMO GUI [here](https://sumo.dlr.de/docs/Downloads.php).

### Step 1 : Network and Route Creation: 

Utilize the SUMO netedit tool to craft a network (e.g., 'network.net.xml') and save it in the maps folder.
Navigate to the maps folder and execute the following command:
 
`python randomTrips.py -n network.net.xml -r routes.rou.xml -e 500`

This command generates a 'routes.rou.xml' file for 500 simulation steps based on the network "network.net.xml."

### Step 2 : Configuration File Setup:

Specify the network and route files in the Configuration file by changing the net-file and route-files under input.

`<input>`        
  `<net-file value='maps/city1.net.xml'/>`
  `<route-files value='maps/city1.rou.xml'/>`
`</input>`

### Step 3 : Model Training:

Utilize the 'train.py' file to train a model for this network:

`python train.py --train -e 50 -m model_name -s 500`

This code trains the model for 50 epochs, with -e setting the epochs, -m specifying the model_name saved in the model folder, and -s indicating the simulation to run for 500 steps. If --train is not specified, it loads 'model_name' from the model's folder. After simulation completion, time_vs_epoch graphs are displayed and saved in the Visualization folder as 'time_vs_epoch.png.'

### Step 4 : Running Trained Model:<br/>

To run a pre-trained model on the GUI, use 'train.py' with the command:

`python train.py -m model_name -s 500`

This opens the GUI for observing your model's performance. For accuracy, set the -s value the same for testing and training.
After the completion fo the model you will get the total waiting time for 500 Simulation Steps.

![opt1](/Smart%20Traffic%20Signal/Output_data_files/trained_model.jpg)

### Step 5 : Running the Simulation without training model to check the difference :

To run a pre-trained model on the GUI, use 'without_training.py' with the command:

`python without_training.py`

This will open the GUI for the original model and in the command line you will get the total waiting time for 500 Simulation Steps.

![Simulation Output](/Smart%20Traffic%20Signal/Output_data_files/without_training.jpg)

### Step 6 : Results

Traffic Congestion without Training

![Traffic Congestion before training](https://github.com/Elcampeoncr7/Smart-Traffic-Light-Management-System/assets/71449727/c2666b0c-4cd9-461d-98d8-755380b33ad4)

Traffic Cangestion after Training

![Traffic Congestion after training](https://github.com/Elcampeoncr7/Smart-Traffic-Light-Management-System/assets/71449727/4ce08c76-a86e-4b99-96fe-349096ac783f)

