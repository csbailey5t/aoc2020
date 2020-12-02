const data: string = await Deno.readTextFile("../data/day2.txt")
const lines: Array<string> = data.split("\n")

interface PasswordEntry {
    min: number, 
    max: number, 
    letter: string,
    password: string
}

const lineToPE = function (line: string): PasswordEntry {
    const chunks = line.split(":")
    const minMaxLetter = chunks[0].split(" ")
    const minMax = minMaxLetter[0].split("-")
    const pe = {
        min: Number(minMax[0]), 
        max: Number(minMax[1]),
        letter: minMaxLetter[1],
        password: chunks[1].trim()
    }
    return pe
}

const checkValidPE = function (pe: PasswordEntry): boolean {
    let charCount = 0
    Array.from(pe.password).forEach(char => {
        if (char == pe.letter) charCount += 1
    })
    return (charCount >= pe.min && charCount <= pe.max) 
}

const entries = lines.map(lineToPE)
const validPasswords = entries.filter(pe => checkValidPE(pe) === true)

console.log("part1", validPasswords.length)


// Part 2


interface PasswordEntryT {
    p1: number, 
    p2: number, 
    letter: string,
    password: string
}

const lineToPET = function (line: string): PasswordEntryT {
    const chunks = line.split(":")
    const minMaxLetter = chunks[0].split(" ")
    const minMax = minMaxLetter[0].split("-")
    const pe = {
        p1: Number(minMax[0]) - 1, 
        p2: Number(minMax[1]) - 1,
        letter: minMaxLetter[1],
        password: chunks[1].trim()
    }
    return pe
}


const checkValidPET = function (pe: PasswordEntryT): boolean {
    return ((pe.password[pe.p1] === pe.letter && pe.password[pe.p2] != pe.letter) || (pe.password[pe.p1] != pe.letter && pe.password[pe.p2] === pe.letter)) 
}

const entriesT = lines.map(lineToPET)
const validPasswordsT = entriesT.filter(entry => checkValidPET(entry) === true)

console.log("part2", validPasswordsT.length)