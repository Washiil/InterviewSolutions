from math import inf

class Solution:
    def earliestFinishTime(
        self,
        landStartTime: list[int],
        landDuration: list[int],
        waterStartTime: list[int],
        waterDuration: list[int]
    ) -> int:

        def calculate_earliest_finish(
            first_starts: list[int],
            first_durations: list[int],
            second_starts: list[int],
            second_durations: list[int]
        ) -> int:
            earliest_first_phase_finish = inf
            for i in range(len(first_starts)):
                finish_time = first_starts[i] + first_durations[i]
                earliest_first_phase_finish = min(earliest_first_phase_finish, finish_time)

            earliest_total_finish = inf
            for i in range(len(second_starts)):
                actual_start_time = max(earliest_first_phase_finish, second_starts[i])
                finish_time = actual_start_time + second_durations[i]
                earliest_total_finish = min(earliest_total_finish, finish_time)

            return earliest_total_finish

        land_then_water_finish = calculate_earliest_finish(
            landStartTime, landDuration,
            waterStartTime, waterDuration
        )

        water_then_land_finish = calculate_earliest_finish(
            waterStartTime, waterDuration,
            landStartTime, landDuration
        )

        return min(land_then_water_finish, water_then_land_finish)
