for i in range(1,-1,-1):
    try:
        print(1/i, end=' ')

    except:

        print("ERROR", end=' ')

    else:

        print("SAFE", end=' ')

    finally:

        print("DONE", end=' ')