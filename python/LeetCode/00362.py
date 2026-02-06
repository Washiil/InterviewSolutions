class HitCounter:
    def __init__(self):
        self.hits = [0] * 300
        self.timestamps = [0] * 300

    def hit(self, timestamp: int) -> None:
        idx = timestamp % 300

        if self.timestamps[idx] == timestamp:
            self.hits[idx] += 1
        else:
            self.timestamps[idx] = timestamp
            self.hits[idx] = 1

    def getHits(self, timestamp: int) -> int:
        total_hits = 0
        for i in range(300):
            if timestamp - self.timestamps[i] < 300:
                total_hits += self.hits[i]
        return total_hits
