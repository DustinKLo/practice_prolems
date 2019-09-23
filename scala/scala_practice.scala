
def lastRecursive(ls: List[Int]): Any = ls match {
	case h :: Nil  => h
    case _ :: tail => lastRecursive(tail)
    case _         => throw new NoSuchElementException
}
println(lastRecursive(List(1,2,3,4)))



def penultimateRecursive(ls: List[Int]): Any = {
	if (ls.length == 2) {
		ls(0)
	} else {
		// println(ls.length)
		penultimateRecursive(ls.tail)
	}
}
println(penultimateRecursive((1 until 100000).toList))

def penultimate(ls: List[Int]) = {
	val listLength = ls.length
	ls(listLength - 2)
}
println(penultimate((1 until 100000).toList))



def listToString(list: List[String]): Any = list match {
    case s :: rest => rest
    case Nil => ""
}
listToString(List())



def nthElement(n: Int, ls: List[Int]): Any = (n, ls) match {
	case (0, h :: _) => h
	case (n, _ :: tail) => nthElement(n - 1, tail)
    case (_, Nil      ) => throw new NoSuchElementException
}
nthElement(2, List(1,2,3,4,5,6,7,8,9))


def listLength(ls: List[Int]): Int = ls match {
	case Nil => 0
	case h :: tail => 1 + listLength(tail)
}
listLength(List(1, 1, 2, 3, 5, 8))


def reverse(ls: List[Int]): Any = ls match {
	case Nil => Nil
	case h :: tail => reverse(tail) ::: List(h)
}
reverse(List(1,2,3,4,5))




List(1,2,3,2,1) match {
	case head :: Nil => Option(head)
    case head :: tail => last(tail)
    case _ => Option.empty
}





def pack(ls: List[Int]): List[Any] = {
	if(ls.isEmpty) return Nil
	val (packed, next) = ls span { _ == ls.head }
	print(packed)
	print(" ")
	print(next)
	println("")
	return packed :: pack(next)
}

val x = List(1,1,1,1,1,3,3,3,3,3,4,4,4,4,5,6,6,6,7) 
pack(x)
// val (packed, next) = x span { _ == x.head }


def encode(ls: List[Any]): List[Any] = {
	if(ls.isEmpty) return Nil
	val (packed, next) = ls span { _ == ls.head }
	val packedLength = packed.length
	val letter = packed.head
	if(packed.length > 1) return List((packedLength, letter)) :: encode(next)
	else return List(letter) ::: encode(next)
}
val x = List('a, 'a, 'a, 'a, 'b, 'c, 'c, 'a, 'a, 'd, 'e, 'e, 'e, 'e)
encode(x)



def duplicate(ls: List[Any]): List[Any] = ls match {
	case Nil => Nil
	case h :: tail => List(h, h) ::: duplicate(tail)
}
duplicate(List('a, 'b, 'c, 'c, 'd))



def duplicateN(n: Int, ls: List[Any]): List[Any] = ls match {
	case Nil => Nil
	case h :: tail => List.fill(n)(h) ::: duplicateN(n, tail)
}
duplicateN(5, List('a, 'b, 'c, 'c, 'd))



def slice(ls: List[Any], n: Int, m: Int): List[Any] = {
	n_m = m - n
	return ls.drop(n)
}
slice(List(1,2,3,4,5,6,7,8,9,10), 2, 5)


def rotateN(n: Int, ls: List[Any]): List[Any] = {
	if(n > 0) {
		val head = ls.slice(0, n)
		val tail = ls.slice(n, ls.length)
		return tail ::: head
	} 
	if(n < 0) {
		val tail = ls.slice(ls.length + n, ls.length)
		val head = ls.slice(0, ls.length + n)
		return tail ::: head
	}
	else return ls
}

rotateN(3, List('a, 'b, 'c, 'd, 'e, 'f, 'g, 'h, 'i, 'j, 'k))
rotateN(-2, List('a, 'b, 'c, 'd, 'e, 'f, 'g, 'h, 'i, 'j, 'k))
rotateN(0, List('a, 'b, 'c, 'd, 'e, 'f, 'g, 'h, 'i, 'j, 'k))


def removeAt(n: Int, ls: List[Any]): List[Any] = {
	if(n == 0) return ls
	
	val head = ls.slice(0, n)
	val tail = ls.slice(n + 1, ls.length)
	return head ::: tail
}
removeAt(1, List('a, 'b, 'c, 'd))
removeAt(0, List('a, 'b, 'c, 'd))



def lotto(n: Int, limit: Int): List[Int] = {
	if(n <= 0) return Nil
	
	val rnd = new scala.util.Random
	val r = rnd.nextInt(limit)
	return List(r) ::: lotto(n-1, limit)
}
lotto(6, 49)



def randomPermute(ls: List[Int]): List[Int] = {
	val arr = ls.toArray
	for(i <- 0 until arr.length) {
		val rnd = new scala.util.Random
		val r = rnd.nextInt(arr.length)
		
		val temp = arr(i)
		arr.update(i, arr(r))
		arr.update(r, temp)
	}
	return arr.toList
}
randomPermute((1 to 20).toList)


def randomSelect(n: Int, ls: List[Any]): List[Any] = {
	if(n == 0) return Nil

	val buff = ls.toBuffer
	
	val rnd = new scala.util.Random
	val r = rnd.nextInt(buff.length)

	val removedValue = buff.remove(r)

	return List(removedValue) ::: randomSelect(n-1, buff.toList)
}
randomSelect(3, List('a, 'b, 'c, 'd, 'f, 'g, 'h))
randomSelect(3, List('h))




1,2,3,4,5,6
1,2,3	1,2,4	1,2,5	1,2,6	1,3,4	1,3,5	1,3,6	1,4,5	1,4,6	1,5,6
2,3,4	2,3,5	2,3,6	2,4,5	2,4,6	2,5,6
3,4,5	3,4,6	3,5,6
4,5,6



def combinations(n: Int, ls: List[Any]): List[Any] = {
	if(n == ls.length) return ls
}


val ls = List(1,2,3,4,5,6)
ls.







