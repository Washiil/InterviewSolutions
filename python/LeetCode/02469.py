def convertTemperature(self, celsius: float) -> list[float]:
    return [celsius + 273.15, (celsius * 9/5) + 32]
