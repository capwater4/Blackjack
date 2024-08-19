# Blackjack
V0: Fully playable CLI game featuring betting, splitting, aces, etc. \
V1: Implement basic strategy table and action tracker\
V2: Implement multiple players, ability to simulate runs\
V3: Implement counting checker + statistics\
\
To be hosted on website with offline play capability, bet caching, etc.

index=your_index "event run" OR "event end"
| eval EventType=if(message="event run", "Start", "End")
| transaction startswith="event run" endswith="event end" maxspan=1d
| eval duration_minutes = duration / 60
| timechart span=1d sum(duration_minutes) as Total_Duration
