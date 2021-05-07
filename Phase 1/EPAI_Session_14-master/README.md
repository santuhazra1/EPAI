## Polygon

#### In this assignment we have implemented two different class in two different module.

#### Polygon:

##### In this class we have implemented such way that it will take input as #edges and side length and it will output #edges, #vertices, interior angle, edge length, apothem, area and perimeter. Also, we have implemented __eq__ method such way that is no of edges and side length is same for two Polygon '==' will return True else False. Similarly, __gt__  method such way that it will return True with garter no of vertices. Also, we have implemented properties such a way that it will be evaluated lazily, so that after calling it once it will be calculated. 

#### Polygons:

##### Here we have implemented a property max_efficiency_polygon which will return maximum efficiency polygon with a lazy evalution. Also, we have made sure that the elements in the iterator are computed lazily. Foe that we have implemented iter and next method to make this class a iterable so that each time next is called it will be evaluated.