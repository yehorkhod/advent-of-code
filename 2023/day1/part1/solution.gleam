import gleam/io
import gleam/int
import gleam/list
import gleam/string
import simplifile

const file_path: String = "input.txt"

pub fn main() -> Nil {
  let assert Ok(content) = simplifile.read(file_path)
  content
  |> string.split("\n")
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
