function nextpoint(lattpnt, dir, magnitude) {
    dirdict = {"N": [0, 1], "S": [0, -1], "E": [1, 0], "W": [-1, 0]}
    distance = []
    for(i = 0; i < dirdict[dir].length; i ++) {
        distance[i] = magnitude * dirdict[dir][i];
    }
    finalpnt = []
    for(i = 0; i < lattpnt.length; i ++) {
        finalpnt[i] = lattpnt[i] + distance[i];
    }
    return finalpnt
}

function terminus(lattpnt, directionlist) {
	destination = []
    for(i = 0; i < directionlist.length; i ++) {
        destination[i] = directionlist[i];
    }
    for(i = 0; i < directionlist.length; i ++) {
        for(j = 1; j < directionlist[i].length; j ++) { 
            destination = nextpoint(destination, directionlist[i][j], parseInt(directionlist[i][0]))
        }
    }
    return destination
}

console.log(terminus([-1,1], directionlist = ["1NE"]))