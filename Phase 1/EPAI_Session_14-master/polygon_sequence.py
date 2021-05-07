from polygon import Polygon
class Polygons:
    '''Polygons sequence type class which stores n no of polygons with side length R.
    max_efficiency_polygon property returns Ploygon with max efficiency ratio'''
    def __init__(self, m, R):
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m
        self._R = R
        self._max_efficiency_polygon = None
        
    def __len__(self):
        return self._m - 2
    
    def __repr__(self):
        return f'Polygons(m={self._m}, R={self._R})'
    
    def __iter__(self):
        return self.PolyIter(self._m, self._R)

    class PolyIter:
        def __init__(self, m, R):
            self.m = m + 1
            self.R = R
            self.i = 3
            
        def __iter__(self):
            return self
        
        def __next__(self):
            if self.i >= self.m:
                raise StopIteration
            else:
                polygon = Polygon(self.i, self.R)
                self.i += 1
                return polygon
    
    @property
    def max_efficiency_polygon(self):
        if self._max_efficiency_polygon is None:
            print('Calculating max efficiency polygon...')
            self._max_efficiency_polygon = sorted(self, 
                                 key=lambda p: p.area/p.perimeter,
                                reverse=True)[0]
        return self._max_efficiency_polygon
