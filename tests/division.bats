load harness

@test "division-1" {
  check '15 / 7' '2'
}

@test "division-2" {
  check '8 / 7 + 3 * 6' '19'
}

@test "division-3" {
  check '7 * 5 / 4 + 6 / 2' '11'
}
