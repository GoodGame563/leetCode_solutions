fn main() {
    println!("{:?}", max_area(vec![1, 8, 100, 2, 100, 4, 8, 3, 7]));
}

pub fn max_area(height: Vec<i32>) -> i32 {
    let mut left = 0;
    let mut right = height.len() - 1;
    let mut max = 0;
    while left < right {
        let width = (right - left) as i32;
        let h = height[left].min(height[right]);
        let water = h * width as i32;
        max = max.max(water);
        if height[left] < height[right] {
            left += 1;
        } else {
            right -= 1
        }
    }
    max
}
