import heapq


def furthesBuilding(heights, bricks, ladders):
    heap = []
    for building_index in range(len(heights) - 1):
        diff = heights[building_index + 1] - heights[building_index]
        if diff <= 0:
            continue
        heapq.heappush(heap, diff)
        if len(heap) > ladders:
            min_diff = heapq.heappop(heap)
            bricks -= min_diff
            if bricks < 0:
                return building_index
    return len(heights) - 1

def main():
    #print('res', carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    print('res', inorderTraversal(heights=[4,2,7,6,9,14,12], bricks=5, ladders=1))



if __name__ == "__main__":
    main()
