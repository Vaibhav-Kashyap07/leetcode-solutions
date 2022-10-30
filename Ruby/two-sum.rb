def two_sum(nums, target)
    passed = Hash.new
    nums.each_with_index do |n, i|
        if passed.has_key?(target-n)
            return i, passed[target-n]
        end
        passed[n] = i
    end
end