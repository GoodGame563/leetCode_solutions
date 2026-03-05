fn main() {
    let nums = vec![1, 2, 3, 4, 5];
    println!("{:?}", triangular_sum(nums));
}

pub fn triangular_sum(nums: Vec<i32>) -> i32 {
    if nums.len() <= 1 {
        return nums[0];
    }
    let mut new_nums = vec![];

    for i in 0..nums.len() - 1 {
        new_nums.push((nums[i] + nums[i + 1]) % 10)
    }

    triangular_sum(new_nums)
}
