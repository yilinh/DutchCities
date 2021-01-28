from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import ContinuousSpace

import pandas as pd


# ---------------------------------------------------------------
class CityAgent(Agent):
    """A simple city agent"""
    toggle_flag = True

    def __init__(self, unique_id, model, name='Unknown', population=0):
        super().__init__(unique_id, model)
        self.name = name
        self.population = population

    def toggle(self):
        # dummy action
        self.toggle_flag = not self.toggle_flag
        if self.toggle_flag:
            self.population = self.population * 1.2
        else:
            self.population = self.population / 1.2

    def step(self):
        self.toggle()
        print(self.name + ' ' + str(self.population))


# ---------------------------------------------------------------
# input: latitude and Longitude in Decimal Degrees (DD)
def set_lat_lon_bound(lat_min, lat_max, lon_min, lon_max, edge_ratio=0.02):

    # add edges (margins) to the bounding box
    lat_edge = (lat_max - lat_min) * edge_ratio
    lon_edge = (lon_max - lon_min) * edge_ratio
    x_max = lon_max + lon_edge
    y_max = lat_min - lat_edge
    x_min = lon_min - lon_edge
    y_min = lat_max + lat_edge
    return y_min, y_max, x_min, x_max


class DutchCitiesModel(Model):

    def __init__(self, x_max=0, y_max=0, x_min=0, y_min=0):

        self.schedule = RandomActivation(self)
        self.running = True

        df = pd.read_csv('DutchCities.csv')
        self.num_agents = len(df.index)

        y_min, y_max, x_min, x_max = set_lat_lon_bound(
            df['Lat'].min(),
            df['Lat'].max(),
            df['Lon'].min(),
            df['Lon'].max(),
            0.05
        )

        self.space = ContinuousSpace(x_max, y_max, True, x_min, y_min)

        for index, row in df.iterrows():
            city = CityAgent(index, self, row['City'], row['Population'])
            self.schedule.add(city)

            y = row['Lat']
            x = row['Lon']

            self.space.place_agent(city, (x, y))
            city.pos = (x, y)

    def step(self):
        """Advance the model by one step."""
        self.schedule.step()
