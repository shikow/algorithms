
/* Returns either the index of the location in the array,
  or -1 if the array did not contain the targetValue */
  var doSearch = function(array, targetValue) {
	var min = 0;
	var max = array.length - 1;
    var find = false;
    var position = -1;
    var totalIterations = 0;
    while(min <= max){

        var mid = Math.floor((min + max) /2);
        
        if(targetValue === array[mid]){
            console.log('Number of iterations: ' + totalIterations);
            return mid;
        }
        else if(targetValue > array[mid]){
            min = mid + 1;
                        
        }else{
            max = mid -1;
        }
        totalIterations++;
    }
    
    return position;
};

var primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 
		41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];

var result = doSearch(primes, 2);
console.log("Found prime at index " + result);

