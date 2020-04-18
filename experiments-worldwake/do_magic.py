import arcade
import os
import cv2

import numpy as np
import open3d as o3d


SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Isometric Example"

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 200

MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title, *args, **kwargs):
        """
        Initializer
        """
        super().__init__(width, height, title, *args, **kwargs)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        self.text = arcade.draw_text("this is text", 400, 300, font_size=48, color=arcade.color.AERO_BLUE)


    def on_update(self, delta_time):
        pass
        """ Movement and game logic """


def main():
    """ Main method """
    #window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, update_rate=0.1)
    #arcade.run()


    print("Load a ply point cloud, print it, and render it")
    pcd = o3d.io.read_point_cloud("chest.ply")

    #downpcd = pcd.voxel_down_sample(voxel_size=10)

    #print(np.asarray(downpcd.points))

    vis = o3d.visualization.Visualizer()
    vis.create_window(visible=False)

    vis.add_geometry(pcd)

    vis.run()

    vis.destroy_window()
    vis.close()
    ctr = vis.get_view_control()
    print("Field of view (before changing) %.2f" % ctr.get_field_of_view())

    X = vis.capture_screen_float_buffer(False)
    X = vis.capture_depth_float_buffer()
    Y = np.asarray(X)

    print(Y.shape)

    print(np.sum(Y))

    #cv2.imsave("X", np.asarray(X))

    cv2.imwrite("X.png", np.asarray(X))
    #o3d.visualization.draw_geometries([downpcd])

    #custom_draw_geometry_with_camera_trajectory.vis =
    #vis = o3d.visualization.Visualizer()
    #def move_forward(vis):
    #ctr = vis.get_view_control()
    #image = vis.capture_screen_float_buffer(False)

if __name__ == "__main__":
    main()
