var twoSum = (nums, target) => {
    var map = new Map();
    for (let i = 0; i < nums.length; i++) {
        const n = nums[i];
        const diff = (target - n);

        if (map.has(diff)) return [ i, map.get(diff) ];

        map.set(n, i);
    }
}