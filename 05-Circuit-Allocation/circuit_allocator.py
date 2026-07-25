import json
import sys

filename = sys.argv[1]
with open(filename) as f:
    data = json.load(f)

links = data['links']
possible_circuits = data['possible-circuits']
simulation = data['simulation']
demands = simulation['demands']

link_cap = {}
for link in links:
    points = link['points']
    key = tuple(sorted(points))
    link_cap[key] = link['capacity']

events = []
for i, d in enumerate(demands):
    start_time = d['start-time']
    end_time = d['end-time']
    end_points = d['end-points']
    demand_value = d['demand']
    events.append((start_time, 'alloc', i, end_points, demand_value))
    events.append((end_time, 'dealloc', i, end_points, demand_value))

def event_key(event):
    time, etype, idx, _, _ = event
    priority = 0 if etype == 'dealloc' else 1
    return (time, priority, idx)

events.sort(key=event_key)

demand_path = [None] * len(demands)
event_number = 1

for event in events:
    time, etype, idx, end_points, demand_value = event
    if etype == 'alloc':
        found_circuit = None
        for circuit in possible_circuits:
            if sorted([circuit[0], circuit[-1]]) == sorted(end_points):
                valid = True
                for j in range(len(circuit) - 1):
                    node1 = circuit[j]
                    node2 = circuit[j+1]
                    link_key = tuple(sorted([node1, node2]))
                    if link_key not in link_cap or link_cap[link_key] < demand_value:
                        valid = False
                        break
                if valid:
                    found_circuit = circuit
                    break

        if found_circuit is not None:
            for j in range(len(found_circuit) - 1):
                node1 = found_circuit[j]
                node2 = found_circuit[j+1]
                link_key = tuple(sorted([node1, node2]))
                link_cap[link_key] -= demand_value
            demand_path[idx] = found_circuit
            print(f"{event_number}. demand allocation: {end_points[0]}<->{end_points[1]} st:{time} - successful")
        else:
            demand_path[idx] = None
            print(f"{event_number}. demand allocation: {end_points[0]}<->{end_points[1]} st:{time} - unsuccessful")
        event_number += 1
    else:
        if demand_path[idx] is not None:
            circuit = demand_path[idx]
            for j in range(len(circuit) - 1):
                node1 = circuit[j]
                node2 = circuit[j+1]
                link_key = tuple(sorted([node1, node2]))
                link_cap[link_key] += demand_value
            print(f"{event_number}. demand deallocation: {end_points[0]}<->{end_points[1]} st:{time}")
            event_number += 1
