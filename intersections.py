from typing import List

def count_overlapping_lines(points: List[str]) -> int:
    """
    Counts the number of overlapping lines in a list of points.

    :param points: A list of points, where each point is a string of the format "s" or "e"
        followed by a number, representing the start or end of a line.

    :return: The number of overlapping lines.
    """

    count = 0
    active_lines = set()
    for point in points:
        is_start = point[0] == "s"
        line_number = int(point[1:])
        if is_start:
            active_lines.add(line_number)
        else:
            count += max(0, len(active_lines)-1)
            if len(active_lines) > 0:
                active_lines.remove(line_number)

    return count

def main():
    intersections = 0
    input_list = []

    # sample input
    # 1. (0.78, 1.47, 1.77, 3.92), (s1, s2, e1, e2)
    # 2. (0.9, 1.3, 1.70, 2.92), (s1, e1, s2, e2)
    # 3. (0.78, 1.47, 1.77, 3.92), (s1, s2, s3, e1, e2, e3)

    input_string = input("Enter the input string: ") # just copy paste the input string
    
    for tup in input_string.split('), ('):
        tup = tup.replace(')','').replace('(','').replace(' ','').replace("_",'')
        input_list.append(tuple(tup.split(',')))

    points = list(map(float, input_list[0])) # we are ignoring the first element of the tuple as it is not needed
    identifiers = list(map(str, input_list[1]))

    intersections = count_overlapping_lines(identifiers)

    print("Number of intersections: ", intersections)

if __name__ == "__main__":
    main()