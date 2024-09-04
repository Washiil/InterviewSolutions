use std::{collections::HashSet};

struct Solution;

enum Direction {
    North,
    South,
    East,
    West
}

impl Direction {
    pub fn turn_left(&mut self) {
        *self = match *self {
            Direction::North => Direction::West,
            Direction::West => Direction::South,
            Direction::South => Direction::East,
            Direction::East => Direction::North,
        };
    }

    pub fn turn_right(&mut self) {
        *self = match *self {
            Direction::North => Direction::East,
            Direction::South => Direction::West,
            Direction::East => Direction::South,
            Direction::West => Direction::North,
        }
    }
}

fn calculate_euclidean_distance(x1: i32, y1: i32, x2: i32, y2: i32) -> f32 {
    let differences = ((x2 - x1).pow(2) + (y2 - y1).pow(2)) as f32;
    differences.sqrt()
}

impl Solution {
    pub fn robot_sim(commands: Vec<i32>, obstacles: Vec<Vec<i32>>) -> i32 {
        let mut obstacle_locations: HashSet<(i32, i32)> = HashSet::new();
        for x in obstacles {
            obstacle_locations.insert((x[0], x[1]));
        }

        let mut max_distance: f32 = 0.0;
        let mut max_point = (0, 0);

        let mut direction: Direction = Direction::North;
        let mut x = 0;
        let mut y = 0;

        for command in commands {
            match command {
                -1 => direction.turn_right(),
                -2 => direction.turn_left(),
                _ => {
                    match direction {
                        Direction::North => {
                            for _ in 0..command {
                                y += 1;
                                if obstacle_locations.contains(&(x, y)) {
                                    y -= 1;
                                    break;
                                }
                            }
                        },
                        Direction::South => {
                            for _ in 0..command {
                                y -= 1;
                                if obstacle_locations.contains(&(x, y)) {
                                    y += 1;
                                    break;
                                }
                            }
                        },
                        Direction::East => {
                            for _ in 0..command {
                                x += 1;
                                if obstacle_locations.contains(&(x, y)) {
                                    x -= 1;
                                    break;
                                }
                            }
                        },
                        Direction::West => {
                            for _ in 0..command {
                                x -= 1;
                                if obstacle_locations.contains(&(x, y)) {
                                    x += 1;
                                    break;
                                }
                            }
                        },
                    }
                    println!("x: {}, y: {}", x, y);
                    let temp_distance = calculate_euclidean_distance(x, y, 0, 0);
                    if max_distance < temp_distance {
                        max_distance = temp_distance;
                        max_point = (x, y)
                    }
                }
            }
        }

        max_point.0.pow(2) + max_point.1.pow(2)
    }
}



mod tests {
    use super::*;

    #[test]
    fn test_874() {
        let commands = vec![4,-1,4,-2,4];
        let obstacles = vec![vec![2,4]];

        let result = Solution::robot_sim(commands, obstacles);
        assert_eq!(result, 65);
    }
}
