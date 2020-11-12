from djongo import models


class EmployeeData(models.Model):
	name=models.CharField(max_length=20,unique=True)
	date=models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.name
