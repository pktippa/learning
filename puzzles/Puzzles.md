# Puzzles

Q. 25 Tracks 5 horses puzzle -  There are 25 horses among which you need to find out the fastest 3 horses. You can conduct race among at most 5 to find out their relative speed. At no point you can find out the actual speed of the horse in a race. Find out how many races are required to get the top 3 horses.

A: Number the horses from h1 to h25, divide them into 5 groups and conduct the 5 races, after which take the top 3 from each group. Lets say first 3 from each group came first in race i.e h1, h2, h3 from 1st group, h6,h7,h8 from 2nd and so on.

Now comes elimination:
Eliminate all the horses from 5 groups that are in 4th and 5th position i.e. h4, h5 in 1st group, h9, h10 from 2nd group and so on.

Now we left with 15 horses.

Now take all the 5 horses that came first on each group i.e h1, h6, h11, h16, h21, Now conduct the 6th race, lets assume h1, h6, h11 came in 1st, 2nd, 3rd positions, 

Now comes elimination:

So we can eliminate h16, h21 which are in 4th and 5th position.

Now we left with 13 horses.

Since h16, h21 horses came after 3rd position, horses after them in their respective groups will be slower than them, so we can eliminate h16, h21 (3 horses) groups horses i.e. h17, h18, h22, h23. 

Now we left with 9 horses.

Since h11 came third horses after that in its group h12, h13 would be slower than them so we can eliminate them.

Now we left with 7 horses.

Since h6 came in 2nd position, see the horses in h6 group i.e. h7, h8. If we would have conducted race with these two also h8 would come at 4th position or more in the race, since we are interested in first 3 positions, we take only h7. h8 can be eliminated.

Now we left with 6 horses.

These horses are 

h1, h2, h3
h6, h7
h11

Since h1 already came first in race, we dont have to consider it for next race we have to fill the second and third positions. So we take h2, h3, h6, h7, h11 - these 5 horses and conduct the 7th race and get the first two positions. These two position horses stand as 2nd and 3rd positions (h1 being at first position.)

So we need minimum of 7 races to find the first 3 fastest horses.



Q: There is a room with a door (closed) and three light bulbs. Outside the room there are three switches, connected to the bulbs. You may manipulate the switches as you wish, but once you open the door you can’t change them. Identify each switch with its bulb.

A: We have to understand that light enery is dissipated in form of illuminated and heat energy. Here we have to leverage the heat energy also.

Let the bulbs be X, Y and Z

Turn on switch X for 5 to 10 minutes. Turn it off and turn on switch Y. Open the door and touch the light bulb.

* if the light is on, it is Y
* if the light is off and hot, it is X
* if the light is off and cold, it is Z

Similar Question of 3 switches with one bulb, finding out the correct switch for single bulb.