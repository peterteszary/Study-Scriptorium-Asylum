student_scores = [150, 142, 185, 120, 171, 165, 134, 65, 76]

total_exam_score = sum(student_scores)

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)