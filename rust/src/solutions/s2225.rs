use std::collections::{HashMap, HashSet};

pub struct Solution;

impl Solution {
    pub fn find_winners(matches: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut players: HashMap<i32, i32> = HashMap::new();

        for m in matches {
            let winner = m[0];
            let loser = m[1];

            if !players.contains_key(&winner) {
                players.insert(winner, 0);
            }
            if let Some(player) = players.get_mut(&loser) {
                *player += 1;
            } else {
                players.insert(loser, 1);
            }
        }

        let mut exactly_one = players
            .iter()
            .filter(|&(player, losses)| *losses == 1)
            .map(|(&key, _)| key)
            .collect::<Vec<i32>>();

        let mut exactly_zero = players
            .iter()
            .filter(|&(player, losses)| *losses == 0)
            .map(|(&key, _)| key)
            .collect::<Vec<i32>>();

        exactly_one.sort();
        exactly_zero.sort();

        return vec![exactly_zero, exactly_one];
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test1() {
        let input = vec![vec![2, 3], vec![1, 3], vec![5, 4], vec![6, 4]];
        assert_eq!(
            Solution::find_winners(input),
            vec![vec![1, 2, 5, 6], vec![]]
        );
    }

    fn test2() {
        let input = vec![
            vec![1, 3],
            vec![2, 3],
            vec![3, 6],
            vec![5, 6],
            vec![5, 7],
            vec![4, 5],
            vec![4, 8],
            vec![4, 9],
            vec![10, 4],
            vec![10, 9],
        ];
        assert_eq!(
            Solution::find_winners(input),
            vec![vec![1, 2, 10], vec![4, 5, 7, 8]]
        )
    }
}
