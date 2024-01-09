from Graph import Graph
from PathFinder import SchedulePathFinder
from PathTime import Dijkstra

g = Graph()
g.add_edge("Classroom South", "Langdale Hall", 197, 1)
g.add_edge("Classroom South", "Arts & Humanities", 0.1 * 5280, 2)
g.add_edge("Classroom South", "Dahlberg Hall", 0.3 * 5280, 6)
g.add_edge("Classroom South", "Sparks Hall", 0.2 * 5280, 5)
g.add_edge("Langdale Hall", "Arts & Humanities", 305, 1)
g.add_edge("Langdale Hall", "Dahlberg Hall", 0.3 * 5280, 5)
g.add_edge("Langdale Hall", "Sparks Hall", 0.2 * 5280, 4)
g.add_edge("Arts & Humanities", "Dahlberg Hall", 0.2 * 5280, 4)
g.add_edge("Arts & Humanities", "Sparks Hall", 0.1 * 5280, 3)
g.add_edge("Dahlberg Hall", "Sparks Hall", 328, 2)

dijkstra = Dijkstra(g)

schedule_finder = SchedulePathFinder(g, dijkstra)

#schedule
Ronnie_schedule = [
    "Langdale Hall", "Classroom South", "Langdale Hall", "Dahlberg Hall",
    "Arts & Humanities"
]
path1, total_time1 = schedule_finder.find_shortest_path_for_schedule(Ronnie_schedule)

HamdiSelim_schedule = [
    "Dahlberg Hall", "Langdale Hall", "Classroom South", "Sparks Hall", "Arts & Humanities" ]
path2, total_time2 = schedule_finder.find_shortest_path_for_schedule(HamdiSelim_schedule)

Jake_schedule = [
    "Sparks Hall", "Arts & Humanities", "Classroom South", "Dahlberg Hall",
    "Langdale Hall"]
path3, total_time3 = schedule_finder.find_shortest_path_for_schedule(Jake_schedule)


def display_path_and_time(schedule_path, total_time, schedule_number):
  print(f"{schedule_number}:")
  for start, end, time in schedule_path:
    print(f"From {start} to {end}: {time} min")
  print(f"Total walking time: {total_time} min")
  print("-" * 30)


display_path_and_time(path1, total_time1, "Ronnie's Schedule")
display_path_and_time(path2, total_time2, "Hamdi Selim's Schedule")
display_path_and_time(path3, total_time3, "Jake's Schedule")
