# Tile Cost

# user enters in a floor width/height/unit cost
# returns total cost

def tile_cost(width, height, unit_cost, unit):
    area = width * height
    cost = area * unit_cost
    message = "The cost of covering {}{}, is ${}".format(str(area), unit, str(cost))
    return message
