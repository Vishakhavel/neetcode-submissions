class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let set = new Set();
        for(const num of nums){

            console.log(num);


            if(set.has(num)) return true;
            set.add(num);
        }

        
        console.log(set);
        return false;
    }
}
