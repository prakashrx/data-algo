#![allow(unused)]

use nom::{
    branch::alt,
    bytes::complete::{tag, take_until},
    character::complete::{alpha1, char, digit1, line_ending},
    multi::separated_list1,
    sequence::delimited,
    IResult,
};

#[derive(Debug)]
struct Command {
    count: u32,
    from: u32,
    to: u32,
}

fn item(input: &str) -> IResult<&str, Option<&str>> {
    let (input, value) = alt((tag("   "), delimited(char('['), alpha1, char(']'))))(input)?;
    let result = match value {
        "   " => None,
        value => Some(value),
    };

    Ok((input, result))
}

fn line(input: &str) -> IResult<&str, Vec<Option<&str>>> {
    let (input, value) = separated_list1(tag(" "), item)(input)?;
    Ok((input, value))
}

fn stack(input: &str) -> IResult<&str, Vec<Vec<&str>>> {
    let (input, stack) = separated_list1(line_ending, line)(input)?;
    let (input, _) = take_until("move")(input)?;

    let mut items: Vec<Vec<&str>> = vec![];
    stack.iter().rev().for_each(|x| {
        x.iter().enumerate().for_each(|(ix, i)| {
            if ix >= items.len() {
                items.push(vec![]);
            }
            if let Some(val) = *i {
                items[ix].push(val);
            }
        });
    });

    Ok((input, items))
}

fn command(input: &str) -> IResult<&str, Command> {
    let (input, _) = tag("move ")(input)?;
    let (input, count) = nom::character::complete::u32(input)?;
    let (input, _) = tag(" from ")(input)?;
    let (input, from) = nom::character::complete::u32(input)?;
    let (input, _) = tag(" to ")(input)?;
    let (input, to) = nom::character::complete::u32(input)?;
    Ok((input, Command { count, from, to }))
}

fn commands(input: &str) -> IResult<&str, Vec<Command>> {
    let (input, value) = separated_list1(line_ending, command)(input)?;
    Ok((input, value))
}

fn parse(input: &str) -> IResult<&str, (Vec<Vec<&str>>, Vec<Command>)> {
    let (input, stack) = stack(input).unwrap();
    let (input, commands) = commands(input).unwrap();
    Ok((input, (stack, commands)))
}

pub fn process(input: &str) -> String {
    let (_, (mut stack, commands)) = parse(input).unwrap();

    for command in commands {
        for i in 0..command.count {
            let x = stack
                .get_mut((command.from - 1) as usize)
                .unwrap()
                .pop()
                .unwrap();
            stack.get_mut((command.to - 1) as usize).unwrap().push(x);
        }
    }

    stack
        .iter()
        .map(|x| x.last().unwrap().chars().last().unwrap())
        .collect()
}

pub fn process_part2(input: &str) -> String {
    let (_, (mut stack, commands)) = parse(input).unwrap();

    for Command { from, to, count } in commands {
        let from_stack = &mut stack[(from - 1) as usize];
        let mut x = from_stack
            .drain((from_stack.len() - count as usize)..)
            .collect::<Vec<&str>>();

        let toStack = &mut stack[(to - 1) as usize];
        toStack.append(&mut x);
    }

    stack
        .iter()
        .map(|x| x.last().unwrap().chars().last().unwrap())
        .collect()
}

#[cfg(test)]
mod test {
    use std::fs;

    use super::*;
    #[test]
    fn it_works() {
        let input = fs::read_to_string("test.txt").unwrap();
        assert_eq!(dbg!(process(&input)), "CMZ".to_string());
    }

    #[test]
    fn part2_works() {
        let input = fs::read_to_string("test.txt").unwrap();
        assert_eq!(dbg!(process_part2(&input)), "MCD".to_string());
    }
}
