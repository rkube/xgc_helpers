#!/usr/bin/python
#-*- Encoding: UTF-8 -*-

class mesh_triangle():
    """Describes triangles in the grid.
    Members:
    coord_list:  List [(R_i, phi_i, Z_i), i = 1,2,3] for the three vertices
    node_list:  
    (n1, n2 n3):   Tuple of nodes the triangle connects
    """
    
    def __init__(self, n1, n2, n3, node_coord_dict):
        """Describes the coordinates of a triangle in the mesh
        Input:
        ======
        n1, n2, n3:   The nodes of the triangle
        coord_list:        Array with the coordinates of the nodes. Generated by np.genfromtext(.node file, skip_header=1)
        """
        self.node_list = (n1, n2, n3)
        self.coord_list = []
        
        for node in self.node_list:
            #print("Appending " + str(all_nodes[(all_nodes[:,0] == node).nonzero()][0,1:]))
            self.coord_list.append(node_coord_dict.get(node))
        
    def coords(self):
        """Returns a list of coordinates of the three vertices.
        """
        return self.coord_list
    
    
    def coords_R(self):
        """ Returns a list of the R-coordinates for the three vertices.
        """
        res = [coord[0] for coord in self.coord_list]
        return res 

    
    def coords_phi(self):
        """ Returns a list of the phi-coordinates for the three vertices.
        """
        res = [coord[2] for coord in self.coord_list]
        return res
    
    
    def coords_Z(self):
        """ Returns a list of the Z-coordinates for the three vertices.
        """
        res = [coord[1] for coord in self.coord_list]
        return res 

    
    def nodes(self):
        return self.node_list



class xgc_mesh_v2():
    """ Describes the triangle mesh for an XGC simulation.
    
    """
    def __init__(self, ele_array, node_array):
        self.triangle_list = []
        self.num_triangles = ele_array.shape[0]
        
        # Put coordinates of the nodes in a dict for fast lookup
        # Put coordinates of the nodes in a dict for fast lookup
        # Keys in this dictionary are node NUMBERS, as they appear in grid_ele.
        # Remember to ad 1 to the nidx in the loop
        self.node_coord_dict = {}
        for nidx in range(int(grid_node[-1,0])):
            self.node_coord_dict.update({int(nidx) + 1: list(grid_node[int(nidx), 1:])})
    
        i = 0
        for ele in range(self.num_triangles):
            self.triangle_list.append(mesh_triangle(ele_array[ele, 1], 
                                                    ele_array[ele, 2],
                                                    ele_array[ele, 3], self.node_coord_dict))
            i += 1
            if (i%100000 == 0):
                print("triangle {0:6d}/{1:6d}".format(i, self.num_triangles))
            
    
    def get_triangles(self):
        """ Returns the list of triangles.
        """
        
        return self.triangle_list
        

# End of file grid.py