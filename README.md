# Campus Path Finder

## Overview

Campus Path Finder is a Python application designed to assist users in navigating a university campus efficiently. Utilizing Dijkstra's algorithm, the application calculates the shortest path between various campus buildings based on distance and estimated walking time. This solution is ideal for students, staff, and visitors seeking the quickest route to their destinations.

## Features

- Graph representation of campus buildings and pathways.
- Calculation of the shortest path between buildings.
- Scheduling feature to plan the most efficient route for multiple destinations.
- Display of total walking time for planned routes.

## Installation

To run the Campus Path Finder, you need Python installed on your machine. Clone the repository and navigate to the project directory to begin.

```bash
git clone [repository-url]
cd [repository-directory]
```

## Usage

1. Import the Graph, Dijkstra, and SchedulePathFinder classes.
2. Create a graph instance and add edges representing pathways between buildings.
3. Utilize the SchedulePathFinder class to find the shortest path for a given schedule.

Example:

```python
from Graph import Graph
from PathFinder import SchedulePathFinder
from PathTime import Dijkstra

# Create graph instance and add pathways
g = Graph()
g.add_edge("Building A", "Building B", distance, time)
# ... add other buildings and paths ...

# Create Dijkstra instance
dijkstra = Dijkstra(g)

# Create SchedulePathFinder instance
schedule_finder = SchedulePathFinder(g, dijkstra)

# Define a schedule
schedule = ["Building A", "Building B", ...]

# Find shortest path for the schedule
path, total_time = schedule_finder.find_shortest_path_for_schedule(schedule)

# Display the path and total time
```

## Contributors
- **Hamdi Selim Akin** - Programming, Algorithm Development, Report Writing
- **Ronnie Triplett** - Graph Calculation, Research, Report Writing

## License
This project is licensed under the MIT License - see the LICENSE file for details.