def Kolakoski(n):
    from collections import deque
    import sys


    q = deque([2])
    last = 2
    if n == 1:
        print('1')
    elif n == 2:
        print('12')
    elif n == 3:
        print('122')

    else:
        sys.stdout.write('12')
        sys.stdout.flush()

        for _ in xrange(2,n):
            i = q.popleft()
            last = (last % 2) + 1

            for _ in range(i):
                q.append(last)

            sys.stdout.write(str(i))
            sys.stdout.flush()
