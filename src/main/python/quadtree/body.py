class Body:

    def __init__(self, body_id, mass, x_pos, y_pos, x_vel, y_vel):
        self.body_id = body_id
        self.m = mass
        self.x = x_pos
        self.y = y_pos
        self.vx = x_vel
        self.vy = y_vel

    def get_id(self):
        return self.body_id

    def get_mass(self):
        return self.m

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_vx(self):
        return self.vx

    def get_vy(self):
        return self.vy
