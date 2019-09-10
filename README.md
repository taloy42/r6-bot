# r6-bot
a discord bot for me and my friends for when we play a game

this bot has several functions, every function must start with the prefix stated in the json file

the list of the games available for everyone and for each player is stated in the json file too

you can write the aliases with uppercase or lowercase, it wont matter. the important thing is to spell write and put the prefix before the alias

the functions are:


# heads_or_talis
  ```it sends a picture of heads or tails, to decide tough decisions```
  
  **aliases**
  
  -ht
  
  -hot
  
  -headsortails
  
  -עפ

  -עץ_או_פלי


# team_select
```it gets a list of names(in the message you just write the names with spaces) and sorts them into two groups```


  **aliases**
  
  -ts
  
  -teamselect
  
  -בק
  
  -בחירת-קבוצה
  
 # pick_game
 
```it picks a game based on the parameters given, and based on the json file```

**aliases**

-pg

-pickgame

-pickgame**s**

-אחשלי

**syntax**

alias [(Cc(ategoy)) name_of_category]  [players_that_play separated_by_spaces]

ex.
    
    .pg c shooters eliran avihay levi
    .PickGame ben evyatar
    .אחשלי c multiplayer
    
    
# game_info

```it return a list of all games available for a certain player or a certain category```

**aliases**

-gi

-gameinfo

-game**s**info

**syntax**

alias [(Cc(ategoy)) name_of_category] or [name of player]

ex.
  .gi c zombies
  .gaMesInfO avihay
