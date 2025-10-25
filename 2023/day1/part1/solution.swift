import Foundation

let digits: String = "0123456789"
let fileURL: URL = FileManager.default.homeDirectoryForCurrentUser
    .appendingPathComponent("Desktop/advent-of-code/2023/day1/part1/input.txt")
let text: String = try! String(contentsOf: fileURL, encoding: .utf8)

var result: Int = 0
for line in text.split(separator: "\n") {
    var digs: [Character] = line.filter { digits.contains($0) }

    switch digs.count {
    case 1: result += Int(String(repeating: digs[0], count: 2))!
    default: result += Int(String([digs[0], digs[digs.count - 1]]))!
    }
}

print(result)
