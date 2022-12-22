#![allow(unused)]

use std::collections::HashSet;

#[derive(Debug)]
struct Interval {
    start: i32,
    end: i32,
}

impl From<&str> for Interval {
    fn from(s: &str) -> Self {
        let (x1, x2) = s.split_once('-').unwrap();
        let s: i32 = x1.parse().unwrap();
        let e: i32 = x2.parse().unwrap();
        Interval { start: s, end: e }
    }
}

fn overlaps_fully(x: &Interval, y: &Interval) -> bool {
    (y.start >= x.start && y.end <= x.end) || (x.start >= y.start && x.end <= y.end)
}

fn overlaps(x: &Interval, y: &Interval) -> bool {
    y.start <= x.end && y.end >= x.start || x.start <= y.end && x.end >= y.start
}

pub fn process(input: &str) -> u32 {
    input
        .lines()
        .map(|line| {
            let (a, b) = line.split_once(',').unwrap();
            (a, b)
        })
        .map(|(a, b)| (Interval::from(a), Interval::from(b)))
        .map(|(a, b)| overlaps_fully(&a, &b) as u32)
        .sum()
}

pub fn process_part2(input: &str) -> u32 {
    input
        .lines()
        .map(|line| {
            let (a, b) = line.split_once(',').unwrap();
            (a, b)
        })
        .map(|(a, b)| (Interval::from(a), Interval::from(b)))
        .map(|(a, b)| overlaps(&a, &b) as u32)
        .sum()
}

#[cfg(test)]
mod test {
    use std::fs;

    use super::*;
    #[test]
    fn it_works() {
        let input = fs::read_to_string("test.txt").unwrap();
        assert_eq!(dbg!(process(&input)), 2);
    }

    #[test]
    fn part2_works() {
        let input = fs::read_to_string("test.txt").unwrap();
        assert_eq!(dbg!(process_part2(&input)), 4);
    }
}
