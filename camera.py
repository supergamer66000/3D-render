import glm

FOV = 50 # deg
NEAR = 0.1
FAR = 100

class Camera:
    def __init__(self, app):
        self.app = app
        self.aspect_raio = app.WIN_SIZE[0] / app.WIN_SIZE[1]
        self.position = glm.vec3(2, 3, 3) # Camera Position
        self.up = glm.vec3(0, 1, 0) # ???
        # view matix
        self.m_view = self.get_view_matrix()
        # Projection matrix
        self.m_proj = self.get_projection_matix()
    def get_view_matrix(self):
        return glm.lookAt(self.position, glm.vec3(0, 0, 0), self.up)
    def get_projection_matix(self):
        return glm.perspective(glm.radians(FOV), self.aspect_raio, NEAR, FAR)
