def addTwoNumbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        rl1 = l1[::-1]
        rl2 = l2[::-1]
        a = int(''.join(str(i) for i in rl1))        
        b = int(''.join(str(j) for j in rl2))
        c = a + b

        return print([int(k) for k in str(c)])        

addTwoNumbers((1, 2, 3), (4, 5, 8))



# def centuryFromYear(year):
#     num = year / 100 - 1
#     split_num = str(num).split('.')
#     int_part = int(split_num[0])
#     return print(int_part + 1)

# centuryFromYear(1889)