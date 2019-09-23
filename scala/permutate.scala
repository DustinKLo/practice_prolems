 

def permutate(word: String): List[String] = {
	var permutations = List[String]()
	val wordList = word.toString.split("").toList
	val wordLength = wordList.length

    def permutateRecurse(x: String, leftover: List[String]): List[String] = {
        if(leftover.length == 0) return Nil

        for(i <- 0 to leftover.length - 1) {
            var leftoverTmp = leftover
            val (left, right) = leftoverTmp.splitAt(i)
            leftoverTmp = left ::: right.drop(1)
            val permValue = x + leftover(i)
            
            if(permValue.length == wordLength) permutations = permutations ::: List(permValue)
            permutateRecurse(permValue, leftoverTmp)
        }
        return Nil
    }
    permutateRecurse("",  word.toString.split("").toList)
    return permutations
}

val test = permutate("dustin")
println(test.length)
