class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0,len(nums)-1

        while left <= right :
            mid = left + (right-left) // 2  # 防止整數溢位的常見計算方法
            if nums[mid] == target :
                return mid
            elif nums[mid] < target :
                left = mid + 1 # 往右半部找
            else :
                right = mid -1  # 往左半部找
        
        return -1  # 沒找到返回 -1
