stock = {
    "lapiz": 10,
    "cuaderno": 5,
    "goma": 3
}

stock["cuaderno"] -= 2
stock["regla"] = stock.get("regla", 0) + 1
stock["goma"] = 0

print(stock)
