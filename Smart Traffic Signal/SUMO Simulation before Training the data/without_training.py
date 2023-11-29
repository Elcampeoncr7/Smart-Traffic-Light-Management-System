import traci
import traci.constants as tc
from sumolib import checkBinary 

def compute_total_waiting_time_with_traci(sumo_cfg_file, steps=501):
    # Start SUMO with TraCI
    sumoCmd = ["sumo-gui", "-c", sumo_cfg_file]
    traci.start(sumoCmd)

    
    step = 0
    total_time = 0
        
    traffic_lights_time = dict()
    prev_wait_time = dict()
    prev_vehicles_per_lane = dict()
    prev_action = dict()
    all_lanes = list()
    
    total_waiting_time = 0
    all_junctions = traci.trafficlight.getIDList()
    junction_numbers = list(range(len(all_junctions)))
    
    for junction_number, junction in enumerate(all_junctions):
        prev_wait_time[junction] = 0
        prev_action[junction_number] = 0
        traffic_lights_time[junction] = 0
        prev_vehicles_per_lane[junction_number] = [0] * 4
        # prev_vehicles_per_lane[junction_number] = [0] * (len(all_junctions) * 4) 
        all_lanes.extend(list(traci.trafficlight.getControlledLanes(junction)))
    
    def get_waiting_time(lanes):
        waiting_time = 0
        for lane in lanes:
            waiting_time += traci.lane.getWaitingTime(lane)
        return waiting_time * 7.07
    
    # Main simulation loop for 500 steps
    for step in range(steps):
        traci.simulationStep()
        # For each vehicle, get the waiting time and add it to the total
        # for vehicle_id in traci.vehicle.getIDList():
        for junction_number, junction in enumerate(all_junctions):
            controled_lanes = traci.trafficlight.getControlledLanes(junction)
            waiting_time = get_waiting_time(controled_lanes)
            # waiting_time = traci.vehicle.getWaitingTime(vehicle_id)
            total_waiting_time += waiting_time

    traci.close()
    return total_waiting_time

# Use the function
sumo_cfg_file = r"C:\Users\kpanc\Desktop\Project 298\Smart Traffic Signal\Sjdt.sumocfg"
total_time = compute_total_waiting_time_with_traci(sumo_cfg_file)
print(f"Total waiting time for the 500 simulation steps: {total_time} seconds")