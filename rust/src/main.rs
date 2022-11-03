#![allow(dead_code)] 
#![allow(unused_variables)] 

fn variables(){
    let name = "Test";
    let name2 = &name[0..2];

    let id = 32;
    let id2 = &id;

    let mut age = 32;
    let age2 = &mut age;
    
    let my_new_age = *age2;
    *age2 = 33;
    println!("{}:{}", name, name2);
    println!("{}: {}", id, id2);
    println!("{}", age2);
    println!("{}", age);
    println!("{}", my_new_age);


}

fn swap(a:&mut i32, b:&mut i32) {
    (*a, *b) = (*b, *a);
}

fn test_str(my_str:String)-> String {
    // Write code here
    let mut ret=  String::new();
    for word in my_str.split_whitespace() {
        if let 'c' = word.chars().nth(0).unwrap() {
            ret += &format!("{} ", word);
        }
   }
   ret.pop();
   ret
}

fn test_vec(my_vec: &mut Vec<u32>)-> &mut Vec<u32>{
    // Write code here!
    my_vec.pop();
    my_vec.remove(my_vec.len()/2 );
    my_vec.push(my_vec.iter().sum());
    my_vec
 }

 #[derive(Debug)]
struct MyData {
    name: String,
    age: i32
}

#[derive(Debug)]
struct Test(String, i32);

impl MyData {
    fn new() ->  MyData {
        MyData { name : "Prakash".to_string(), age : 38 }
    }
    fn test(&self) -> String {
        self.name.clone()
    }
}

trait Name {
    fn get_name(&self) -> String;
}

impl  Name for MyData {
    fn get_name(&self) -> String {
        self.name.clone()
    }
}

impl Name for Test {
    fn get_name(&self) -> String {
        self.0.clone()
    }
}


fn main() {

    // let str= "This is a comprehensive course in Rust programming language on the Educative. Read it with full concentration to grasp the content of the course".to_string();
    // let ret = test_str(str);
    // println!("{}", ret);

    // let mut vec = vec![1,5,7,9];
    // println!("{:?}", test_vec(&mut vec));

    //let my_data = MyData { name : "Prakash".to_string(), age : 38 };
    //let my_data2 = Test("Prakash".to_string(), 32);
    //println!("{:?}", my_data2);

    // let my_data = MyData::new();
    // let my_test = Test("Tester".to_string(), 32);
    // println!("{:?}", my_data.get_name());
    // println!("{:?}", my_test.get_name());

    let my_data = MyData::new();
    let MyData{ name:ref myname, ..} = my_data;
    println!("{:}", myname);
}
