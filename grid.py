#!/usr/bin/python
#-*- Encoding: UTF-8 -*-

class mesh_triangle_2d():
    """Describes triangles in the grid.
    Members:
    coord_list:  List [(R_i, phi_i), i = 1,2,3] for the three vertices
    node_list:  
    (v1, v2 v3):   Tuple of vertices that the triangle consitutes
    """
    
    def __init__(self, v1, v2, v3, coord_lookup):
        """Describes the coordinates of a triangle in the mesh
        Input:
        ======
        v1, v2, v3:   The vertex numbers constituting the triangle
        coord_lookup:   Array with the coordinates of the vertices. This is "/coordinates/values" from xgc.mesh.bp
        """
        self.vertices = (v1, v2, v3)
        self.coord_list = []
        
        for vertex in self.vertices:
            #print("Appending " + str(all_nodes[(all_nodes[:,0] == node).nonzero()][0,1:]))
            self.coord_list.append(list(coord_lookup[vertex, :]))
        
    def coords(self):
        """Returns a list of coordinates of the three vertices.
        """
        return self.coord_list
    
    
    def coords_R(self):
        """ Returns a list of the R-coordinates for the three vertices.
        """
        res = [c[0] for c in self.coord_list]
        return res 

    
    def coords_Z(self):
        """ Returns a list of the Z-coordinates for the three vertices.
        """
        res = [c[1] for c in self.coord_list]
        return res 

    
#    def vertices(self):
#        """ Returns the vertex numbers, as defined in nd_connect_list
#        """
#        return self.vertices



class xgc_mesh():
    """ Describes the triangle mesh for an XGC simulation.
    
    """
    def __init__(self, conns, coords):
        """
        Input:
        ======
        conns: Connections of the vertices. An array of [num_triangles, 3]. This is 'nd_connect_list' from xgc.mesh.bp.
        coords: Coordinates of the vertices. An array of [R, Z]. This is '/coordinates/values' from xgc.mesh.bp

        """
        self.triangle_list = []
        self.num_triangles = conns.shape[0]
        self.num_vertices = coords.shape[0]
        
        for tri in range(self.num_triangles):
            self.triangle_list.append(mesh_triangle_2d(conns[tri, 0], 
                                                       conns[tri, 1],
                                                       conns[tri, 2], coords))
#            if (tri%1000 == 0):
#                print("triangle {0:6d}/{1:6d}".format(tri, self.num_triangles))
    
        
    def get_triangles(self):
        """ Returns the list of triangles that constitute the simulation domain.
        """
        
        return self.triangle_list



# End of file grid.py
