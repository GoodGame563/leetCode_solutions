fn main() {
    println!("{:?}", num_water_bottles(15, 4));
}

pub fn num_water_bottles(num_bottles: i32, num_exchange: i32) -> i32 {
    count_water_bottles(num_bottles, 0, num_exchange)
}

pub fn count_water_bottles(full_bottles: i32, empty_bottles: i32, num_exchange: i32) -> i32 {
    if full_bottles + empty_bottles < num_exchange {
        return full_bottles;
    }
    let mut all_bottles = full_bottles;
    all_bottles += count_water_bottles(
        (full_bottles + empty_bottles) / num_exchange,
        (full_bottles + empty_bottles) % num_exchange,
        num_exchange,
    );
    all_bottles
}
