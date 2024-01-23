class person():
    name="ravi"
    age=18
    location="mumbai"
setattr(person,"age",25)
f=getattr(person,'age')
print(f)
