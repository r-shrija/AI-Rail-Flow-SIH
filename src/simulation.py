import simpy
import pandas as pd

# This represents a train moving through a block
def train_process(env, name, travel_time, resource):
    print(f"{name} arriving at block at {env.now}")
    
    # Request the track (The Resource)
    with resource.request() as request:
        yield request # Wait until the track is free
        
        print(f"{name} entering block at {env.now}")
        yield env.timeout(travel_time) # The time it takes to cross
        print(f"{name} leaving block at {env.now}")

# Setup the environment
env = simpy.Environment()
track_block = simpy.Resource(env, capacity=1)

# Add two trains to the world
env.process(train_process(env, 'Freight Train', 20, track_block))
env.process(train_process(env, 'Rajdhani Express', 10, track_block))

env.run()
