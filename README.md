# TODO:
- [x] Draw an arch or series of short lines or points 
- [x] Make the line bigger (brush?)
- [ ] Fix lower timestep causing higher arc (or just ignore it and use a really low timestep if performance is not an issue) (I think timestep approaching 0 also approaches the mathematical correct arc)
- [ ] Store power and angle variables and use them to get starting x and y velocity
- [ ] Make it redraw (and update vars) on key press  
    - [ ] May have to deal with window focus issues  
- [ ] Make the arch start at a chosen position (the tank)  
    - [ ] Make it either go to location clicked/dragged or do some color detection with another api (ambitious)  
- [ ] Somehow input the power and angle. Perhaps replicate the circle and power triangle with outlines?
  
- [ ] Do some in-game experimenting to accurately convert power and angle numbers to shot trajectories
- [ ] Eventually also add in wind 

