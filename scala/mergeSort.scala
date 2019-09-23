

def merge(ls1: List[Int], ls2: List[Int]): List[Int] = {
  println(s"\nlist inputs to split: $ls1 $ls2")
  var orderedList = List[Int]()
  var leftOver = List[Int]()

  var i = 0 // counter for ls1
  var j = 0 // counter for ls2
  while(i < ls1.length && j < ls2.length) {
    // do stuff until one of them (i or j) runs out
    if(ls1(i) < ls2(j)) {
      orderedList = orderedList ::: List(ls1(i))
      i = i + 1
    } else {
      orderedList = orderedList ::: List(ls2(j))
      j = j + 1
    }
  }
  
  if(i < ls1.length) leftOver = ls1.slice(i, ls1.length)
  else leftOver = ls2.slice(j, ls2.length)

  println(s"merged list: ${orderedList ::: leftOver}")
  return orderedList ::: leftOver
}

def mergeSort(ls: List[Int]): List[Int] = {
  if(ls.length == 1) return ls

  val mid = ls.length/2
  var arrayOne = ls.slice(0, mid)
  var arrayTwo = ls.slice(mid, ls.length)
  println(s"\nsplit $ls")

  arrayOne = mergeSort(arrayOne)
  arrayTwo = mergeSort(arrayTwo)

  val orderedSublist = merge(arrayOne, arrayTwo)
  return orderedSublist
}
mergeSort(List(2,8,5,3,9,4,70,8))

