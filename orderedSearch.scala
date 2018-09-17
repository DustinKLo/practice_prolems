

def orderedSearch(ls: List[Int], x: Int): Int = {
  val midIndex = ls.length/2
  val midValue = ls(midIndex)

  if(ls.length == 1) {
    if(ls.head == x) return x
    else throw new Exception
  }

  if(x == midValue) {
    return x
  } else if (x < midValue) {
    val sublist = ls.slice(0, midIndex)
    return orderedSearch(sublist, x)
  } else {
    val sublist = ls.slice(midIndex, ls.length)
    return orderedSearch(sublist, x)
  }
}

val ls = (0 to 100000).toList
orderedSearch(ls, 79)
