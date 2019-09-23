

def isPrime(n: Int): Boolean = {
	if(n < 2) return false
	if(n == 2) return true
	
	val limit = Math.sqrt(n)
    for(i <- 2 to limit.toInt + 1){
    	if(n % i == 0) return false
    }
	return true
}
isPrime(34)


 def gcd(n: Int, m: Int): Int = {
	var larger: Int = 0
	var smaller: Int = 0
	if(n > m) {
		larger = n
		smaller = m
	} else {
		larger = m
		smaller = n
	}
	// println(s"$larger $smaller")
	val remainder = larger % smaller
	larger = smaller

	if(remainder == 1) return 1
	if(remainder == 0) return larger
	return gcd(larger, remainder)
}
gcd(270, 192)
gcd(14, 9)
gcd(482948209, 3813999)


def totient(n: Int): Int = {
	var coprimes = 0
	for(i <- 1 to n) {
		if(gcd(n, i) == 1) coprimes += 1
	}
	return coprimes
}

def primeFactors(n: Int): List[Int] = {
	if(isPrime(n)) return List(n)

	val head = (2 to n/2).filter(n % _ == 0).find(isPrime(_)).get
	val remainder = n / head
	// println(s"$n ${n/2} $head $remainder")

	return List(head) ::: primeFactors(remainder)
}
primeFactors(31558390).groupBy(identity).mapValues(_.size).toList


def phi(ls: List[(Int, Int)]): Int = {
	var total = 1
	ls.foreach(t => println(t))
	ls.foreach(t => total = total * (t._1 - 1) * Math.pow(t._1, t._2 - 1).toInt )
	// * Math.pow(t._1, t._2 - 1)
	return total
}
phi(primeFactors(31558390).groupBy(identity).mapValues(_.size).toList)





def listPrimesinRange(r: Range): List[Int] = {
	return r.toList.filter(isPrime(_))
}
listPrimesinRange(7 to 31)


def goldbach(n: Int): (Int, Int) = {
	val primes = listPrimesinRange(1 to n)
	for(p <- primes) {
		if(isPrime(n - p)) return (p, n - p)
	}
	return (1, 1)
}
goldbach(28)


def printGoldbachList(r: Range) = {
	for(i <- r) {
		if(i % 2 == 0) {
			val goldVals = goldbach(i)
			println(s"$i = ${goldVals._1} + ${goldVals._2}")
		}
	}
}
printGoldbachList(9 to 1000)



List(6, 5, 1, 3, 8, 4, 7, 9, x]
def quicksort(ls: List[Int]) = {

}

