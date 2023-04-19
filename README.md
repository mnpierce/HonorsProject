CSE 2050-001 Honors Project 2023
Matt Pierce
-----------------------------------------------------------------------------------------------------------

Simulation of MTV's "Are You the One?"

-----------------------------------------------------------------------------------------------------------

Rules
  
  16 contestants get paired into 8 “perfect matches”
  
  Each week:
    - Contestants couple up with who they think their perfect match is
    - Contestants are told the number of correct couples (but not which couples are correct)
    - One couple is sent to the “truth booth” for a definitive result of whether they are a prefect match
      
-----------------------------------------------------------------------------------------------------------
   
Approach

  - Create 16 contestants and randomly select the 8 perfect pairs
  - Simulate the game play
  - Compare different algorithms using a histogram
  
-----------------------------------------------------------------------------------------------------------

About

In this project, I developed four algorithms to compare their efficiency in finding all 8 perfect pairs. For every algorithm besides Algorithm 1, the bulk of the generation of both the original list of perfect pairs and the subsequent list of guesses are fully randomized. I chose to take this approach as I wanted the game to play out differently every time it is simulated to make it more like a game. One way to think of this is that even though I use the same names throughout the programs, from game to game, contestants with the same name can be viewed as different contestants, and therefore will not always have the same match. This approach changes when considering Algorithm 1, as attributes that indicate interests are added to each contestant, and these attributes drive the match-making process.

The algorithm I spent the most time developing is Algorithm 2. This algorithm features the use of gathering bad matches to its fullest functionality. This speeds up the guessing process as there are fewer potential guesses to be made. From Algorithm 2, Algorithm 3 and 4 are more naive. Algorithm 3 lacks the full functionality of gathering bad matches, while Algorithm 4 does not gather bad matches at all (only reduces possible guesses by removing guesses with contestants that already have a confirmed match). As mentioned above, Algorithm 1 is different in regard to its match-making process as it uses additional attributes to match contestants. With this being said, the efficiency as can be observed by running Histogram.py ranks in order (1,2,3,4).

A brief description of each algorithm can also be found at the top of each algorithm file.