#!/usr/bin/python3
from relationship_state import State
from relationship_city import City

st = State()
st.name = "california"
c1 = City()
c1.name="tokyo"
c2 = City()
c2.name="dubai"
st.cities=[c1, c2]
print(st.__dict__)

