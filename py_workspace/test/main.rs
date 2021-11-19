/// Adds one to the number given.aaaaaaaaaaa

fn add(a: i32, b: i32) -> i32 {
    return a + b;
}

struct A {
    name: u64
}

fn main() {
    println!("{}",add(2,3));
    println!("Hello, world!");
    println!("Hello, world!");
    println!("Hello, world!");
    println!("Hello, world!");
    println!("Hello, world!");
    println!("Hello, world!");
    // let mut s:&str = "123";
    // s = s + "22342";
    // let s = s.len();
    let x = 5;

    let y = {
        // let x = 3;
        x + 1
    };

    println!("x 的值为 : {}", x);
    println!("y 的值为 : {}", y);

    fn five() -> i32 {
        return 5
    }
    println!("five() 的值为: {}", five());
    // let aa = ['a'];
    let a:A = A{name: 1};
    let b = a;
    println!("{}", b.name);
    // println!("{}", a.name);

    // let reference_to_nothing = dangle();
    // println!(reference_to_nothing)


}
// fn dangle() -> String {
//     let s = String::from("hello");
//
//     // (s, &s)
//     s
// }
