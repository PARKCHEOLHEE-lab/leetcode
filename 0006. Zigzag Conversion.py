class Solution:
    """
        https://leetcode.com/problems/zigzag-conversion/
        
        The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

        ```
        P   A   H   N
        A P L S I I G
        Y   I   R
        ```
        And then read line by line: "PAHNAPLSIIGYIR"

        Write the code that will take a string and make this conversion given a number of rows:

        string convert(string s, int num_rows);

        NOTE:
            row = 2
            A C E G I
            B D F H K
            : 0 1 0 1 0 1 0 1 0 1
        
            row = 3
            A   E   I
            B D F H 
            C   G 
            : 0 1 2 1 0 1 2 1 0
            
            row = 4
            A     G    M
            B   F H   L
            C E   I K 
            D     J 
            : 0 1 2 3 2 1 0 1 2 3 2 1 0 
             
            row = 5
            A       I     Q
            B     H J    P
            C   G   K   O
            D F     L N 
            E       M   
            : 0 1 2 3 4 3 2 1 0 1 2 3 4 3 2 1 0  
    """
    
    def convert(self, s: str, num_rows: int) -> str:
        
        rows = [[] for _ in range(num_rows)]
        pattern = [*range(num_rows), *reversed(range(num_rows)[1:-1])]
        
        for si, each_s in enumerate(s):
            row_index = pattern[si % len(pattern)]
            rows[row_index].append(each_s)
        
        converted_string = "".join("".join(row) for row in rows)
        
        return converted_string