class BMICalculator:
    def __init__(self,weight,height):
        self.weight = weight
        self.height = height
    def bmi(self):
        return self.weight / (self.height**2)
    def category(self):
        bmi_value = self.bmi()  # Call the method correctly
        if bmi_value < 18.5:
            return "underweight"
        elif 18.5 <= bmi_value < 25:
            return "normal"
        else:
            return "overweight"