class Rectangle:
  
  def __init__(self,width,height):
    
    self.width = width
    self.height = height
    self.area = 0
    self.perimeter = 0
    self.diagonal = 0
    self.amount_inside = 0
  #width setter 
  def set_width(self,width):
    self.width = width
  #height setter
  def set_height(self,height):
    self.height = height
  #calculate area    
  def get_area(self):
    self.area = self.width * self.height
    return self.area
  #calculate perimeter   
  def get_perimeter(self):
    self.perimeter = (2*self.width)+(2*self.height)
    return self.perimeter
  #find diagonal
  def get_diagonal(self):
    self.diagonal = (self.width**2 + self.height**2)**.5
    return self.diagonal
  #display shape image
  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return 'Too big for picture.'
    else:
      self.pic = ''
      for h in range(self.height):
        self.pic += '*'*self.width
        self.pic += '\n'
    return self.pic
  #find amount of times another shape can fit 
  def get_amount_inside(self,other_shape = ''):
    if isinstance(other_shape,Rectangle) or isinstance(other_shape,Square):
      self.amount_inside = (self.width//other_shape.width)*(self.height//other_shape.height)
    return self.amount_inside
      
  def __str__(self):    
    display = ('Rectangle(width={}, height={})').format(self.width,self.height)
    return display
    
class Square(Rectangle):
  def __init__(self,side_length):
    self.width = side_length
    self.height = side_length 
  #set side length
  def set_side(self,side_length):
    self.width = side_length
    self.height = side_length
  #set width 
  def set_width(self,side_length):
    self.width = side_length
    self.height = side_length
  #set height 
  def set_height(self,side_length):
    self.height = side_length
    self.width = side_length

  def __str__(self):
    display = ('Square(side={})').format(self.height)
    return display
  