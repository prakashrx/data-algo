#![allow(unused)]
use std::fs;

use day4::{process, process_part2};

fn main() {
    let lines = fs::read_to_string("input.txt").unwrap();
    dbg!(process(&lines));
    dbg!(process_part2(&lines));
}
