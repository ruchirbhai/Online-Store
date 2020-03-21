# Psuedo code implementation
result = application.listen_on('GET product detail on product with id')

print(result.id)   # -> 1

# ... get more info about object with result.id
# ... we pass the variable data which passes info about result.id

application.render_view('product_detail.html', data)

# The goal int this course is how to populate the data variable
