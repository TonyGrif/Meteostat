from datetime import datetime
from meteostat import Point, Daily

start = datetime(2020, 1, 1)
end = datetime(2020,12,1)

point = Point(36.8593, -75.9845)

data = Daily(point, start, end)
data = data.fetch()
print(type(data))
