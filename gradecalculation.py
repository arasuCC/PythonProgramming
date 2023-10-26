# Function to calculate GPA
def get_gpa(average_mark):
    if 90 <= average_mark <= 100:
        return "A"
    elif 80 <= average_mark < 90:
        return "B"
    elif 70 <= average_mark < 80:
        return "C"
    elif 60 <= average_mark < 70:
        return "D"
    else:
        return "F"
    
# Function to calculate average marks
def get_average_marks(marks):
    return sum(marks) / len(marks)