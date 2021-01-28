# Dutch Cities

An example to visualize Mesa models on a continuous canvas 

## How to Run

* Launch the visualization
```
    $ python model_viz.py
```


## Files

* [model.py](model.py): The model file contains the model and the CityAgent class. 
* [SimpleContinuousModule.py](SimpleContinuousModule.py): Defines ``SimpleCanvas``, the Python side of a custom visualization module for drawing objects with continuous positions. This is an adaptation of the Flocker example provided by the Mesa project.
* [simple_continuous_canvas.js](simple_continuous_canvas.js): JavaScript side of the ``SimpleCanvas`` visualization module; takes the output genereated by the Python ``SimpleCanvas`` element and draws it in the browser window via HTML5 canvas. This is an adaptation of the Flocker example provided by the Mesa project.
* [model_viz.py](model_viz.py): Sets up the visualization; uses the SimpleCanvas element defined above. Run the server.
* [DutchCities.cvs](DutchCities.cvs): The data of Dutch cities (pupolation, lat, lon) used to generate city agents. 
* [DutchCities.ipynb](DutchCities.ipynb): Tests the model in a Jupyter notebook.


