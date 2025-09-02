def analyze_scores(scores):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    lowest = min(numbers)
    hightset = (numbers)
    counter = 0 

    for number in numbers:
        if number >= 70:
            counter +=1
        
    return {
        'sum': total,
        'count': count,
        'average': round(average,2),
        'highest': hightset,
        'passed':counter
    }