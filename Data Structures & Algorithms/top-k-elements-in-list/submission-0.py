class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] += 1

        print(frequency)

        buckets = [[] for b in range(len(nums)+1)]
        print(buckets)

        for key,value in frequency.items():
            buckets[value].append(key)

        print(buckets)

        final =[]

        for bucket in buckets[::-1]:
            for bucket_value in bucket:
                if(len(final)!=k):
                    final.append(bucket_value)

        return final