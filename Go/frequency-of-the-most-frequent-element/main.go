package main

import (
	"fmt"
	"sort"
)

func main() {
	fmt.Println("Hello, World!")
	maxFrequency([]int{1, 4, 8, 13}, 5)
}

func max(a, b int) int {
	if a >= b {
		return a
	}

	return b
}

func maxFrequency(nums []int, k int) int {
	maxFreq := 0
	currentSum := 0
	sort.Ints(nums)
	left := 0
	for right := range nums {
		currentSum += nums[right]
		// fmt.Println(nums[right]*(right-left+1) - currentSum)s
		for currentSum+k < nums[right]*(right-left+1) {
			// fmt.Println(nums[right]*(right-left+1) - currentSum)
			currentSum -= nums[left]
			fmt.Println(currentSum)
			left++
		}
		maxFreq = max(maxFreq, right-left+1)
	}

	return maxFreq
}
