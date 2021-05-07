import math

class Polygon:
    '''Polygon class which takes input as #edges and side length and it will output #edges, 
    #vertices, interior angle, edge length, apothem, area and perimeter'''
    def __init__(self, n, R):
        if n < 3:
            raise ValueError('Polygon must have at least 3 vertices.')
        self.n = n
        self.R = R
        
    def __repr__(self):
        return f'Polygon(n={self.n}, R={self.R})'
    
    @property
    def count_vertices(self):
        return self.n
    
    @property
    def count_edges(self):
        return self.n
    
    @property
    def circumradius(self):
        return self.R
    
    @property
    def interior_angle(self):
        return (self.n - 2) * 180 / self.n

    @property
    def side_length(self):
        return 2 * self.R * math.sin(math.pi / self.n)
    
    @property
    def apothem(self):
        return self.R * math.cos(math.pi / self.n)
    
    @property
    def area(self):
        return self.n / 2 * self.side_length * self.apothem
    
    @property
    def perimeter(self):
        return self.n * self.side_length
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.count_edges == other.count_edges 
                    and self.circumradius == other.circumradius)
        else:
            return NotImplemented
        
    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.count_vertices > other.count_vertices
        else:
            return NotImplemented