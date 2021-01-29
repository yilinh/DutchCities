from mesa.visualization.ModularVisualization import ModularServer

from SimpleContinuousModule import SimpleCanvas
from model import DutchCitiesModel


def agent_portrayal(agent):
    portrayal = {
                 # "Shape": "rect",
                 "Shape": "circle",
                 "Filled": "true",
                 "Color": "dodgerblue",
                 "r": max(agent.population / 100000 * 2, 2)
                 # "w": max(agent.population / 100000 * 4, 4),
                 # "h": max(agent.population / 100000 * 4, 4)
                 }

    if agent.name == 'Amsterdam':
        portrayal["Color"] = "green"
    elif agent.name == 'sgravenhage':
        portrayal["Color"] = "HotPink"
    elif agent.name == 'Rotterdam':
        portrayal["Color"] = "DarkSlateGray"
    elif agent.name == 'Utrecht':
        portrayal["Color"] = "DarkGoldenRod"
    elif agent.population > 200000:
        portrayal["Color"] = "red"

    if agent.name in ['Amsterdam', 'sgravenhage', 'Rotterdam', 'Utrecht']:
        portrayal["Text"] = agent.name
        portrayal["Text_color"] = "DarkGray"

    return portrayal


canvas_width = 500
canvas_height = 500

space = SimpleCanvas(agent_portrayal, canvas_width, canvas_height)

server = ModularServer(DutchCitiesModel,
                       [space],
                       "Dutch Cities Model",
                       {})

server.port = 8521  # The default
server.launch()
