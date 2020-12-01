const data: string = await Deno.readTextFile("../data/day1.txt")
const nums: Array<number> = data.split("\n").map(Number)


// part 1
for (const num of nums) {
    if (nums.includes(2020 - num) == true) {
        console.log("part1", num * (2020 - num)) 
        break 
    }
}

//part 2
for (const num1 of nums) {
    for (const num2 of nums) {
        if (nums.includes(2020 - num1 - num2) == true) {
            console.log("part2", num1 * num2 * (2020 - num1 - num2))
            break
        }
    }
}

