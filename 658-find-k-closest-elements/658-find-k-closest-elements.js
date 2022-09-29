/**
 * @param {number[]} arr
 * @param {number} k
 * @param {number} x
 * @return {number[]}
 */

    var findClosestElements = function(arr, k, x) {
    return arr
        .reduce((newArr, e) => { newArr.push({diff: Math.abs(e-x), val: e}); return newArr}, [])
        .sort((a,b)=> a.diff-b.diff)
        .map(e=> e.val)
        .slice(0,k)
        .sort((a,b)=> a-b);
    
};