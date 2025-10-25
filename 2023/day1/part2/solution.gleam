import gleam/int
import gleam/io
import gleam/list
import gleam/string
import simplifile

const file_path: String = "input.txt"
const subs: List(#(String, String)) = [
  #("one", "one1one"),
  #("two", "two2two"),
  #("three", "three3three"),
  #("four", "four4four"),
  #("five", "five5five"),
  #("six", "six6six"),
  #("seven", "seven7seven"),
  #("eight", "eight8eight"),
  #("nine", "nine9nine"),
  #("zero", "zero0zero"),
]

pub fn main() -> Nil {
  let assert Ok(contents) = simplifile.read(file_path)
  contents
  |> string.split("\n")
  |> list.map(substitute(_, subs))
  |> list.map(string.to_graphemes)
  |> list.map(list.filter(_, fn(c) { string.contains("0123456789", c) }))
  |> list.map(fn(digits) {
    case digits {
      [] -> ""
      _ -> {
        let assert Ok(a) = list.first(digits)
        let assert Ok(b) = list.last(digits)
        a <> b
      }
    }
  })
  |> list.filter_map(int.parse)
  |> int.sum
  |> int.to_string
  |> io.print
}

fn substitute(line: String, subs: List(#(String, String))) -> String {
  case subs {
    [#(old, new), ..rest] -> line |> string.replace(old, new) |> substitute(rest)
    [] -> line
  }
}
