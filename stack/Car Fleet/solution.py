class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 將車輛按其位置排序 (從離終點最近的車開始)
        cars = sorted(zip(position,speed),reverse = True)

        # 初始化堆疊來儲存車隊的到達時間
        stack = []

        for pos,spd in cars:
            time = (target - pos) / spd  # 計算該車到達終點的時間
            if not stack or time > stack[-1]:
                 # 如果堆疊為空或這輛車的到達時間比堆疊頂端的車更晚，它自己是一個新的車隊
                stack.append(time)

        # 堆疊的大小即為車隊的數量
        return len(stack)
