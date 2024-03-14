def solution(A, B):
    # Step 1: Parse Start and End Times
    start_hour, start_minute = map(int, A.split(":"))
    end_hour, end_minute = map(int, B.split(":"))
    
    # Convert times to total minutes for easier calculation
    start_time = start_hour * 60 + start_minute
    end_time = end_hour * 60 + end_minute
    
    # Step 5: Handle Overnight Play
    if end_time < start_time:
        end_time += 24 * 60  # Add 24 hours to the end time
    
    # Step 2: Calculate Start of First Possible Round
    # Rounds start at 00, 15, 30, 45 - find the next quarter hour after start_time
    if start_minute > 45:
        start_time = start_time + 60 - start_minute
    elif start_minute > 30:
        start_time = start_time + 45 - start_minute
    elif start_minute > 15:
        start_time = start_time + 30 - start_minute
    else:
        start_time = start_time + 15 - start_minute
    
    # Step 3: Calculate End of Last Possible Round
    # Find the last quarter hour before end_time
    end_time = end_time - (end_minute % 15)
    
    # Step 4: Calculate Number of Rounds
    # There's a 15 minute round in each quarter hour, so calculate the number of 15-minute intervals
    num_rounds = (end_time - start_time) // 15
    
    return max(0, num_rounds)  # Ensure the result is not negative

# Example 
print(solution("12:01", "12:44"))  # Expected output: 1
print(solution("20:00", "06:00"))  # Expected output: 40
print(solution("00:00", "23:59"))  # Expected output: 95