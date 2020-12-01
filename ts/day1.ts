const data: string = await Deno.readTextFile("../data/day1.txt")
const nums: Array<number> = data.split("\n").map(Number)


// part 1
for (const num of nums) {
    if (nums.includes(2020 - num) == true) {
        console.log(num * (2020 - num)) 
        break; 
    }
}

//part 2


